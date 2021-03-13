source = input('Enter a list separated by space:')
buscar = input('Search the value:')

input_list = source.split()
print(input_list)
for i in range(len(input_list)):
    if buscar == input_list[i]:
        r = i
        break
    else:
        r = -1


if r != -1:
    print(f'Value found at index {i}')
else:
    print('Value not found')