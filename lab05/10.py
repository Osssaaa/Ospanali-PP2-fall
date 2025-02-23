import re
def camel_to_snake(camel_str):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str).lower()

print(camel_to_snake("convertToSnakeCase"))