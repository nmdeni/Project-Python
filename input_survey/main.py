user_date = []
user_name = input('insert your name -> ')
user_lastname = input('insert your lastname ->')
user_age = input('insert your age ->')

user_date.append(user_name.capitalize())
user_date.append(user_lastname.capitalize())
user_date.append(user_age)

print("\n".join(user_date))