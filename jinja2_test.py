import urllib3
import jinja2
import yaml

def generate_from_template(template_path, yaml_data, output_path):
    # Load device's Jinja2 template
    with open(template_path, "r") as template_file:
        template_content = template_file.read()

    template = jinja2.Template(template_content)
    # Load YAML device specific data
    with open(yaml_data, "r") as yaml_file:
        data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    # Render full config using template with YAML data
    result = template.render(data)
    # Write the config to the output file
    with open(output_path, "w") as output_file:
        output_file.write(result)

template_path = "templates/2Tier/access.j2"
yaml_data = "inventory_updated_2tier.yml"
output_path = "rendered_access.txt"

generate_from_template(
    template_path=template_path,
    yaml_data=yaml_data,
    output_path=output_path
)