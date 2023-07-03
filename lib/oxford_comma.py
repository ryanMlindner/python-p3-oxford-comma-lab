def oxford_comma(items):
    if(len(items) > 1):
        items[-1] = f'and {items[-1]}'
    if(len(items) == 2):
        output = ' '.join(items)
    else: output = ', '.join(items)
    return output
