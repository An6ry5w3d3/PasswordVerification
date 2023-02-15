from string import ascii_lowercase, ascii_uppercase, digits

def getPasswd(userPasswd):
    print('\n-------------------------')
    specialSimbols = [
        '!', '@', '#', '$', '%', 
        '^', '&', '*', '(', ')',
        '-', '_', '=', '+', '[', 
        '{', ']', '}', '|', ';',
        ':', '"', ',', '<', '.',
        '>', '/', '?']
    
    fLow = fUp = fDig = spec = False

    for s in userPasswd:
        if s in ascii_lowercase:
            fLow = True
        elif s in ascii_uppercase:
            fUp = True
        elif s in digits:
            fDig = True
        elif s in specialSimbols:
            spec = True
    else:
        checkPasswd(userPasswd, [fLow, fUp, fDig, spec])

def checkPasswd(passwd, flags):
    if len(passwd) < 8:
        print('The minimum password length is 8 characters or more! Try again')
        return getPasswd(input('Password: '))
    else:
        if False in flags:
            # Message about lowercase characters
            if flags[0]:
                print('Lowercase characters ✅')
            else:
                print('Lowercase characters ❌')

            # Message about uppercase characters
            if flags[1]:
                print('Uppercase characters ✅')
            else:
                print('Uppercase characters ❌')

            # Message about numeric characters
            if flags[2]:
                print('Numeric characters ✅')
            else:
                print('Numeric characters ❌')

            # Message about special characters
            if flags[3]:
                print('Special characters ✅')
            else:
                print('Special characters ❌')
            
            yesNo = input('\nThe password does not meet all security recommendations! Are you sure you want to set this password? (Y/N): ')
            while yesNo != 'Y' and yesNo != 'N':
                yesNo = input('Please answer (Y/N): ')
            
            if yesNo == 'Y':
                print('\nWelcome to the system!')
            else:
                print('\nGood. Set a new password')
                return getPasswd(input('Password: '))
        else:
            print('Lowercase characters ✅\nUppercase characters ✅\nNumeric characters ✅\nSpecial characters ✅\n\nWelcome to the system!')

getPasswd(input('Password: '))
