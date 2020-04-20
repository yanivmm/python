###  exceptions

"""
exceptions
campusIL
Yaniv M
"""


def read_file(file_name):
    try:
        print("__CONTENT_START__")
        f = open(file_name)
    except IOError:
        print("__NO_SUCH_FILE__")
    else:
        f.readtext()
    finally:
        print("__CONTENT_END__")


def send_invitation(name, age):
    try:    
        if int(age) < 18:
            raise underAge(age)
    except underAge as A:
        print("bro, you're young you can come in %s years from now"  %(18-A.get_age()))
    else:
         print("The party will be at the 3/3/21, tou're welcome.")   
            
class underAge(Exception):
    def __init__(self,age):
        self._age = age
    def __str__(self):
        return "The fellow's age -  %s is not on the right range." % self._age
    def get_age(self):
        return int(self._age)   



"""
                Summering excersize about exceptions 
"""

 
specielChars         = '!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~_'
specielCharsWithout_ = '!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~'

def check_input(username, password):
    """the method takes username and password and cheks theirs legality.
    """
    
    if len(username)>16:
        raise usernameTooLong(username)
    if len(username)<3:
        raise usernameTooShort(username)
    if username_conntains_missing_values(username):
        raise UsernameContainsIllegalCharacter(username)
    if len(password)>40:
        raise passwordTooLong(password)
    if len(password)<8:
        raise passwordTooShort(password)     
    if not any(char.isupper() for char in password):
        raise passwordMissingUpperCaseLetter(password)
    if not any(char.islower() for char in password):
        raise passwordMissingLowerCaseLetter(password)
    if not any(char.isdigit() for char in password):
        raise passwordMissingDigit(password)
    if not any(char in specielChars for char in password):
        raise passwordMissingSpecielSign(password)


    print("OK")
    

def username_conntains_missing_values(x):
    """מוצאת אם יש תו חריג וקולטת אותו ומיקומו    
    """
    global charIndex
    global charInIndex
    
    for i in x:
        if i in specielCharsWithout_:
            charIndex = x.find(i)
            charInIndex = i
            return True   
        return False


class usernameTooShort(Exception): 
    """ שם משתמש קצר מידי"""     
    
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "Provided username %s is too short." % self._arg
    def get_arg(self):
        return self._arg
    

class usernameTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "Provided username %s is too long." % self._arg
    def get_arg(self):
        return self._arg


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "Provided username contains illegal character" ,charInIndex , "at index",  charIndex
    def get_arg(self):
        return self._arg

    
class passwordTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "Provided password %s is too short." % self._arg
    def get_arg(self):
        return self._arg
    

class passwordTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "Provided password %s is too long." % self._arg
    def get_arg(self):
        return self._arg


class passwordMissingCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "Provided password %s is missing characters." % self._arg
    def get_arg(self):
        return self._arg


"""
The following classes are all inherit from passwordMissingCharacter Super_Class (wrong password):
"""


class passwordMissingUpperCaseLetter(passwordMissingCharacter):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "Provided password %s is missing characters.(upeer letter)" % self._arg
    def get_arg(self):
        return self._arg
    

class passwordMissingLowerCaseLetter(passwordMissingCharacter):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "Provided password %s is missing characters.(lower letter)" % self._arg
    def get_arg(self):
        return self._arg
    

class passwordMissingSpecielSign(passwordMissingCharacter):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "Provided password %s is missing characters.(speciel sign)" % self._arg
    def get_arg(self):
        return self._arg


class passwordMissingDigit(passwordMissingCharacter):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "Provided password %s is missing characters.(digit)" % self._arg
    def get_arg(self):
        return self._arg


#check_input("A_a1.", "12345678")

def main():
    username = input("please enter username:\n")
    password = input("please enter a password:\n")
    check_input(username,password)
    
main()








