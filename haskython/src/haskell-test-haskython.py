def incList (integer_list0,):
	if integer_list0 == []:
		return []
	else:
		returnList = [integer_list0[0]+1]
		returnList.extend(incList(integer_list0[1:]))
		return returnList

def decList (integer_list0,):
	if integer_list0 == []:
		return []
	else:
		returnList = [integer_list0[0]-1]
		returnList.extend(decList(integer_list0[1:]))
		return returnList

def sumList (integer_list0,):
	if integer_list0 == []:
		return 0
	else:
		return integer_list0[0] + sumList(integer_list0[1:])

def power (integer0,integer1,):
	if integer1 == 0:
		return 1
	elif integer1 == 1:
		return integer0
	else:
		return integer0 * power(integer0, (integer1 - 1))
