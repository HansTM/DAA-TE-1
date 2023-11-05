import random

def _partition(A, start, end):
	x = A[end]
	i = start
	for j in range(start, end):
		if A[j] <= x:
			A[i], A[j] = A[j], A[i]
			i += 1
	A[i], A[end] = A[end], A[i]
	return i

def _random_partition(A, start, end):
	i = random.randint(start, end)
	A[end], A[i] = A[i], A[end]
	return _partition(A, start, end)

def _quicksort(A, start, end):
	if start < end:
		q = _random_partition(A, start, end)
		# print(A)
		_quicksort(A, start, q-1)
		_quicksort(A, q + 1, end)

def quicksort(A: list):
	_quicksort(A, 0, len(A) - 1)
	return A
