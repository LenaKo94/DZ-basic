lst= [1, 3, 5]
#lst=[6]
#lst=[]
every_second_element = lst[::2]
sum_of_elements = sum(every_second_element)
last_element = lst[-1]
result = sum_of_elements * last_element if lst else 0
print(result)