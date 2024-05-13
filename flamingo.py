class flamingo:
    def __init__(self, is_it_a_boy,height,weight,pink_ratio):
        self.is_it_a_boy = is_it_a_boy
        self.height = height
        self.weight = weight
        self.pink_ratio = pink_ratio

    def is_it_a_boy(self):
        if (self.is_it_a_boy) == True:
            print("He is a boy!")
        else:
            print("He is a girl")
    def check_weight(self):
        print(self.weight)
    def check_height(self):
        print(self.height)

    def eat(self):
        print("om nom")
        self.weight += 100
        self.height += 5
        self.pink_ratio += 1
        print(self.pink_ratio)


