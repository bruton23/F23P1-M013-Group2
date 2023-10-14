import pandas as pd

# task 1: reads in characters and binary values from Excel to Python
get = pd.read_excel("F23P1-M013-Group2.xlsx", dtype=str)
bins = list(get["Bin"])
chars = list(get["Char"])
i = chars.index("\\n")
chars[i] = "\n"  # removes one of the slashes for the new line character
o = chars.index("<space>")
chars[o] = " "  # accounts for a space character


# task 2: converts the beginning of the string to its binary equal
def task_2(p1: str):
    if len(p1) >= 3:
        word3 = p1[0:3]  # get the first 3 letters of str
        for i in range(len(chars)):  # loop over indices of chars
            if chars[i] == word3:
                p1 = p1[3:]  # p1 now == letters from 4th letter on
                bVal = bins[i]  # new variable with binary value of first 3 characters
                return bVal, p1
    if len(p1) >= 2:
        word2 = p1[0:2]  # get the first 2 letters of str
        for i in range(len(chars)):  # loop over indices of chars
            if chars[i] == word2:
                p1 = p1[2:]  # p1 now == letters from 3rd letter on
                bVal = bins[i]  # new variable with binary value of first 2 characters
                return bVal, p1
    if len(p1) >= 1:
        for i in range(len(chars)):  # loop over indices of chars
            if chars[i] == p1[0]:
                if len(p1) > 1:
                    p1 = p1[1:]  # p1 now == letters from 2nd letter on
                else:
                    p1 = ""
                bVal = bins[i]  # new variable with binary value of first character
                return bVal, p1


#task 4
def code(fn):
    f = open(fn, "rr")
    s = f.read()
    f.close()

    BinStr = ''
    while (s != ''):
        bVal, s = getBin(s)
        binStr = binStr +bVal

    numBits = len(binStr)
    binStr = str(numBits) + "." + binStr

    f = open("BinOutput.txt", "w+")
    f.write(binStr)
    f.close()


# task 6: double-checks if original input and TextOutput are equal
def task_6(s1: str, s2: str = "TextOutput.txt") -> bool:
    f1 = open(s1)
    r1 = f1.read()  # reads the txt file into a string (r1)
    f2 = open(s2)
    r2 = f2.read()  # reads the second txt file into a second string (r2)
    f1.close()
    f2.close()
    if r1 == r2:
        return True
    else:
        return False

# tested 2, it works individually and returns a tuple (to be used in task 3). task 6 cannot be tested until task
# 5 is added to the project
