from serializers.json_serializer.JsonSerializer import JsonSerializer
from serializers.factory import SerializersFactory
from os import path, getcwd


def create_path(path_part: str):
    return path.join(getcwd(), "temp_serialized_files", path_part)


sz = SerializersFactory.create_serializer("JSON")
a = None
with open(create_path("primitive_type.json"), 'w', encoding='utf-8') as f:
    sz.dump(a, f)

dct = {"a": 4, "b": 3, 3: "string"}
with open(create_path("dict.json"), 'w', encoding='utf-8') as f:
    sz.dump(dct, f)
