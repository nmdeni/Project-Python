user_date = []
user_name = input('insert your name -> ')
user_lastname = input('insert your lastname -> ')
user_age = input('insert your age -> ')
user_hobby = input('insert your hobby (separated by commas soccer,chess) -> ')
# user_work = input('insert where you work or learning -> ')
# user_childrens = input('insert do you have children\'s -> ')
# user_married = input('insert do you married -> ')

user_date.append('Name - ' + user_name.capitalize())
user_date.append('Lastname - ' + user_lastname.capitalize())
user_date.append( 'Age - ' + user_age)
user_date.append(user_hobby.split(','))
# user_date.append('Lastname - ' + user_lastname.capitalize())
# user_date.append( 'Age - ' + user_age)

print(user_date)