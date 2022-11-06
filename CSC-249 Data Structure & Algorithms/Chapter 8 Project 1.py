
#function get number will return a # based on a string of characters
def getNumber(alphabet):
    if alphabet in "ABC":
        return "2"
    elif alphabet in "DEF":
        return "3"
    elif alphabet in "GHI":
        return "4"
    elif alphabet in "JKL":
        return "5"
    elif alphabet in "MNO":
        return "6"
    elif alphabet in "PQRS":
        return "7"
    elif alphabet in "TUV":
        return "8"
    elif alphabet in "WXYZ":
        return "9"
    else:
        return alphabet

# function phone_number will loop through the input when the function is called at the end of the program 
def phone_number(num):
    result = ''
    for ch in num:
        result += getNumber(ch)
    return result


number = input("Enter a phone number to be translated:")
print(phone_number(number))