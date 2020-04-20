####  תכניות מונחה עצמים######

class animal:
    def __init__(self,age=0,name='octavio'):
         self.name = name
         self.age = age
         
    def birthday(self):
         self.age+=1
         
    def get_age(self):
        print("i'm " ,self.age,"years old")
        
    def set_name(self,name):
        self.name=name
    
    def get_name(self):
        print("i'm ",self.name)
        
        
def main2():
    dogy = animal(3,'fluppy')
    dogy.birthday()
    dogy.birthday()
    dogy.get_age()
    dogy.get_name()
    dogy.set_name('chuch')
    dogy.get_name()
    
main2()


########  pixel excersize  ########



class pixel:

    def __init__(self,x=0,y=0,red=0,green=0,blue=0):
        self.x = x
        self.y = y
        self.red  = red
        self.green= green
        self.blue = blue

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        
    def set_grayscale(self):
        grayscale = (self.red+self.green+self.blue)//3 
        self.red  = grayscale
        self.green= grayscale
        self.blue = grayscale

           
    def print_pixel_info(self):
        color = (self.red,self.green,self.blue)
        print("X:",self.x," Y:", self.y," Color:",color,end=' ')  
        
        if color.count(0)==2:
            y=list(color[:])
            y.remove(0)
            y.remove(0)
            only_color = ["red","green","blue"][color.index(y[0])]
            print(only_color)
    


def main():
    pixi = pixel(5,6,250)
    pixi.print_pixel_info()
    pixi.set_grayscale()
    pixi.print_pixel_info()
main()












