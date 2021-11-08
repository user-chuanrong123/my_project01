import yaml

file = open('/home/pi/my_project01/Python_Gorge/interface/yaml_file.yaml', 'r', encoding='utf-8')
data = yaml.load(stream=file, Loader=yaml.FullLoader)
file.close()
print(type(data))
print(data)
print(data['content1'])