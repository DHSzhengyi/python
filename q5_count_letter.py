#Occurrences of a specified character in a string

string = input("Enter a word / sentence:")
character = input("Enter an alphabet:")

def count_letter(str, ch):
    if len(str) == 0:
        return 0
    elif str[0] == ch:
        return 1 + count_letter(str[1:], ch)
    else:
        return count_letter(str[1:], ch)
    
print(count_letter(string, character))



    
