
class blueWhale:
    def __init__(self, is_it_a_boy,height,weight):
        self.is_it_a_boy = is_it_a_boy
        self.height = height
        self.weight = weight

    def check_weight(self):
        return self.weight
    def check_height(self):
        return self.height

    def eat(self):
        print("om nom")
        self.weight += 100
        self.height += 5

    def make_noise(self):
        print("w0000000o0ooooooooooooooooo0oooooooooooo000")

    def poop(self):
        print("<poop noise>")
        self.weight -= 25
        if self.weight >= 50:
            print("poop noise")
            self.weight -= 25

        else:
            print("oops! the whale died")
            self.weight -= 0