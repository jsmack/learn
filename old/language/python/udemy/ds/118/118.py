"""
[DEFAULT]
debug = False

[web_server]
host = 127.0.0.1
por = 80

[db_server]
host = 127.0.0.1
port = 3306
"""


import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {
    'debug': True
}

config['web_server'] = {
    'host': '127.0.0.1',
    'port': 80
}

config['db_server'] = {
    'host': '127.0.0.1',
    'port': 3306
}

with open('config.ini', 'w') as config_file:
    config.write(config_file)


config = configparser.ConfigParser()
config.read('config.ini')
print(config)
for _v in config:
    for _vv in config[_v]:
        print(config[_v][_vv])