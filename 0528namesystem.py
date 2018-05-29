#名字管理器
#打印功能
print("="*50)
print('Name System')
print('1: add new name')
print('2: delet name')
print('3: revise name')
print('4: search name')
print('5: quite')
print("="*50)
name = []
#獲取用戶的選擇
#根據選擇，執行相印功能
while True:
	num = int(input("please enter the option: "))
	if num == 1:
		new_name = input("enter the name: ")
		name.append(new_name)
		print(name)

	elif num == 2:
		de_name = input("enter the name you want to remove: ")
		name.remove(de_name)
		print(name)
	elif num == 3:
	    a = input("enter the name you want to change: ")
	    if a in name:
	    	b = input("enter the correct name: ")
	    	loc = name.index(a)
	    	name[loc] = b
	    	print(name)
	    else:
	    	print("not in list")
	elif num == 4:
		find_name = input("enter the name you want to find: ")
		if find_name in name:
			print("in list")
		else:
			print("not in list")
	elif num == 5:
		break
	else:
		print("wrong option, enter again")



