def build_profile(first, last, **user_info):
    user = {}
    user['first'] = first
    user['last'] = last
    for key, value in user_info.items():
        user[key] = value
    return user
myself = build_profile('Trayvont', 'York',
                        location='NY',
                        education='Senior',
                        driver='Permit'
                    )
print(myself)
