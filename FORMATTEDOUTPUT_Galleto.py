first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
favorite_subject = input("Enter favorite subject: ")

first_last_name = " ".join([first_name, last_name])

character_count = len(first_last_name)

print("\nOutput:")
print(f"Name: {first_last_name}")
print(f"Name Code: {first_last_name}")
print(f"Section {section}")
print(f"Favorite Subject: {favorite_subject}")
print(f"Character Count: {character_count}")