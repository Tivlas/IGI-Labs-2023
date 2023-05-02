def serialize_to_json(obj) -> str:
    """ 
    Function:
    -----------
    Serializes object to josn string

    Parameters:
    -----------
           - obj: object to serialize

    Returns:
    -----------
          - string
    """
    if type(obj) == tuple:
        serialized = []
        for i in obj:
            serialized.append(f"{serialize_to_json(i)}")
        ans = ", ".join(serialized)
        return f"[{ans}]"
    else:
        return f"\"{str(obj)}\""
