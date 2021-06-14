from jsonParser.json_parser import Json
from pickleParser.pickle_parser import Pickle
from tomlParser.toml_parser import Toml
from yamlParser.yaml_parser import Yaml


class Serializer:
    def create_serializer(ext):
        if ext == ".json":
            return Json
        elif ext == ".toml":
            return Toml
        elif ext == ".yaml":
            return Yaml
        else:
            return Pickle
