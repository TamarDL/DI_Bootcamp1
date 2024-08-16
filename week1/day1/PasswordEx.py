username = input('what is your username?')
password = input('enter your password')
password_length = len(password)
hidden_password = "*" * password_length
print (f'{username },your password: {password},have {len(password)} letters long')