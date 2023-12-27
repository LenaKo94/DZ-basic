#lst = [0, 1, 0, 12, 3]
#lst = [0]
#lst = [1, 0, 13, 0, 0, 0, 5]
lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
for i in range(len(lst) - 1, -1, -1):
    if lst[i] == 0:
        pop_element = lst.pop(i)
        lst.append(pop_element)
print(lst)