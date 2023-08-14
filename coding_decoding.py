import random
import string

characters = string.ascii_letters + string.digits
r1 = ''.join(random.choice(characters) for _ in range(3))
characters = string.ascii_letters + string.digits

r2 = ''.join(random.choice(characters) for _ in range(3))


st = input("Enter the String: ")
words = st.split(" ")
coding = input("1. Coding\n2. Decoding : ")
coding = True if (coding == '1') else False

if coding:
    nwords = []
    for word in words:
        if 3 <= len(word) <= 5:

            stnew = r1 + word[1:3] + r2 + word[0] + r1 + word[3:] + r2
            nwords.append(stnew)
        elif len(word) > 5:
            stnew = r1 + word[1:3] + r2 + word[0] + r1 + word[3:6] + r2 +word[6:] +r1
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    nwords = []
    for word in words:
        if 3 <= len(word) <= 5:
            stnew = word[8] + word[3:5] + word[12:-3]
            nwords.append(stnew)
        elif len(word) > 5:
            stnew = word[8] + word[3:5] + word[12:15] + word[18:-3]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))


