inventory_country_capital = {"Allemagne" : "Berlin", "Canada" : "UQAM", "U.S.A" : "Washington"}
for country in inventory_country_capital.keys():
     print("This country is : ", country, "and his happy place is : ", inventory_country_capital[country])
print(list(inventory_country_capital.values()))

print(list(inventory_country_capital.items()))

print(inventory_country_capital.get("Allemagne"))