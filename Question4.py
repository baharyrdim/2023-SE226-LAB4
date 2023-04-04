dictionary = {}
for i in range(1, 31):
    dictionary[i] = (i-1) * i
print(dictionary)

for key, value in dictionary.items():
    print(key, value)

sum = 0
for value in dictionary.values():
    sum += value
print("Total:" , sum)

while True:
    user_input = input("Enter a number between 1 and 30 to remove from the dictionary: ")
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input in dictionary:
            del dictionary[user_input]
            print(dictionary)
            break
        else:
            print("The number is not in the dictionary.")
    else:
        print("Invalid input. Please enter a number.")