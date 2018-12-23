quick_sort = lambda array: array if len(array) <= 1 else quick_sort([i for i in array[1:] if i <= array[0]]) + [array[0]] + quick_sort([i for i in array[1:] if i > array[0]])


test = [5,2,4, 6, 1, 3]
print quick_sort(test)

