#!/usr/bin/env python3

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J$dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code':$
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # Combine two lists into a dictionary using a while loop
    result = {}
    i = 0
    while i < len(keys) and i < len(values):
        result[keys[i]] = values[i]
        i += 1
    return result

def shared_values(dict1, dict2):
    # Get common values between two dictionaries
    set1 = set(dict1.values())
    set2 = set(dict2.values())
    return set1.intersection(set2)

if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)
