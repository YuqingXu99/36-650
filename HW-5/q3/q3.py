def check_replace(string1, string2): #equal length
    for i in range(len(string1)):
        string_1, string_2 = string1, string2
        string_1 = string_1.replace(string_1[i], '')
        string_2 = string_2.replace(string_2[i], '')
        if string_1 == string_2:
            return True
    return False

def check_insert_remove(string1, string2): #len(string1)>len(string2)
    for i in range(len(string1)):
        string_1 = string1
        if string_1.replace(string_1[i], '') == string2:
            return True
    return False
    
def one_edit(string1, string2):
    if len(string1) == len(string2):
        return check_replace(string1, string2)
    elif len(string1) > len(string2):
        string_long,string_short = string1, string2
    else:
        string_long, string_short = string2, string1
    return check_insert_remove(string_long, string_short)


one_edit("pale", "ple")
one_edit("pales", "pale")
one_edit("pale", "bale")
one_edit("pale", "bake")