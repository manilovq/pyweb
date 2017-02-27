import yaml

with open('config/test.yaml') as file:
    file_content = file.read()

config = yaml.load(file_content)

print(config)
print(type(config))
print(type(config['alphakey']))
