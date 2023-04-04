divided = {1:['Tony', 41] , 2:['Rhodey', 43], 3:['Nat', 35]}
we_fall = {4:['Steve', 39], 5:['Clint', 35], 6:['Wanda', 28]}
merged_dictionary1 = divided.copy()
merged_dictionary1.update(we_fall)

print("{:<10} {:<10}".format('NAME', 'AGE'))
for key, value in merged_dictionary1.items():
    name, age = value
    print("{:<10} {:<10}".format(name, age))

divided2 = {'Tony': 41, 'Rhodey': 43, 'Nat': 35}
we_fall2 = {'Steve': 39, 'Clint': 35, 'Wanda': 28}
merged_dictionary = divided2.copy()
merged_dictionary.update(we_fall2)

del merged_dictionary['Nat']
print(merged_dictionary)

sort_list = sorted(merged_dictionary.items(), key=lambda u: u[1])

for s in sort_list:
    print(s[0], s[1])

key_max = max(merged_dictionary.keys(), key=(lambda k: merged_dictionary[k]))
key_min = min(merged_dictionary.keys(), key=(lambda k: merged_dictionary[k]))

print('Maximum Value: ', merged_dictionary[key_max])
print('Minimum Value: ', merged_dictionary[key_min])