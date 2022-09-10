# Neihbours in the array

def neighbour(a):
    y = 1
    for i in range(0, len(a) - 1):
        if abs(int(a[i + 1]) - int(a[i])) < y:
            position = i
            y = abs(int(a[i + 1]) - int(a[i]))

    if y < 10:
        return f'the index is equal to {position}'
    else:
        return 'there are no neighbours'


a = []
array = input('Input the array:\t').replace(',', '')
a[:0] = array
print(a)

print(neighbour(a))
