person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

# Print the dictionary
print("Person Dictionary:", person)

# Print keys
print("Keys:")
for key in person.keys():
    print(key)

# Print values
print("\nValues:")
for value in person.values():
    print(value)

# Print the value for the 2nd key
second_key = list(person.keys())[1]
second_key_value = person[second_key]

print("The value for the 2nd key '%s' is: %s" % (second_key, second_key_value))

