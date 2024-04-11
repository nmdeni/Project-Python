user_date = {
    'user_id':'',
    'user_name':'',
    'user_lastname':'',
    'user_age':'',
    'user_work':'',
    'user_hobby':[]
}
#
for key,val in user_date.items():
    if key == 'user_id':
        user_date[key] = (1)
    else:
        user_date[key] = input('insert ' + str(key) + ' -> ')

print(user_date)