# cities = ["Adelaide", "Darwin", "Sydney", "Melbourne"]
#
# with open('cities.txt', 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file, flush=True)
cities = []
with open("cities.txt", "r") as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))

print(cities)
for city in cities:
    print(city)

imelda = "More Mayhem", "Imelda May", '2011', (1, "Pulling the Rug"), (2, "Psycho")

with open("imelda3.txt", "r") as imelda_file:
    print(imelda, file=imelda_file)