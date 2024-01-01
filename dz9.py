import random
my_list = []
for i in range(random.randint(6, 15)):
    my_list.append(random.randint(1, 1000))
print(my_list)
if len(my_list) >= 3:
    result = [my_list[0], my_list[2], my_list[-2]]
    print(result)

