def serialize_to_json(obj) -> str:
    if type(obj) == tuple:
        serialized = []
        for i in obj:
            serialized.append(f"{serialize_to_json(i)}")
        ans = ", ".join(serialized)
        return f"[{ans}]"
    else:
        return f"\"{str(obj)}\""