import random
class panda:
    def __init__(self, is_it_a_boy,height,weight):
        self.is_it_a_boy = is_it_a_boy
        self.height = height
        self.weight = weight

    def is_it_a_boy(self):
        if self.is_it_a_boy == True:
            print("He is a boy!")
        elif self.is_it_a_boy == False:
            print("He is a girl")
    def check_weight(self):
        print(self.weight)
    def check_height(self):
        print(self.height)

    def eat(self):
        print("om nom")
        self.weight += 100
        self.height += 5

    def extinct(self):
        if random.randint(1, 10) < 3:
            print("all pandas went extinct")
        else:
            print("they're ok for now")