#!/usr/bin/env python

from jinja2 import Template
import os

def main():
    template_dir = os.path.join(os.getcwd(), 'templates')

    if not os.path.isdir(template_dir):
        print(f'{template_dir} is not a directory!')
        exit(1)

    for filename in os.listdir(template_dir):
        if filename.endswith('.yaml'):
            template_path = os.path.join(template_dir, filename)
            rendered_template = read_template(template_path)
            write_rendered_template(rendered_template, filename)

def read_template(template_path):
    if not os.path.isfile(template_path):
        print(f'{template_path} is not a file!')
        exit(1)

    print(f'Found {template_path}, processing...')

    with open(template_path, 'r') as template_file:
        template = Template(template_file.read())

    rendered_template = template.render()
    return rendered_template

def write_rendered_template(rendered_template, filename):
    output_dir = os.path.join(os.getcwd(), 'output')
    output_path = os.path.join(output_dir, filename)

    if not os.path.isdir(output_dir):
        print(f'Did not find {output_dir}, creating...')
        os.mkdir(output_dir)

    with open(output_path, 'w') as output_file:
        output_file.write(rendered_template)

if __name__ == "__main__":
    main()
