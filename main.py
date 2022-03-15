class Euro:
    """
    class of the coin euro
    """
    def __init__(self,amountOfEuro):
        """
        Ctor to reset the values

        :param amountOfEuro: amount of the coin
        """
        self._=amountOfEuro
    def amount(self):
        """
        calculates and prints the amount of the coin in shekels
        """
        valInShekel=self._*rates.get(('euro', 'nis'))
        print(valInShekel)
    def __add__(self, num2):
        """
        prints the result of adding the two coins that given

        :param num2: the other coin
        """
        print(addOperator(self,num2))
    def NameOfType(self):
        """
        gives the type of the class

        :return: string of type of the class
        """
        return("Euro")
    def __str__(self):
        """
        gives the amount of the coin with its sign

        :return: string of the amount of the coin with its sign
        """
        return f'{self._}€'
    def __repr__(self):
        """
        gives the amount of coin* value to convert to shekel

        :return: string of the amount of coin * value to convert to shekel
        """
        mulValue = rates.get(('euro', 'nis'))
        return f'{self._}*{mulValue}'


class Dollar:
    """
        class of the coin dollar
        """
    def __init__(self, amountOfDollar):
        """
                Ctor to reset the values

                :param amountOfEuro: amount of the coin
                """
        self._ = amountOfDollar
    def amount(self):
        """
               calculates and prints the amount of the coin in shekels
               """
        valInShekel=self._*rates.get(('dollar', 'nis'))
        print(valInShekel)
        #return self._
    def __add__(self, num2):
        """
                prints the result of adding the two coins that given

                :param num2: the other coin
                """
        print(addOperator(self,num2))
    def NameOfType(self):
        """
                gives the type of the class

                :return: string of type of the class
                """
        return("Dollar")
    def __str__(self):
        """
                gives the amount of the coin with its sign

                :return: string of the amount of the coin with its sign
                """
        return f'{self._}$'
    def __repr__(self):
        """
                gives the amount of coin* value to convert to shekel

                :return: string of the amount of coin * value to convert to shekel
                """
        mulValue=rates.get(('dollar', 'nis'))
        return f'{self._}*{mulValue}'



class Shekel:
    """
        class of the coin shekel
        """
    def __init__(self, amountOfShekel):
        """
                Ctor to reset the values

                :param amountOfEuro: amount of the coin
                """
        self._ = amountOfShekel
    def amount(self):
        """
               calculates and prints the amount of the coin in shekels
               """
        print(self._)
       # return self._
    def __add__(self, num2):
        """
                prints the result of adding the two coins that given

                :param num2: the other coin
                :return:
                """
        print(addOperator(self, num2))
    def NameOfType(self):
        """
                gives the type of the class

                :return: string of type of the class
                """
        return("Shekel")
    def __str__(self):
        """
                gives the amount of the coin with its sign

                :return: string of the amount of the coin with its sign
                """
        return f'{self._}nis'
    def __repr__(self):
        """
                gives the amount of coin* value to convert to shekel

                :return: string of the amount of coin * value to convert to shekel
                """
        return f'{self._}'

def isEuro(num):
    """
    checks if the type of coin is euro

    :param num: coin
    :return: true or false
    """
    return type(num) ==Euro
def isDollar(num):
    """
        checks if the type of coin is dollar

        :param num: coin
        :return: true or false
        """
    return type(num) ==Dollar
def isShekel(num):
    """
        checks if the type of coin is shekel

        :param num: coin
        :return: true or false
        """
    return type(num) ==Shekel


def addOperator(num1, num2):
    """
    sums the coins and return the result in shekels

    :param num1: first coin
    :param num2: second coin
    :return: sum of both
    """
    if isDollar(num1):
        a= num1._*rates.get(('dollar', 'nis'))
    if isDollar(num2):
        b = num2._ * rates.get(('dollar', 'nis'))
    if isEuro(num1):
        a = num1._ * rates.get(('euro', 'nis'))
    if isEuro(num2):
        b = num2._ * rates.get(('euro', 'nis'))
    if isShekel(num1):
        a = num1._
    if isShekel(num2):
        b = num2._
    sum=a+b
    return sum

def add(num1,num2):
    """
    sums the coins and prints and return the result in shekels

    :param num1: first coin
    :param num2: second coin
    :return: sum of both
    """
    print(addOperator(num1, num2))
    return addOperator(num1, num2)


def apply(operator_name, x, y):
    """
    chooses the correct function to call for the add\sub action

    :param operator_name: sub or add
    :param x: first parameter
    :param y: second parameter
    :return: a call to athe correct function to add or dub the parameters
    """
    implementations = {('add', ('Dollar', 'Shekel')): AddDollarShekel,
                       ('add',('Dollar', 'Euro')): AddDollarEuro,
                       ('add', ('Euro', 'Shekel')): AddEuroShekel,
                       ('add', ('Euro', 'Dollar')): AddEuroDollar,
                       ('add', ('Shekel', 'Euro')): AddShekelEuro,
                       ('add', ('Shekel', 'Dollar')): AddShekelDollar,
                       ('sub', ('Dollar', 'Shekel')): SubDollarShekel,
                       ('sub', ('Dollar', 'Euro')): SubDollarEuro,
                       ('sub', ('Euro', 'Shekel')): SubEuroShekel,
                       ('sub', ('Euro', 'Dollar')): SubEuroDollar,
                       ('sub', ('Shekel', 'Euro')): SubShekelEuro,
                       ('sub', ('Shekel', 'Dollar')): SubShekelDollar}

    types = (x.NameOfType(), y.NameOfType())
    return type(x)(implementations[(operator_name,(types))](x, y))

def AddDollarShekel(x, y):
    """
    adds the both parameters and return the result in the coin type of the first parameter given

    :param x: first coin
    :param y: second coin
    :return: result of add in the coin type of the first parameter
    """
    print("Dollar(",x._ +y._*rates[('nis', 'dollar')],")")
    return x._ +y._*rates[('nis', 'dollar')]
def AddDollarEuro(x, y):
    """
        adds the both parameters and return the result in the coin type of the first parameter given

        :param x: first coin
        :param y: second coin
        :return: result of add in the coin type of the first parameter
        """
    print("Dollar(",x._ +y._*rates[('euro', 'dollar')],")")
    return x._ +y._*rates[('euro', 'dollar')]
def AddEuroShekel(x, y):
    """
        adds the both parameters and return the result in the coin type of the first parameter given

        :param x: first coin
        :param y: second coin
        :return: result of add in the coin type of the first parameter
        """
    print("Euro(",x._ +y._*rates[('nis','euro')],")")
    return x._ +y._*rates[('nis','euro')]
def AddEuroDollar(x, y):
    """
        adds the both parameters and return the result in the coin type of the first parameter given

        :param x: first coin
        :param y: second coin
        :return: result of add in the coin type of the first parameter
        """
    print("Euro(",x._ +y._*rates[('dollar','euro')],")")
    return x._ +y._*rates[('dollar','euro')]
def AddShekelEuro(x, y):
    """
        adds the both parameters and return the result in the coin type of the first parameter given

        :param x: first coin
        :param y: second coin
        :return: result of add in the coin type of the first parameter
        """
    print("Shekel(",x._ +y._*rates[('euro','nis')],")")
    return x._ +y._*rates[('euro','nis')]
def AddShekelDollar(x, y):
    """
        adds the both parameters and return the result in the coin type of the first parameter given

        :param x: first coin
        :param y: second coin
        :return: result of add in the coin type of the first parameter
        """
    print("Shekel(",x._ +y._*rates[('dollar','nis')],")")
    return x._ +y._*rates[('dollar','nis')]

def SubDollarShekel(x, y):
    """
        subs the both parameters and return the result in the coin type of the first parameter given

        :param x: first coin
        :param y: second coin
        :return: result of sub in the coin type of the first parameter
        """
    print("Dollar(",x._ -y._*rates[('nis', 'dollar')],")")
    return x._ -y._*rates[('nis', 'dollar')]
def SubDollarEuro(x, y):
    """
            subs the both parameters and return the result in the coin type of the first parameter given

            :param x: first coin
            :param y: second coin
            :return: result of sub in the coin type of the first parameter
            """
    print("Dollar(",x._ -y._*rates[('euro', 'dollar')],")")
    return x._ -y._*rates[('euro', 'dollar')]
def SubEuroShekel(x, y):
    """
            subs the both parameters and return the result in the coin type of the first parameter given

            :param x: first coin
            :param y: second coin
            :return: result of sub in the coin type of the first parameter
            """
    print("Euro(",x._ -y._*rates[('nis','euro')],")")
    return x._ -y._*rates[('nis','euro')]
def SubEuroDollar(x, y):
    """
            subs the both parameters and return the result in the coin type of the first parameter given

            :param x: first coin
            :param y: second coin
            :return: result of sub in the coin type of the first parameter
            """
    print("Euro(",x._ -y._*rates[('dollar','euro')],")")
    return x._ -y._*rates[('dollar','euro')]
def SubShekelEuro(x, y):
    """
            subs the both parameters and return the result in the coin type of the first parameter given

            :param x: first coin
            :param y: second coin
            :return: result of sub in the coin type of the first parameter
            """
    print("Shekel(",x._ -y._*rates[('euro','nis')],")")
    return x._ -y._*rates[('euro','nis')]
def SubShekelDollar(x, y):
    """
            subs the both parameters and return the result in the coin type of the first parameter given

            :param x: first coin
            :param y: second coin
            :return: result of sub in the coin type of the first parameter
            """
    print("Shekel(",x._ -y._*rates[('dollar','nis')],")")
    return x._ -y._*rates[('dollar','nis')]

def DollarToShekelDictionary(x):
    """
    converts dollar to shekel and prints it

    :param x: the given coin to convert
    :return: the amount after convert action
    """
    x= x._*rates.get(('dollar', 'nis'))
    print("Shekel(",x,")")
    return x

def EuroToShekelDictionary(x):
    """
        converts euro to shekel and prints it

        :param x: the given coin to convert
        :return: the amount after convert action
        """
    x = x._ * rates.get(('euro', 'nis'))
    print("Shekel(",x, ")")
    return x

def DollarToShekel(x):
    """
        converts dollar to shekel

        :param x: the given coin to convert
        :return: the amount after convert action
        """
    x= x._*rates.get(('dollar', 'nis'))
    return x
def EuroToShekel(x):
    """
        converts euro to shekel

        :param x: the given coin to convert
        :return: the amount after convert action
        """
    x = x._ * rates.get(('euro', 'nis'))
    return x

def coerce_apply(action,x,y):
    """
    converts the dollar\euro to shekel and does an action of add\sub on it

    :param action: add or sub
    :param x: first parameter
    :param y: second parameter
    :return: the amount after the action
    """
    if x.NameOfType()=="Dollar":
        a=DollarToShekel(x)
    if y.NameOfType() == "Dollar":
        b=DollarToShekel(y)
    if x.NameOfType() == "Euro":
        a=EuroToShekel(x)
    if y.NameOfType() == "Euro":
        b=EuroToShekel(y)
    if x.NameOfType() == "Shekel":
        a =x._
    if y.NameOfType() == "Shekel":
        b =y._
    if action == "add":
        print("Shekel(",a+b,")")
        return a+b
    if action=="sub":
        print("Shekel(", a - b, ")")
        return a-b






rates ={('dollar', 'nis'): 3.82,('euro','nis'): 4.07,('euro','dollar'): 1.06}
s = Shekel(50)
if type(s)=="Shekel":
    print("1")
d = Dollar(50)
e = Euro(50)
d.amount()
e.amount()
d + s
add(e, d)
z=eval(repr(d))
print(z)
print(s)
print(e)

rates[('euro','dollar')] = 1.06
apply('add', Shekel(50), Dollar(20))
apply('add', Dollar(50), Euro(20))
apply('sub', Dollar(50), Euro(20))



coercions={('dollar','nis'):DollarToShekelDictionary}
coercions[('dollar','nis')](Dollar(50))
coerce_apply('add', Shekel(50), Dollar(20))
coerce_apply('add', Dollar(50), Euro(20))
coerce_apply('sub', Dollar(50), Euro(20))







