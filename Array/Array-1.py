import array

val = array.array('i', [1, 2, 3, 4, 5])

val.append(12)
print(val.buffer_info())