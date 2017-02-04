import random
from random import randint

def name():
    number = int(input('Number of employees buying the Powerball ticket'))
    for i in range(number):
        first_name = str(input('Enter you first name:'))
        last_name = str(input('Enter your last name:'))

        first = int(input('Select 1st # (1 thru 69):'))
        second = int(input('Select 2nd # (1 thru 69 excluding 1st):'))
        third = int(input('Select 3rd # (1 thru 69 excluding 1st and 2nd):'))
        fourth = int(input('Select 4th # (1 thru 69 excluding 1st, 2nd and 3rd):'))
        fifth = int(input('Select 5th # (1 thru 69 excluding 1st, 2nd, 3rd and 4th):'))
        sixth = int(input('Select Powerball # (1 thru 26):'))

        fav_nos = []
        fav_nos.append(first)
        fav_nos.append(second)
        fav_nos.append(third)
        fav_nos.append(fourth)
        fav_nos.append(fifth)

        for x in range(len(fav_nos) - 1):
            for y in range(len(fav_nos) - 1):
                if x == y:
                    y += 1
                if fav_nos[x] == fav_nos[y] or sixth == fav_nos[y]:
                    fav_nos[y] = randint(1,70)
                    y -= 1

        print(first_name, last_name, '{!r} {!r} {!r} {!r} {!r} Powerball: {!r}'.format(fav_nos[0], fav_nos[1], fav_nos[2], fav_nos[3], fav_nos[4], sixth))

def powerball():
    name()
    print("Powerball winning numbers:")
    list1 = []
    for i in random.sample(range(1,70),5):
        list1.append(i)
    power_ball = random.choice(range(1,27))
    print('{!r} {!r} {!r} {!r} {!r} Powerball: {!r}'.format(list1[0],list1[1],list1[2],list1[3],list1[4], power_ball))
    
powerball()




