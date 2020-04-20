
import itertools


class idTooShort(Exception):
    pass


def check_id(id):
    
    """
    checks ID validation
    

    Parameters
    ----------
    ID : int/string , must .
        DESCRIPTION: ID number or string format, for validation check
        
    Returns
    -------
    TYPE: bool
        DESCRIPTION: ID valid?: True or False
    
    """
    
    # removing leading zeros
    id = str(id)
    while id[0] == '0':
        id = id[1:]
        
    # input length validation
    try:
        if len(id) != 9:
            raise idTooShort(id)
    except idTooShort:
        print("ID length must be 9 characters exclude leading zeros")
    
    #The check 
    else:
        x = [int(id[i])*2 if i%2==1 else int(id[i]) for i in range(len(str(id)))]  #return ints
        y = [i if i<10 else int(str(i)[0]) + int(str(i)[1]) for i in x]    #ints
        return sum(y)%10 == 0

 

class IDIterator:
    
    """
    creates a valid ID's iterator
    

    Parameters
    ----------
    start : int, optional.
        DESCRIPTION: The default is 100000000.
        the id given starts the ID counting

    Returns
    -------
    TYPE: int
        DESCRIPTION: valid ID by calling 'print next'
    """
    
    # initialize start ID
    def __init__(self,id=100000000):
        self.id = id
        
    # creating iterator
    def __iter__(self):
        return self
    
    # returning next
    def __next__(self):  
        # stop condition - Max 9 digits int. 
        if self.id >= 999999999 :
            raise StopIteration()
        
        # if ID not valid, increment ID until it does.
        while not check_id(self.id):
            self.id += 1
        
        # increment by 1 for the next call(avoid duplicate)
        self.id+=1
        
        #return the valid ID
        return self.id-1
        



def IDGenerator(start=123456780):
    
    """
    creates a valid ID's generator
    

    Parameters
    ----------
    start : int, optional.
        DESCRIPTION: The default is 123456780.
        the id given starts the counting

    Returns
    -------
    TYPE: int
        DESCRIPTION: valid ID by calling 'print next'
    """
    
    return (i for i in itertools.count(start) if check_id(i))


def main():
    
    """
    creates  IDGenerator /IDIterator instances
    prints 10 ID's from each.
    

    Parameters
    ----------
    none.
        the method only prints.
        no values expected.
            
    Returns
    -------
    TYPE: nonType
        DESCRIPTION: prints 20 valid ID's
    """
    
    # initialize iterator as z
    z = IDIterator(123456780)

    # print 10 first valid ID's from iterator
    for i in range(10):
        print(next(z))
    
    # initialize generator as s
    s = IDGenerator()
    
    # print 10 first valid ID's ffrom generator
    for i in range(10):
        print(next(s))