#!/usr/bin/python3
#!/usr/bin/python3
def islower(s):
    if 'a' <= s <= 'z':
        return True
    return False


def uppercase(str):
    for i in str:
        if (islower(i)):
            i = chr(ord(i) - ord('a') + ord('A'))
        print("{0}".format(i), end="")
    print()

        
