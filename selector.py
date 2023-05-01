from random import randint

num_list = []

while True:
    tmp = randint(1, 45)
    if len(num_list) == 6:
        num_list.sort()
        break
    elif tmp not in num_list:
        num_list.append(tmp)
    else:
        continue

print(num_list)