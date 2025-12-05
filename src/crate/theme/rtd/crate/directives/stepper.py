# -*- coding: utf-8; -*-
"""
Stepper directive for step-by-step documentation.

Step 2: Detect nested step directives and count them
"""

from docutils import nodes
from sphinx.util.docutils import SphinxDirective


class StepperDirective(SphinxDirective):
    """Container for step-by-step instructions."""

    has_content = True

    def run(self):
        # Create a container to hold the content
        container = nodes.container()
        container['classes'].append('stepper')

        # Parse nested content (this will process :::{step} directives)
        self.state.nested_parse(
            self.content,
            self.content_offset,
            container
        )

        # Count how many steps we detected
        step_count = 0
        for child in container.children:
            if 'stepper-step' in child.get('classes', []):
                step_count += 1

        # For Step 2, add a debug message showing step count
        debug_msg = nodes.paragraph(
            text=f"Detected {step_count} steps"
        )
        debug_msg['classes'].append('stepper-debug')

        # Return debug message first, then the container
        return [debug_msg, container]


class StepDirective(SphinxDirective):
    """Individual step in a stepper."""

    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True  # Allow spaces in title

    def run(self):
        # Create step container
        step = nodes.container()
        step['classes'].append('stepper-step')

        # Get the title (all arguments combined into one)
        if self.arguments:
            title = self.arguments[0]
        else:
            title = "Untitled"

        # Create a paragraph with the title
        title_para = nodes.paragraph(text=f"Step: {title}")
        title_para['classes'].append('step-title')
        step += title_para

        # Parse step content
        self.state.nested_parse(
            self.content,
            self.content_offset,
            step
        )

        return [step]


def setup(app):
    """Register the stepper directives."""
    app.add_directive('stepper', StepperDirective)
    app.add_directive('step', StepDirective)

    return {
        'version': '0.2',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
