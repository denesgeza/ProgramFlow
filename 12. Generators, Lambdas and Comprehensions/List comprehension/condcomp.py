menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]
 
# for meal in menu:
#     if "spam" not in meal:
#         # print(meal)

meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
# print(meals)

fussy_meals = [meal for meal in menu if ("spam" in meal or "eggs" in meal)
               if not ("bacon" in meal and "sausage" in meal)]
# print(fussy_meals)

# Conditional expressions
x = 15
expression = "Twelve" if x == 12 else "unknown"
print(expression)

meals = [meal if "spam" not in meal else "a meal skipped" for meal in menu]
# print(meals)

# for meal in menu:
    # print(meal, 'contains chicken' if 'chicken' in meal else 'contains bacon'
    # if 'bacon' in meal else 'contains eggs')

items = set()
for meal in menu:
    for item in meal:
        items.add(item)

for meal in menu:
    for item in items:
        if item in meal:
            # print('{} contains {}'.format(meal, item))
            break

for x in range(31):
    fizzbuzz = 'fizz buzz' if x % 15 == 0 else 'fizz' if x % 3 == 0 else 'buzz' if x % 5 == 0 else str(x)
    print(fizzbuzz)
