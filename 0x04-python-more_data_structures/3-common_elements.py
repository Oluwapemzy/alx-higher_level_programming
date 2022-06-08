#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_element = []
    for item in set_1:
        for val in set_2:
            if item == val:
                common_element.append(item)
    return common_element
