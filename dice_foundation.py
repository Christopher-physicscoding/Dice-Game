import random

dice_code = ['\u2680','\u2681', '\u2682', '\u2683','\u2684', '\u2685']
dice_1 = random.choice(dice_code)
dice_2 = random.choice(dice_code)
dice_3 = random.choice(dice_code)
dice_4 = random.choice(dice_code)
dice_5 = random.choice(dice_code)
dice_6 = random.choice(dice_code)

number_of_dice = input("how many dice will you play [1-6]: ")

if number_of_dice == ("1"):
    print(dice_1)
elif number_of_dice == ("2"):
    print(dice_1,dice_2)
elif number_of_dice == ("3"):
    print(dice_1,dice_2,dice_3)
elif number_of_dice == ("4"):
    print(dice_1,dice_2,dice_3,dice_4)
elif number_of_dice == ("5"):
    print(dice_1,dice_2,dice_3,dice_4,dice_5)
elif number_of_dice == ("6"):
    print(dice_1,dice_2,dice_3,dice_4,dice_5,dice_6)
else:
    print("fail")


