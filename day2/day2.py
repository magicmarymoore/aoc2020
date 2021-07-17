'''
★ ° •. advent of code 2020 .• ° ★
'''

#imports
import data

#data setup
#x = data.DATA.splitlines()
#print(sorted(x))

#part 1
def passwordsCheck(passwords : list) -> int:
    passwords = passwords
    letter, pswd = '', ''
    low, high, n, total = 0,0,0,0

    for a in passwords:

        if a[1] == '-': #first num == single digit

            if a[3] == ' ': #second num == single digit
                low = int(a[0])
                high = int(a[2])
                letter = a[4]
                pswd = a[7:]
                for b in pswd:
                    if b == letter: n += 1
                if n >= low and n <= high: total += 1
                n = 0

            elif a[4] == ' ': #second num == double digit
                low = int(a[0])
                high = int(a[2:4])
                letter = a[5]
                pswd = a[8:]
                for b in pswd:
                    if b == letter: n += 1
                if n >= low and n <= high: total += 1
                n = 0

        elif a[2] == '-': #first num == double digit
            low = int(a[:2])
            high = int(a[3:5])
            letter = a[6]
            pswd = a[9:]
            for b in pswd:
                if b == letter: n += 1
            if n >= low and n <= high: total += 1
            n = 0
    
    return total

print(passwordsCheck(data.NEW_DATA))

#part 2
def passwordsCheckV2(passwords : list) -> int:
    passwords = passwords
    letter, pswd = '', ''
    low, high, n, total = 0,0,0,0

    for a in passwords:
        print(a)
        if a[1] == '-': #first num == single digit

            if a[3] == ' ': #second num == single digit
                low = int(a[0])
                high = int(a[2])
                letter = a[4]
                pswd = a[7:]
                
                if a[low+6] == letter: n+= 1
                if a[high+6] == letter: n+= 1
                if n == 1: total += 1
                n = 0

            elif a[4] == ' ': #second num == double digit
                low = int(a[0])
                high = int(a[2:4])
                letter = a[5]
                pswd = a[8:]
                
                if a[low+7] == letter: n+= 1
                if a[high+7] == letter: n+= 1
                if n == 1: total += 1
                n = 0

        elif a[2] == '-': #first num == double digit
            low = int(a[:2])
            high = int(a[3:5])
            letter = a[6]
            pswd = a[9:]
           
            if a[low+8] == letter: n+= 1
            if a[high+8] == letter: n+= 1
            if n == 1: total += 1
            n = 0
    
    return total

print(passwordsCheckV2(data.NEW_DATA))