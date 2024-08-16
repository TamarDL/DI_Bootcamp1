username = input('what is your username?')
password = input('enter your password')
password_length = len(password)
hidden_password = "*" * password_length
print (f'{username },your password {hidden_password},have {password_length} letters long')