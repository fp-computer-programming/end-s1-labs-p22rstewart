# Author RTS 1/28/22

def middle(s):
    mid = len(s) // 2 # Dividing the string
    if len(s) % 2 == 0: # Checking to see if the string is even
        return s[(mid - 1): (mid + 1)] # returns the middle
    else: # This is the odd string
        return s[mid] # returns the middle


print(middle("Ryan") == "ya")
print(middle("Nolan") == "l")
print(middle("no") == "no")
