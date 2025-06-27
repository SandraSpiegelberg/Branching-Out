import json

def filter_users_by_name(name):
    """
    Filtering users by their name from a JSON file.
    :params: name (str): The name to filter users 
    :returns: None
    """
    with open("users.json", "r") as file:
        users = json.load(file)
    
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    
    for user in filtered_users:
        print(user)

def filter_by_age(age):
    """
    Filtering users by their age from a JSON file.
    :params: age (int): The age to filter users 
    :returns: None
    """
    with open("users.json", "r") as file:
        users = json.load(file)
    
    filtered_users = [user for user in users if user["age"] == age]
    
    for user in filtered_users:
        print(user)

def filter_by_email(email):
    """
    Filtering users by their email from a JSON file.
    :params: email (str): The email to filter users 
    :returns: None
    """
    with open("users.json", "r") as file:
        users = json.load(file)
    
    filtered_users = [user for user in users if user["email"].lower() == email.lower()]
    
    for user in filtered_users:
        print(user)

def filter_options():
    """ 
    Prompting user for filter options and calling the appropriate function to filtering the entered value of the user.
    :params: None
    :returns: None
    """
    filter_option = input("What would you like to filter by? (Currently, only 'name', 'age' or 'email' is supported): ").strip().lower()
    
    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)    
    elif filter_option == "age":
        age_to_search = int(input("Enter an age to filter users: ").strip())
        filter_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")

if __name__ == "__main__":
    filter_options()