import random

a = random.randint(0,80)

print("あなたの運勢は")
print("")
if a < 2:
   print("大吉")
elif 2 <= a < 10:
    print("中吉")
elif 10 <= a < 20:
    print("小吉")
elif 20 <= a < 40:
    print("吉")
elif 40 <= a < 50:
    print("末吉")
elif 50 <= a < 55:
    print("凶")
elif 55 <= a < 80:
    print("中凶")
else:
    print("大凶")

