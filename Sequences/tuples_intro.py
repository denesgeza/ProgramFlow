t = ("a", "b", "c")
u = 'a', 'b', 'c'
print(t)
print(u)

metallica = ("Ride the Lightning", 'Metallica', 1984)

print(metallica[0])
print(metallica[1])
print(metallica[2])

# metallica[2] = 1986 # --> doesn't work

# it works with a list
metallica2 = list(metallica) # transform tuple to list
metallica2[2] = 1986
print(metallica)
print(metallica2)

title, artist, year = metallica
print(title)
print(artist)
print(year)

table = ('Coffee table', 200, 100, 25.5)
print(table[1] * table[2])
name, length, width, price = table
print(length * width)

# NOTE
# tupples are immutable, we cannot assign a value to a tupple
# tupples are safer than list and use less memory
#