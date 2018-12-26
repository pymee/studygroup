from OmikujiProperties import OmikujiProperties
from OmikujiWriter import OmikujiWriter
from OmikujiBox import OmikujiBox

import copy


class OmikujiFactory:

    def __init__(self, number_of_omikuji):
        omikuji_properties = OmikujiProperties()
        omikuji_writer = OmikujiWriter(omikuji_properties)
        self.omikuji_box = OmikujiBox()
        self._make_omikuji_box(number_of_omikuji, omikuji_writer.get_omikuji_object_list())

    def _make_omikuji_box(self, number, omikuji_object_list):
        for omikuji_obj in omikuji_object_list:
            count = int(omikuji_obj.get_rate() / 100 * number)
            for i in range(count):
                self.omikuji_box.set_omikuji(copy.copy(omikuji_obj))

    def get_omikuji_box(self):
        return self.omikuji_box


if __name__ == '__main__':
    NUMBERS_OF_OMIKUJI = 100
    omkjf = OmikujiFactory(NUMBERS_OF_OMIKUJI)
    omkjb = omkjf.get_omikuji_box()
    for i in range(20):
        omkj = omkjb.get_omikuji()
        print(omkj.get_vars())
