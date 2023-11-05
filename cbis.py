import sys

# sys.setrecursionlimit(70)

def _binary_loc_finder(a_list: list, start: int, end: int, key: int):
	if start == end:
		if a_list[start] > key:
			loc = start
			return loc
		else:
			loc = start + 1
			return loc
	if start > end:
		loc = start
		return loc
	else:
		middle = (start + end) // 2
		if a_list[middle] < key:
			return _binary_loc_finder(a_list, middle + 1, end, key)
		elif a_list[middle] > key:
			return _binary_loc_finder(a_list, start, middle - 1, key)
		else:
			return middle

def _place_inserter(a_list: list, start: int, end: int):
	temp = a_list[end]
	for k in list(range(end, start, -1)):
		a_list[k] = a_list[k - 1]
		k = k - 1
	a_list[start] = temp
	return a_list

# cop = current pointer
# pop = position pointer

def cbis(a_list: list):
	pop = 0
	for i in list(range(1, len(a_list))):
		cop = i
		key = a_list[cop]
		if key >= a_list[pop]:
			place = _binary_loc_finder(a_list, pop + 1, cop - 1, key)
		else:
			place = _binary_loc_finder(a_list, 0, pop - 1, key)
		pop = place
		a_list = _place_inserter(a_list, place, cop)
		i += 1
	return a_list
