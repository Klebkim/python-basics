class Jamie:

    def __init__(self, is_it_a_boy, height, weight):
        self.is_it_a_boy = is_it_a_boy
        self.height = height
        self.weight = weight

    def check_if_tall_enough_to_ride_roller_coaster(self):
        # minimum heighht is 72 inches
        if self.height >= 72:
            return True

        else: return False
    def check_if_light_enough_for_ifly(self):
        if self.weight <= 300:
            return True
        else: return False
