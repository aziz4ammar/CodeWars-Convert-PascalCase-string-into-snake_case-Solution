def to_underscore(string):
    if not isinstance(string, str):
        return str(string)

    result = [string[0].lower()]

    for char in string[1:]:
        if char.isupper():
            result.extend(['_', char.lower()])
        else:
            result.append(char)

    return ''.join(result)