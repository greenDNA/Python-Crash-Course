current_users = ['tim', 'joan', 'sally', 'billy', 'jade']
new_users = ['Jade', 'jim', 'bob', 'Joan', 'amber']
for user in new_users:
    if user.lower() in [name.lower() for name in current_users]:
        print('you need to enter a new username {}'.format(user))
    else:
        print('username is available {}'.format(user))
