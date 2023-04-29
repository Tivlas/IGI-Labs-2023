from . import constants


def get_specific_serializer_function(obj):
    if isinstance(obj, int | float | str | bool | complex | type(None)):
        return serialize_primitive_type
    if isinstance(obj, dict):
        return serialize_dict
    if isinstance(obj, list | tuple | bytes):
        return serialize_default_collection


def serialize(obj) -> tuple:
    """ 
    Function:
    -----------
    Serializes any type

    Parameters:
    -----------
           - obj: object to serialize

    Returns:
    -----------
          - tuple of tuples: {type, value}
    """
    serializer = get_specific_serializer_function(obj)
    serialized_obj = serializer(obj)
    result = tuple((k, serialized_obj[k]) for k in serialized_obj)
    return result


def serialize_primitive_type(obj: float | bool | int | complex | str | None) -> dict:
    """ 
    Function:
    -----------
    Serializes built in primitive types

    Parameters:
    -----------
           - obj (float | bool | int | complex | str | None): object to serialize

    Returns:
    -----------
          - dict: {type: value}
    """
    serialized_primitive_type = dict()
    serialized_primitive_type[constants.TYPE] = type(obj).__name__
    serialized_primitive_type[constants.VALUE] = obj
    return serialized_primitive_type


def serialize_dict(obj: dict) -> dict:
    """ 
    Function:
    -----------
    Serializes dict

    Parameters:
    -----------
           - obj (dict): object to serialize

    Returns:
    -----------
          - dict of tuples: [((type: name), (value: v))] = ((type: name), (value: v))
    """
    serialized_obj = dict()
    serialized_obj[constants.TYPE] = constants.DICT
    serialized_obj[constants.VALUE] = {}

    for k, v in obj.items():
        key = serialize(k)
        value = serialize(v)
        serialized_obj[constants.VALUE][key] = value

    serialized_obj[constants.VALUE] = tuple((k, serialized_obj[constants.VALUE][k])
                                            for k in serialized_obj[constants.VALUE])

    return serialized_obj


def serialize_default_collection(obj: tuple | list | bytes):
    """ 
    Function:
    -----------
    Serializes tuple | list | bytes

    Parameters:
    -----------
           - obj: object to serialize

    Returns:
    -----------
          - dict with tuple
    """
    serialized_obj = dict()
    serialized_obj[constants.TYPE] = type(obj).__name__
    serialized_obj[constants.VALUE] = tuple([serialize(i) for i in obj])
    return serialized_obj
