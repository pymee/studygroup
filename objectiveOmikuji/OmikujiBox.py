import random


class OmikujiBox:
    def __init__(self):
        self.omikuji_object_list = []

    def get_omikuji(self):
        return random.choice(self.omikuji_object_list)

    def set_omikuji(self, omikuji_obj):
        self.omikuji_object_list.append(omikuji_obj)
