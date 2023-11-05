from quicksort import quicksort
from cbis import cbis
from gendata import read_data
from pathlib import Path
import time
import gc
from pympler import asizeof 
import psutil

process = psutil.Process()

for func in [quicksort, cbis]:
	for type in ['sorted', 'reversed', 'random']:
		for num in [200, 2000, 20000]:
			
			print(f"{func.__name__} {type} {num}:")
			total_time = 0
			total_size = 0
			iters = 3

			for i in range(0, iters):
				data = None
				gc.collect()
				data = read_data(Path('data', f'{type}_{num}.txt'))

				start_time = time.time()
				start_size = process.memory_info().rss
				
				func(data)

				iter_size = process.memory_info().rss - start_size
				iter_time = time.time() - start_time
				total_time += iter_time
				total_size += iter_size
				
				print(f'{round(iter_time * 1000, 4)}ms {iter_size}')

				time.sleep(0.5)
			
			print(f'{round((total_time/iters) * 1000, 4)}ms {round(total_size/3, 4)}')
