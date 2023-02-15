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
        print('Your password is too short!\nUse complex passwords to protect your data!')
        return getPasswd(input('Passwd: '))
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
            
            print('\nThe password should protect your data, and not be an easy target for scammers! Try again')
            return getPasswd(input('Passwd: '))
        else:
            print('Lowercase characters ✅\nUppercase characters ✅\nNumeric characters ✅\nSpecial characters ✅\n\nWelcome to the system!')

getPasswd(input('Passwd: '))
