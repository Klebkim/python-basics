class Lizard:

    def __init__(self, am_i_a_boy):
        self.am_i_a_boy = am_i_a_boy
    def make_noise(self):
        if self.am_i_a_boy:
            print("PSSSSST PSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSST *INAUDIBLE*")
        else:
            print("p.s.t")

    def eat(self):
        if self.am_i_a_boy:
            print("I LOVE FOOD I LOVE FOOD I LOVE FOOD I LOVE FOOD I LOVE FOOD I LOVE FOOD I LOVE FOOD I LOVE FOOD FOOOOOOOOOOOOOOOOOOOOOOD")
        else:
            print("whats food")

    def poop(self):
        if self.am_i_a_boy:
            print("PRFFFFFFFT")
        else:
            print("doink")

    def sleep(self):
        if self.am_i_a_boy:
            print('*EARTHQUAKE THAT CAUSED THE MASS EXTINCTION FOR DINOSAURS* ')
        else:
            print("z")