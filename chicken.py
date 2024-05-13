class chicken:
    def __init__(self, is_it_a_boy,height,weight,egg_count):
        self.is_it_a_boy = is_it_a_boy
        self.height = height
        self.weight = weight
        self.egg_count = egg_count


    def is_it_a_boy(self):
        if (self.is_it_a_boy) == True:
            print("He is a boy!")
        else:
            print("He is a girl")
    def check_weight(self):
        print(self.weight)
    def check_height(self):
        print(self.height)

    egg_counter = 0
    def eat(self):
        print("om nom")
        self.weight += 100
        self.height += 5

    def lay_egg(self):
        print("bop")
        self.weight -= 2
        self.egg_count += 1
        print( self.egg_count)
        if self.weight <= 0:
            print("oop he's dead")