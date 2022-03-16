input_filename = 'country_info.txt'

countries = {}
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict

# print(countries)

print(countries['afghanistan']['capital'])

while True:
    chosen_country = input('Please enter a name of a country  ').casefold()
    if chosen_country in countries:
        country_data = countries[chosen_country]
        print(f"The capital of {chosen_country.title()} is {countries[chosen_country]['capital']}.")
    elif chosen_country == 'quit':
        break
