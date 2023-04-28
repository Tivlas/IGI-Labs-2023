from . import constants


def get_specific_serializer_function(obj):
    if isinstance(obj, int | float | str | bool | complex | type(None)):
        return serialize_primitive_type


def serialize(obj):
    serializer = get_specific_serializer_function(obj)
    serialized_obj = serializer(obj)
    return tuple((k, serialized_obj[k]) for k in serialized_obj)


def serialize_primitive_type(obj: float | bool | int | complex | str | None) -> dict:
    serialized_primitive_type = dict()
    serialized_primitive_type[constants.TYPE] = type(obj).__name__
    serialized_primitive_type[constants.VALUE] = obj
    return serialized_primitive_type
