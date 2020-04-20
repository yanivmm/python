#####summering excercise 2.5



class Animal:
    """
    The main class of our code: 'animal'
    """
    zoo_name = "Hayaton"
    
    def __init__(self,name,hunger=0):
        """a Boot function to the animal's values
        """
        self.name = name
        self.hunger = hunger

    def get_name(self):
        """returns the name of the specific animal
        rType- string
        """
        print(self.name)
    
    def is_hungry(self):
        """ cheks if the anumal is hungry(hunger greater than 0)
        rType-Boolean
        """
        print(self.hunger>0)
        
    def feed(self):
        """ feeds the animal(hunger level is down by 1)
        returns nothing
        """
        self.hunger-=1
        
    def talk(self):
        """super class of each animal's sound
        the specific sound  will be written in the subclasses"""
        pass
    



class Dog(Animal):
    def __init__(self, name,hunger):
        Animal.__init__(self, name,hunger)
    
    def talk(self):
        super().talk()
        print("Waff waff")
        
    def fetch_stick(self):
        print("There you go, sir!")
        
        
class Cat(Animal):
    def __init__(self, name,hunger):
        Animal.__init__(self, name,hunger)
    
    def talk(self):
        super().talk()
        print("meow")
    
    def chase_laser(self):
        print("Meeeeow")

        
class Skunk(Animal):
    def __init__(self, name,hunger,stink_count=6):
        Animal.__init__(self, name,hunger)
        self.stink_count = stink_count
        
    def talk(self):
        super().talk()
        print("tssss")        
    
    def stink(self):
        print("Dear lord!")

        
class Unicorn(Animal):
    def __init__(self, name,hunger):
        Animal.__init__(self, name,hunger)
    
    def talk(self):
        super().talk()
        print("good day darling")
            
    def sing(self):
        print("I’m not your toy...")
        
        
class Dragon(Animal):
    def __init__(self,name,hunger,color="green"):
        Animal.__init__(self, name,hunger)
        self.color = color
        
    def talk(self):
        super().talk()
        print("raaaaawr")
    
    def breath_fire(self):
        print("$@#$#@$")
        
    
    
def main():
    """The main function 
    adding list of animals to zoo_lst variable,feeds and print alues
    """
    #adding animals to zoo_lst
    zoo_lst=[]
    zoo_lst.append(Dog("Brownie", 10))
    zoo_lst.append(Cat('Zelda',3))
    zoo_lst.append(Skunk('Stinky',0))
    zoo_lst.append(Unicorn('Keith',7))
    zoo_lst.append(Dragon('Lizzy',1450))
    zoo_lst.append(Dog("Doggo", 80))
    zoo_lst.append(Cat('Kitty',80))
    zoo_lst.append(Skunk('Stinky jr.',80))
    zoo_lst.append(Unicorn('Clair',80))
    zoo_lst.append(Dragon('Mc. fly',80))
    
    #feeds the animals and prints the following values: name,sound,specific function ogf the animal.
    for animal in zoo_lst:
        while animal.hunger>0:
            animal.feed()
        animal.get_name()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
            print(animal.stink_count)
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()
            print(animal.color)
    print(animal.zoo_name)
   
    
#calling the main method
main()
