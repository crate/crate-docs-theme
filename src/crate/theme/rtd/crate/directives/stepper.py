# -*- coding: utf-8; -*-
"""
Stepper directive for step-by-step documentation.
"""

from docutils import nodes
from sphinx.util.docutils import SphinxDirective


# Define custom nodes
class stepper_node(nodes.General, nodes.Element):
    pass

class step_node(nodes.General, nodes.Element):
    pass

class StepperDirective(SphinxDirective):
    """Container for step-by-step instructions."""

    has_content = True
    option_spec = {
        'class': str, # directives.class_option is for multiple classes
    }

    def run(self):
        stepper = stepper_node()
        stepper['classes'] = self.options.get('class', '').split() # Add custom classes if provided
        self_content = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, self_content)

        step_number = 1
        for child in self_content.children:
            if isinstance(child, step_node):
                child['step-number'] = step_number
                step_number += 1
            stepper += child # Add all children from self_content to stepper

        return [stepper]


class StepDirective(SphinxDirective):
    """Individual step in a stepper."""

    has_content = True
    required_arguments = 1  # Step title
    optional_arguments = 0
    final_argument_whitespace = True  # Allow spaces in title
    option_spec = {
        'class': str,
    }

    def run(self):
        step = step_node()
        step['classes'] = ['stepper-step']
        step['classes'].extend(self.options.get('class', '').split())

        # Set title
        step['step-title'] = self.arguments[0]

        # Parse content
        self.state.nested_parse(
            self.content,
            self.content_offset,
            step
        )
        return [step]

# HTML Translator functions
def html_visit_stepper_node(self, node):
    self.context.append('')
    self.body.append(self.starttag(node, 'div', CLASS='stepper'))

def html_depart_stepper_node(self, node):
    self.body.append('</div>\n')
    self.context.pop()

def html_visit_step_node(self, node):
    self.context.append('')
    self.body.append(self.starttag(node, 'div', CLASS='stepper-step'))
    self.body.append(f'<div class="stepper-header">')
    self.body.append(f'<div class="stepper-number">{node.get("step-number", "")}</div>')
    self.body.append(f'<div class="stepper-title">{node.get("step-title", "")}</div>')
    self.body.append(f'</div>')
    self.body.append(f'<div class="stepper-content">')

def html_depart_step_node(self, node):
    self.body.append('</div>\n') # Close stepper-content
    self.body.append('</div>\n') # Close stepper-step
    self.context.pop()


def setup(app):
    """Register the stepper directives and nodes."""
    app.add_node(stepper_node, html=(html_visit_stepper_node, html_depart_stepper_node))
    app.add_node(step_node, html=(html_visit_step_node, html_depart_step_node))

    app.add_directive('stepper', StepperDirective)
    app.add_directive('step', StepDirective)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
