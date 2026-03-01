def input_type(value:str)-> str:
    try:
        int(value)
        return 'integer'
    except ValueError:
        pass
    try:
        float(value)
        return 'double'
    except ValueError:
        pass
    return 'string'



value = input()
print(input_type(value))