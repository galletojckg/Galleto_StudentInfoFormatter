first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
favorite_subject = input("Enter favorite subject: ")

first_last_name = " ".join([first_name, last_name])
full_name = first_last_name.title()

name_code = first_last_name.upper()

formatted_section = section.upper()

favorite_subject_formatted = favorite_subject.title()

character_count = len(first_last_name)

print("\nFormatted Output:")
print(f"Name: {full_name}")
print(f"Name Code: {name_code}")
print(f"Section: {formatted_section}")
print(f"Favorite Subject: {favorite_subject_formatted}")
print(f"Character Count: {character_count}")
