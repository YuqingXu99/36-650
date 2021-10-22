


def remove_punc(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for character in string:
        if character in punctuations:
            string = string.replace(character,'')
    return string

string = "Hello in 36-650, & other MSP courses."
remove_punc(string)