# PASSWORD GENRATOR....



import string
import random

if __name__ == '__main__':
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    plen = int(input("Enter the lenght of your password...\n"))
    s = []
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)

    #print(s)
    random.shuffle(s)
    print(''.join(s[0:plen]))