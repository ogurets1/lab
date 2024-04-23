def copy_without_value(lst, value):

    result = [x for x in lst if x != value]
    return result