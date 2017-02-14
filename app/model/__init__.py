import yaml 

from orator import DatabaseManager, Model

with open('config/database.yaml') as file:
    config = yaml.load(file.read())

db = DatabaseManager(config)

Model.set_connection_resolver(db)
