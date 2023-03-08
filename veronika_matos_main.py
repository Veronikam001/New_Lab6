def encode(password):

    new_pass = ''
    for elem in password[::]:
        if elem == '0':
            new_pass += '3'
        if elem == '1':
            new_pass += '4'
        if elem == '2':
            new_pass += '5'
        if elem == '3':
            new_pass += '6'
        if elem == '4':
            new_pass += '7'
        if elem == '5':
            new_pass += '8'
        if elem == '6':
            new_pass += '9'
        if elem == '7':
            new_pass += '0'
        if elem == '8':
            new_pass += '1'
        if elem == '9':
            new_pass += '2'
    return new_pass

def decode(password):                   # Decode functions the same as the encode function.
    new_pass = ''
    for elem in password[::]:
        if elem == '0':
            new_pass += '3'
        if elem == '1':
            new_pass += '4'
        if elem == '2':
            new_pass += '5'
        if elem == '3':
            new_pass += '6'
        if elem == '4':
            new_pass += '7'
        if elem == '5':
            new_pass += '8'
        if elem == '6':
            new_pass += '9'
        if elem == '7':
            new_pass += '0'
        if elem == '8':
            new_pass += '1'
        if elem == '9':
            new_pass += '2'

    return new_pass


if __name__ == '__main__':
    print('Menu', '\n-------------', '\n1. Encode', '\n2. Decode', '\n3. Quit', '\n')
    x = input('Please enter an option:')
    password = 'a'      # Created a password variable to store password input by user
    while x != '3':
        if x == '1':
            password = input('Please enter your password to encode:')
            encode(password)
            print('Your password has been encoded and stored!')
            print('Menu', '\n-------------', '\n1. Encode', '\n2. Decode', '\n3. Quit', '\n')
            x = input('Please enter an option:')
            # Added the first comment
            # Additional comment for 2nd change
        if x == '2':        # Actual decode happens here, prints the encoded password with defined decode, then prints original password
            decode(password)
            print(f'The encoded password is {decode(password)}, and the original password is {password}')
            print('Menu', '\n-------------', '\n1. Encode', '\n2. Decode', '\n3. Quit', '\n')
            x = input('Please enter an option: ')
        if x == '3':    # Added a quit function
            quit()
