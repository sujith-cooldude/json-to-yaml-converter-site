import yaml
import json
def convert_json_to_yaml(text_data):
    js_data = json.loads(text_data)
    result = yaml.safe_dump(js_data)
    return result
