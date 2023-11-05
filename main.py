from quicksort import quicksort
from cbis import cbis
from gendata import read_data
from pathlib import Path
import time
import gc

A = [5,4,3,2,1]
B = [46, 24, 25, 71, 72, 84, 60, 87, 91, 96, 45, 20, 61, 48, 22, 21]

print(quicksort(A.copy()))
print(cbis(A.copy()))
