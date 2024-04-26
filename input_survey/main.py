def view_tree():
    pass
def view_user():
    pass
def add_user():
    pass
def rem_user():
    pass

def edit_user():
    pass

user_date = {
    'user_id':'',
    'user_name':'',
    'user_lastname':'',
    'user_age':'',
    'user_status':'',
    'user_work':'',
    'user_info':''
}

for key,val in user_date.items():
    if key == 'user_id':
        user_date[key] = (1)
    elif key == 'user_name' or key == 'user_lastname':
        user_date[key] = input('insert ' + str(key) + ' -> ').title()
    else:
        user_date[key] = input('insert ' + str(key) + ' -> ')

print("*** USER INFORMATION ***")
for key,val in user_date.items():
    print(f"{key.replace('user_','').title()} => {val}")

view_tree()