

# Escribe un programa que una dos listas y se ordenen de forma ascendente

import random

random_numbers1 = []
random_numbers2 = []
random_list = []
random_list2 = []

for i in range(1,21,1):
	random_number = random.randint(1,20)
	random_numbers1.append(random_number)
	random_number = random.randint(1,20)
	random_numbers2.append(random_number)
	
print(random_numbers1)
print(random_numbers2)

random_list = random_numbers1 + random_numbers2

random_list.sort()
for number in random_list:
	if number not in random_list2:
		random_list2.append(number)

	#print(number)

#print(random_list)
print(random_list2)
