import random

# every password has 16 characters

English = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
capital = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
others = ["@", "$", "%", "^", "&", "*", "(", ")", "_", "/", "?"]

total = [English, capital, numbers, others]

def Password_Generator():
    passwd = ""
    password = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 16):
        if password[i] == 0:
            password[i] = random.choice(random.choice(total))
    for j in password:
        passwd += j
    print(passwd)
    

Password_Generator()