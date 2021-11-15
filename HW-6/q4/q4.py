def delete_keys(keys,dictionary):
    for key in keys:
        if key in dictionary:
            del dictionary[key]
    return dictionary

dict = {"firstName": "Mohamed", "lastName": "Farag", "birthYear": 1990, "nationality": "Egyptian"}
a = delete_keys(["lastName","birthYear"],dict)
print(a)