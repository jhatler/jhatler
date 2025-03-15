#!/usr/bin/env python3

"""
This renders the given Jinja2 template with the provided YAML data.
"""

import sys

import yaml
from jinja2 import Environment, FileSystemLoader


def main():
    """
    Main function to render the Jinja2 template with YAML data.
    """

    # first argument is the template name
    # rest of the arguments are data files
    if len(sys.argv) < 4:
        print("Usage: python render.py <template> <output> [<data_file> ...]")
        sys.exit(1)

    data = {}
    template_name = sys.argv[1]
    output_name = sys.argv[2]
    for data_file in sys.argv[3:]:
        with open(data_file, "r", encoding="utf-8") as f:
            data.update(yaml.safe_load(f))

    # Create a Jinja2 environment
    env = Environment(loader=FileSystemLoader("."))

    # Load the template
    template = env.get_template(template_name)

    # Render the template with the data
    with open(output_name, "w", encoding="utf-8") as f:
        f.write(template.render(data=data))
        f.write("\n")

    print(f"Rendered {output_name} successfully.")


if __name__ == "__main__":
    main()
