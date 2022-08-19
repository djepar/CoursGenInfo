inventory_country_capital = {"Allemagne" : "Berlin", "Canada" : "UQAM", "U.S.A" : "Washington"}
for country in inventory_country_capital.keys():
     print("This country is : ", country, "and his happy place is : ", inventory_country_capital[country])
for capital in inventory_country_capital.values():
     print(capital)

print(inventory_country_capital.get('Allemagne'))

print(inventory_country_capital.get('Quc', 'Allo'))

for (l, i) in inventory_country_capital.items():
     print("got", l, "that maps to ", i)

print(inventory_country_capital['Canada'])

keylist = list(inventory_country_capital.keys())
print(keylist)

all = list(inventory_country_capital)
print(all)

inventory = inventory_country_capital
print(inventory['Canada'])
inventory['Canada'] = 'left'
print(inventory_country_capital['Canada'])
