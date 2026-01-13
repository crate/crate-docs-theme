#!/bin/bash
set -e

# =============================================================================
# Multi-Project Documentation Testing
# =============================================================================
#
# Builds multiple doc projects and serves them together to test e.g. cross-project
# navigation (sidebar TOC links) in a production-like URL structure.
#
# PROBLEM: When developing locally with `make dev`, each project runs in
# isolation. Links to other projects (e.g., /docs/cloud/ from guide) don't
# work. This script builds all projects statically and serves them together.
#
# USAGE:
#   ./test-multi-project.sh              # Default: reset, parallel, local theme
#   ./test-multi-project.sh --help       # Show all options
#
# CONFIGURATION:
#   Edit PROJECTS array below to add/remove projects.
#   Format: "directory-name:url-path"
#
# OUTPUT:
#   Builds to devtools/_multi-project-build/ and serves at
#   http://localhost:8000/docs/guide
#
# NOTES:
#   - No live-reload: re-run script after editing docs
#   - Modifies requirements.txt files (creates .bak backups) in all projects
#   - Revert with: git checkout */docs/requirements.txt
#
# =============================================================================

# Project definitions: "directory:url-path"
# Paths are relative to the root of this project folder.
ROOT="../../"
PROJECTS=(
    "cratedb-guide:guide"
    "cloud-docs:cloud"
    #"crate:crate-reference"
    "../crate-admin:crate/admin-ui"
    "../croud:cloud/cli"
    "../crash:crate/crash"
    "../crate-python:python"
    "../crate-jdbc:jdbc"
    "../crate-pdo:pdo"
    "../crate-dbal:dbal"
    "../sqlalchemy-cratedb:sqlalchemy-cratedb"
)

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

# Default options (optimized for theme development)
DO_RESET=true
PARALLEL=true
LOCAL_THEME=true
QUIET=true

show_help() {
    cat << 'EOF'
Multi-Project Documentation Testing

Builds (make html) multiple doc projects and serves them together to test
cross-project navigation in a production-like URL structure. Serves at
http://localhost:8000/docs/guide.

USAGE:
    ./test-multi-project.sh [options]

OPTIONS:
    --skip-reset      Skip 'make reset' before building
    --sequential      Build projects sequentially instead of parallel
    --remote-theme    Use PyPI theme instead of local
    -v, --verbose     Show full build output
    -h, --help        Show this help message

DEFAULTS:
    All flags default to ON for typical theme development workflow:
    - Reset build cache before each build
    - Build projects in parallel
    - Use local crate-docs-theme (by adjusting docs/requirements.txt!)
    - Quiet mode (errors only)

EXAMPLES:
    ./test-multi-project.sh                    # Standard workflow
    ./test-multi-project.sh --remote-theme     # Test with PyPI theme
    ./test-multi-project.sh --verbose          # Debug build issues
    ./test-multi-project.sh --sequential -v    # Ordered verbose output

CONFIGURATION:
    Edit PROJECTS array in this script to add/remove projects.
    Format: "directory-name:url-path"

EOF
    exit 0
}

# Parse options
while [[ $# -gt 0 ]]; do
    case $1 in
        --skip-reset)
            DO_RESET=false
            shift
            ;;
        --sequential)
            PARALLEL=false
            shift
            ;;
        --remote-theme)
            LOCAL_THEME=false
            shift
            ;;
        -v|--verbose)
            QUIET=false
            shift
            ;;
        -h|--help)
            show_help
            ;;
        *)
            echo "Unknown option: $1"
            echo "Use --help for usage"
            exit 1
            ;;
    esac
done

# Path setup
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
THEME_PATH="$(cd "$SCRIPT_DIR/.." && pwd)"
ROOT="$(cd "$SCRIPT_DIR/$ROOT" && pwd)"
COMBINED_DIR="$SCRIPT_DIR/_multi-project-build"

echo -e "${BLUE}=== Multi-Project Testing ===${NC}"
echo "Theme: $THEME_PATH"
echo "Root: $ROOT"
echo "Output: $COMBINED_DIR"
echo "Options: reset=$DO_RESET parallel=$PARALLEL local-theme=$LOCAL_THEME quiet=$QUIET"
echo ""

# Verify theme path
if [ "$LOCAL_THEME" = true ] && [ ! -f "$THEME_PATH/setup.py" ]; then
    echo -e "${RED}ERROR: Theme not found at $THEME_PATH${NC}"
    exit 1
fi

# Validate all project paths exist before building
echo -e "${BLUE}Validating project paths...${NC}"
MISSING_PROJECTS=()
for project in "${PROJECTS[@]}"; do
    IFS=':' read -r dir path <<< "$project"
    PROJECT_PATH="$ROOT/$dir/docs"
    if [ ! -d "$PROJECT_PATH" ]; then
        MISSING_PROJECTS+=("$dir -> $PROJECT_PATH")
    fi
done

if [ ${#MISSING_PROJECTS[@]} -gt 0 ]; then
    echo -e "${RED}ERROR: The following projects were not found:${NC}"
    for missing in "${MISSING_PROJECTS[@]}"; do
        echo -e "${RED}  - $missing${NC}"
    done
    echo ""
    echo "Please adjust the PROJECTS array in this script."
    echo "Comment out missing projects or fix the paths."
    exit 1
fi
echo -e "${GREEN}All ${#PROJECTS[@]} projects found${NC}"
echo ""

# Clean previous build
rm -rf "$COMBINED_DIR"
mkdir -p "$COMBINED_DIR/docs"

# Setup local theme in requirements.txt
setup_local_theme() {
    local project_path=$1
    local requirements_file="$project_path/requirements.txt"

    if [ ! -f "$requirements_file" ]; then
        echo -e "${RED}  No requirements.txt at $requirements_file${NC}"
        return 1
    fi

    local theme_line="-e $THEME_PATH"

    # Already using local theme?
    if grep -q "^-e.*crate-docs-theme" "$requirements_file"; then
        return 0
    fi

    # Comment out remote theme if present
    if grep -q "^crate-docs-theme" "$requirements_file"; then
        sed -i.bak 's/^crate-docs-theme/#crate-docs-theme/' "$requirements_file"
    fi

    # Prepend local theme
    echo "$theme_line" | cat - "$requirements_file" > "$requirements_file.tmp"
    mv "$requirements_file.tmp" "$requirements_file"
    return 0
}

# Build a single project
build_project() {
    local project=$1
    IFS=':' read -r dir path <<< "$project"

    local PROJECT_PATH="$ROOT/$dir/docs"

    if [ ! -d "$PROJECT_PATH" ]; then
        echo -e "${RED}Project not found: $PROJECT_PATH${NC}"
        return 1
    fi

    echo -e "${BLUE}Building $dir...${NC}"

    # Setup local theme
    if [ "$LOCAL_THEME" = true ]; then
        setup_local_theme "$PROJECT_PATH" || return 1
    fi

    local TEMP_OUTPUT=$(mktemp)

    # Reset if requested
    if [ "$DO_RESET" = true ]; then
        if [ "$QUIET" = true ]; then
            if ! (cd "$PROJECT_PATH" && make reset > "$TEMP_OUTPUT" 2>&1); then
                echo -e "${RED}Reset failed for $dir:${NC}"
                cat "$TEMP_OUTPUT"
                rm -f "$TEMP_OUTPUT"
                return 1
            fi
        else
            (cd "$PROJECT_PATH" && make reset) || { rm -f "$TEMP_OUTPUT"; return 1; }
        fi
    fi

    # Build HTML
    if [ "$QUIET" = true ]; then
        if ! (cd "$PROJECT_PATH" && make html > "$TEMP_OUTPUT" 2>&1); then
            echo -e "${RED}Build failed for $dir:${NC}"
            cat "$TEMP_OUTPUT"
            rm -f "$TEMP_OUTPUT"
            return 1
        fi
    else
        (cd "$PROJECT_PATH" && make html) || { rm -f "$TEMP_OUTPUT"; return 1; }
    fi

    rm -f "$TEMP_OUTPUT"

    # Verify build
    local BUILD_DIR="$PROJECT_PATH/.crate-docs/.build"
    if [ ! -d "$BUILD_DIR" ]; then
        echo -e "${RED}No build output for $dir${NC}"
        return 1
    fi

    echo -e "${GREEN}Built $dir${NC}"
    return 0
}

# Execute builds
if [ "$PARALLEL" = true ]; then
    echo -e "${BLUE}Building in parallel...${NC}"
    echo ""

    declare -a PIDS
    declare -a PROJECTS_STARTED

    for project in "${PROJECTS[@]}"; do
        build_project "$project" &
        PIDS+=($!)
        PROJECTS_STARTED+=("$project")
    done

    ALL_SUCCESS=true
    for i in "${!PIDS[@]}"; do
        if ! wait "${PIDS[$i]}"; then
            IFS=':' read -r dir path <<< "${PROJECTS_STARTED[$i]}"
            echo -e "${RED}Failed: $dir${NC}"
            ALL_SUCCESS=false
        fi
    done

    [ "$ALL_SUCCESS" = false ] && exit 1
else
    for project in "${PROJECTS[@]}"; do
        build_project "$project" || exit 1
    done
fi

echo ""
echo -e "${BLUE}Copying to combined structure...${NC}"

# Copy builds to combined directory
for project in "${PROJECTS[@]}"; do
    IFS=':' read -r dir path <<< "$project"

    PROJECT_PATH="$ROOT/$dir/docs"
    BUILD_DIR="$PROJECT_PATH/.crate-docs/.build"
    TARGET_DIR="$COMBINED_DIR/docs/$path"

    [ ! -d "$BUILD_DIR" ] && continue

    mkdir -p "$(dirname "$TARGET_DIR")"
    cp -r "$BUILD_DIR" "$TARGET_DIR"
    echo -e "${GREEN}Copied $dir -> /docs/$path${NC}"
done

echo ""
echo -e "${GREEN}=== Build Complete ===${NC}"
echo ""

if [ "$LOCAL_THEME" = true ]; then
    echo -e "${BLUE}Note: requirements.txt files modified (revert with git checkout)${NC}"
    echo ""
fi

echo -e "${BLUE}Server: http://localhost:8000/docs/guide/${NC}"
echo "Press Ctrl+C to stop"
echo ""

cd "$COMBINED_DIR"
python3 -m http.server 8000
