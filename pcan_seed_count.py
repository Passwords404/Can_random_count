#!-*- coding:utf-8 -*-

can_seed_file = "xxx.txt"

can_seed_number = []
can_seed_repeat = {}

with open(can_seed_file, 'r') as f1:
    list1 = f1.readlines()
#print(list1)


for i in range(0, len(list1)):
	if "06 67" in list1[i]:
		seed_number = list1[i][40:63]
		#print(seed_number)
		can_seed_number.append(seed_number)
print(can_seed_number)

#
# # 对seed进行统计
for i in can_seed_number:
	print(i)
	if i in can_seed_repeat.keys():
		can_seed_repeat[i] = can_seed_repeat[i] + 1
	else:
		can_seed_repeat[i] = 1
#
#
file_write_obj = open("count.txt", 'w')
#
for q in can_seed_repeat:
	seed_count_number = "seed numer's {} ==> {}".format(q, can_seed_repeat[q])
	file_write_obj.writelines(seed_count_number)
	file_write_obj.writelines("\n")
