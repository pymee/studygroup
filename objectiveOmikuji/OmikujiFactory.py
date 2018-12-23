from OmikujiProperties import OmikujiProperties
from OmikujiWriter import OmikujiWriter


class OmikujiFactory:

    def __init__(self, omikuji_properties):
        self.omikuji_writer = OmikujiWriter(omikuji_properties)
        self.omikuji_box = []

    def get_omikuji_box(self):
        for omikuji in self.omikuji_writer.get_omikuji_list():
            self.omikuji_box.append(omikuji)
        return self.omikuji_box


if __name__ == '__main__':
    omkjp = OmikujiProperties()
    omkjf = OmikujiFactory(omkjp)

    for i in omkjf.get_omikuji_box():
        print(vars(i))
