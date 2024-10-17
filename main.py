import random
import timeit
import numpy as np
import matplotlib.pyplot as plt

def stoogesort(arr, l, h): 
    if l >= h: 
        return
  
    # Если первый элемент больше последнего, поменять их местами 
    if arr[l] > arr[h]: 
        arr[l], arr[h] = arr[h], arr[l] 
  
    # Если в списке 2 элемента, то сортировка завершена 
    if h - l + 1 > 2: 
        t = (int)((h - l + 1) / 3) 
        # Рекурсивно сортировать первые 2/3 элемента 
        stoogesort(arr, l, (h - t)) 
        # Рекурсивно сортировать последние 2/3 элемента 
        stoogesort(arr, l + t, (h)) 
        # Рекурсивно сортировать первые 2/3 элемента еще раз,
        # чтобы убедиться, что они находятся в правильном порядке 
        stoogesort(arr, l, (h - t)) 

def generate_random_sequence(length):
    sequence = list(range(length))
    random.shuffle(sequence)
    return sequence

def measure_sorting_time(sort_func, sequence):
    l, h = 0, len(sequence) - 1
    return timeit.timeit(lambda: sort_func(sequence, l, h), number=1)

def perform_measurements(sort_func):
    sizes = list(range(1000, 11000, 1000))
    time_data = []

    for size in sizes:
        measurements = []
        for _ in range(10):
            sequence = generate_random_sequence(size)
            measurements.append(measure_sorting_time(sort_func, sequence))
        time_data.append(measurements)

    return sizes, np.array(time_data)

def plot_graph(lengths, mean_times):
    plt.plot(lengths, mean_times, marker='o')
    plt.xlabel('Длина последовательности')
    plt.ylabel('Время выполнения (сек)')
    plt.title('Время выполнения блуждающей сортировки (stooge sort)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    lengths, time_data = perform_measurements(stoogesort)
    mean_times = np.mean(time_data, axis=1)
    plot_graph(lengths, mean_times)