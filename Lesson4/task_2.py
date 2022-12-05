source = [1, 2, 33, 4, 5]


def recursive_max(list_to_find_max: list):
    if len(list_to_find_max) == 1:
        return list_to_find_max[0]
    else:
        max_num = recursive_max(list_to_find_max[1:])
        if max_num > list_to_find_max[0]:
            return max_num
        else:
            return list_to_find_max[0]


print(recursive_max(source))