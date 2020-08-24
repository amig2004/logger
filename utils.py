def checkData(dictobj: dict, fields: list):
    """Check if given dict contain all necessary field"""
    return list(dictobj.keys) == fields