def neat(first_name, last_name):
    """function that returns neatly formatted names """
    full_name = f"{first_name.title()} {last_name.title()}"
    return full_name


author = neat('christopher', 'steiner')
print(author)


# default parameters to manage a specific condition.
def neat(first_name='No first name provided', last_name='No last name provided.'):
    """function that returns neatly formatted names """
    full_name = f"{first_name.title()} {last_name.title()}"
    return full_name


author = neat('christopher')
print(author)

# default parameters to support optional arguments
def neat(first_name='No first name provided', last_name='No last name provided.', middle_name = ''):
    """function that returns neatly formatted names """
    if middle_name:
        full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        full_name = f"{first_name.title()} {last_name.title()}"
    return full_name


author = neat('christopher')
print(author)
author = neat(first_name='mayuri', middle_name= 'B', last_name='upadhaya')
print(author)

