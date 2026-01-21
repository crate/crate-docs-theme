# -*- coding: utf-8; -*-
"""
Stepper directive for step-by-step documentation.

Usage (MyST markdown):
```
:::{stepper}
## First step
Content for first step.

## Second step
Content for second step.

### Nested heading
This stays inside step two.
:::
```

Each heading at the first level inside the stepper becomes a numbered step.
Deeper headings remain as nested content within their parent step.
"""

import re
from docutils import nodes
from sphinx.util.docutils import SphinxDirective


class stepper_node(nodes.General, nodes.Element):
    """Container node for the stepper component."""
    pass


class step_node(nodes.General, nodes.Element):
    """Individual step node within a stepper."""
    pass


class step_title_node(nodes.General, nodes.Element):
    """Step title node that renders as a proper heading element."""
    pass


class StepperDirective(SphinxDirective):
    """Container for step-by-step instructions.

    Converts MyST markdown headings into numbered steps while preserving
    their level and anchors for deep linking. Only the first heading level
    encountered becomes steps; deeper headings stay nested within steps.
    """

    has_content = True
    option_spec = {
        'class': str,
    }

    def run(self):
        stepper = stepper_node()
        stepper['classes'] = self.options.get('class', '').split()

        # Pre-scan content to detect heading levels from MyST markdown
        # and determine the step level (first heading level found)
        heading_levels = {}
        step_level = None
        for line in self.content:
            match = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
            if match:
                level = len(match.group(1))
                title = match.group(2).strip()
                slug = nodes.make_id(title)
                heading_levels[slug] = level
                # First heading level becomes the step level
                if step_level is None:
                    step_level = level

        # Parse the content
        container = nodes.container()
        self.state.nested_parse(self.content, self.content_offset, container)

        step_number = 1
        current_step = None
        intro_content = []

        for child in container.children:
            if isinstance(child, nodes.rubric):
                # Get heading info
                heading_id = child.get('ids', [''])[0] if child.get('ids') else ''
                heading_text = child.astext()
                heading_level = heading_levels.get(heading_id, 3)

                # Only treat as new step if at the step level
                if heading_level == step_level:
                    # Close previous step if any
                    if current_step is not None:
                        stepper += current_step

                    # Add intro content before first step
                    if intro_content:
                        for item in intro_content:
                            stepper += item
                        intro_content = []

                    # Create new step
                    current_step = step_node()
                    current_step['step-number'] = step_number
                    current_step['classes'] = ['stepper-step']

                    # Create step title node
                    title_node = step_title_node()
                    title_node['ids'] = child.get('ids', [])
                    title_node['level'] = heading_level
                    title_node['text'] = heading_text
                    current_step += title_node

                    step_number += 1
                else:
                    # Nested heading - add as content within current step
                    if current_step is not None:
                        # Convert rubric to a proper heading node for nested headings
                        title_node = step_title_node()
                        title_node['ids'] = child.get('ids', [])
                        title_node['level'] = heading_level
                        title_node['text'] = heading_text
                        current_step += title_node
                    else:
                        intro_content.append(child)
            else:
                if current_step is not None:
                    current_step += child
                else:
                    intro_content.append(child)

        if current_step is not None:
            stepper += current_step

        if intro_content:
            for item in intro_content:
                stepper += item

        return [stepper]


# HTML Translator functions

def html_visit_stepper_node(self, node):
    self.body.append(self.starttag(node, 'div', CLASS='stepper'))


def html_depart_stepper_node(self, node):
    self.body.append('</div>\n')


def html_visit_step_node(self, node):
    step_number = node.get('step-number', '')
    self.body.append('<div class="stepper-step">\n')
    self.body.append(f'<div class="stepper-number">{step_number}</div>\n')
    self.body.append('<div class="stepper-content">\n')


def html_depart_step_node(self, node):
    self.body.append('</div>\n')  # Close stepper-content
    self.body.append('</div>\n')  # Close stepper-step


def html_visit_step_title_node(self, node):
    level = node.get('level', 3)
    heading_id = node.get('ids', [''])[0] if node.get('ids') else ''
    text = node.get('text', '')

    id_attr = f' id="{heading_id}"' if heading_id else ''
    headerlink = ''
    if heading_id:
        headerlink = (
            f'<a class="headerlink" href="#{heading_id}" '
            f'title="Link to this heading">¶</a>'
        )
    self.body.append(f'<h{level}{id_attr}>{text}{headerlink}</h{level}>\n')
    raise nodes.SkipNode


def html_depart_step_title_node(self, node):
    pass  # Not called due to SkipNode


def setup(app):
    """Register the stepper directive and nodes."""
    app.add_node(
        stepper_node,
        html=(html_visit_stepper_node, html_depart_stepper_node)
    )
    app.add_node(
        step_node,
        html=(html_visit_step_node, html_depart_step_node)
    )
    app.add_node(
        step_title_node,
        html=(html_visit_step_title_node, html_depart_step_title_node)
    )

    app.add_directive('stepper', StepperDirective)

    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
