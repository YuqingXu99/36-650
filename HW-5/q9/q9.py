def palindrome(string):
    if len(string) == 1:
        return True
    else:
        start, end = 0, len(string)-1
        if string[start] != string[end]:
            return False
        else:
            string_short = string[start+1: end]
            return palindrome(string_short)

palindrome("kayak")
palindrome("hello")
            