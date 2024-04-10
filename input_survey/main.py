user_date = []
user_name = input('insert your name -> ')
user_lastname = input('insert your lastname -> ')
user_age =input('insert your age -> ')

user_date.append('Name - ' + user_name.capitalize())
user_date.append('Lastname - ' + user_lastname.capitalize())
user_date.append( 'Age - ' + user_age)

print("\n".join(user_date))