from ..src.serialization import serialize
from .serialization_logic import serialize_to_json


class JsonSerializer:
    @staticmethod
    def dumps(obj) -> str:
        serialized_obj = serialize(obj)
        return serialize_to_json(serialized_obj)

    def dump(obj, file):
        file.write(JsonSerializer.dumps(obj))
