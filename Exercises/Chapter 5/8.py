users = ['admin', 'burt', 'anne', 'sue', 'jade']
for user in users:
    if user == 'admin':
        print('Hello {}, would you like to see a status report?'.format(user))
    else:
        print('Hello {}, thank you for logging in again.'.format(user))
