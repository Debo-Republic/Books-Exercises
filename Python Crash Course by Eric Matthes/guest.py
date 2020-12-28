# Program to make a guest list.

# Asking user for their names.
while True:
    user_name_temp = input('Please enter your first and last name.')
    print(f"Very glad to have you in our guest book.")
    with open('guest_list.txt', 'a') as file_objects:
        file_objects.write(user_name_temp.strip())
        file_objects.write("\n")
    flag = input("Do you want to continue ? Y/N")
    if flag == 'N':
        break



