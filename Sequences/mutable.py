computer_parts = ['PC',
                  'monitor',
                  'keyboard',
                  'mouse',
                  'mouse pad',
                  ]

another_list = computer_parts
print(id(computer_parts))
print(id(another_list))

print('Adding cookies')
computer_parts += ['cookies']
print(computer_parts)
print(id(computer_parts))

a = b = c = d = e = another_list

print(a)

print('phone case')
print('Adding case')
b.append('case')

print(c)
