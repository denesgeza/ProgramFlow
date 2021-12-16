from contents import pantry

chicken_quantity = pantry.setdefault('chicken', 0)
print(f"chicken: {chicken_quantity}")

# if the item doesn't exist it adds the key to the dictionary
beans_quantity = pantry.setdefault('beans', 0)
print(f"beans: {beans_quantity}")

# it just gets back if the value exists, doesn't add the value to the dictionary
ketchup_quantity = pantry.get('ketchup', 0)
print(f'ketchup: {ketchup_quantity}')

z_quantity = pantry.setdefault("zucchini", 'eight')
print(f'zucchini: {z_quantity}')

print(pantry)
