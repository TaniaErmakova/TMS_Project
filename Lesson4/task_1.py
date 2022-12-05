source = [1, 2, 3, 4, 5]


def recursive_reverse(list_to_reverse: list):
    if len(list_to_reverse) == 0:
        return []
    else:
        reversed_part_list = recursive_reverse(list_to_reverse[1:])
        return reversed_part_list + [list_to_reverse[0]]


print(recursive_reverse(source))



