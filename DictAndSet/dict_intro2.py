vehicles = {'dream': 'Honda 250T',
            'roadster': 'BMW R1100',
            'er5': 'Kawasaki ER5',
            'can-am': 'Bombardier Can-Am',
            'jimny': 'Suzuki Jimny 1.5',
            'fiesta': 'Ford Fiesta 1.4',
            'virago': 'Dacia Duster',
            'starfighter': "Lockheed F-104",
            'learjet': 'Bombardier LearJet 75',
            'toy': 'glider'
            }

# for key in vehicles:
#     print(key, vehicles[key], sep=", ")
# add a new key to dictionary
vehicles['work'] = 'Audi A4'

# update the virago key
vehicles['virago']: 'Dacia Duster'

# delete a key from a dictionary
del vehicles['toy']

# del vehicles['f1']
# vehicles.pop('f1')  # KeyError -> key doesn't exist

# pop, check if it exists, if not returns str, 'You wish'
print('-' * 80)
result = vehicles.pop('f1', 'You wish!')
print(result)
print('-' * 80)

for key, value in vehicles.items():
    print(key, value, sep=', ')
