

def order_by_value(dictionary:dict)->list:


    def key_to_val(key:str)->int:
        return dictionary[key]


    return sorted(dictionary.keys(), key=key_to_val)


my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True