from . import constants


def create_deserializer(obj_type):
    if obj_type == constants.DICT:
        return deserialize_dict
    if obj_type == constants.FUNCTION:
        return deserialize_function
    if obj_type in constants.DEFAULT_COLLECTION_TYPES:
        return deserialize_default_collection
    if obj_type == constants.CLASS:
        return deserialize_class
    if obj_type in constants.PRIMITIVE_TYPES:
        return deserialize_primitive_type
    if obj_type == constants.OBJECT:
        return deserialize_any_obj
    if obj_type == constants.MODULE_NAME:
        return deserialize_module


def deserialize(obj):
    obj = dict((a, b) for a, b in obj)
    obj_type = obj[constants.TYPE]
    deserializer = create_deserializer(obj_type)

    if deserializer is None:
        return

    return deserializer(obj_type, obj[constants.VALUE])


def deserialize_primitive_type():
    pass


def deserialize_default_collection():
    pass


def deserialize_dict():
    pass


def deserialize_function():
    pass


def deserialize_class():
    pass


def deserialize_module():
    pass


def deserialize_any_obj():
    pass
