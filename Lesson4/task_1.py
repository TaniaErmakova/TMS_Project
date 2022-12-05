source = [1, 2, 3, 4, 5]


def recursive_reverse(list_to_reverse: list) -> list:
    if len(list_to_reverse) == 1:
        return list_to_reverse
    else:
        reversed_part_list = recursive_reverse(list_to_reverse[1:])
        reversed_part_list.append(list_to_reverse[0])
        return reversed_part_list


print(recursive_reverse(source))



