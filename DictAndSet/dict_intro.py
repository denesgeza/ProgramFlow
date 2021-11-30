vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta 1.4',
    'virago': 'Yamaha XV2500'
}

my_car = vehicles['fiesta']
print(my_car)

commuter = vehicles['jimny']
print(commuter)

learner = vehicles.get('roadster')
print(learner)