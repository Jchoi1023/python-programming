#CIS41 - Jihye Choi
#Enter valid email address

user_input = input("Enter an email address:")

if '@' in user_input and '.' in user_input:
    at_index = user_input.index('@')
    dot_index = user_input.index('.')
    if at_index < dot_index:
        domain_name = user_input[at_index + 1: dot_index]
        print("Domain name:", domain_name)
    else:
        print("Invalid email address.")
else:
    print("Invalid email address.")

    '''
Enter an email address:joe@yahoo.com
Domain name: yahoo

Enter an email address:jihye@gmail.com
Domain name: gmail

    '''