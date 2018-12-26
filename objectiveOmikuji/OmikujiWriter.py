from OmikujiProperties import OmikujiProperties
from Omikuji import Omikuji

import random


class OmikujiWriter:

    def __init__(self, omikuji_properties):
        self.omikuji_properties = omikuji_properties
        self.omikuji_object_list = []
        self._make_omikuji_object(self.omikuji_properties.get_omikuji_raw_data())

    def _make_omikuji_object(self, omikuji_raw_data):
        for fortune, detail in omikuji_raw_data.items():
            omikuji_obj = Omikuji()
            setattr(omikuji_obj, "index", fortune)
            for key, value in detail.items():
                t = type(value)
                if t is str or t is int:
                    setattr(omikuji_obj, key, value)
                elif type(value) is dict:
                    for k, v in value.items():
                        if type(v) is str:
                            fortune_name = v
                        if type(v) is list:
                            fortune_contents = random.choice(v)
                    setattr(omikuji_obj, key, fortune_name + "," + fortune_contents)
            self.omikuji_object_list.append(omikuji_obj)

    def get_omikuji_object_list(self):
        # self.make_omikuji_object(omikuji_raw_data)
        return self.omikuji_object_list


if __name__ == "__main__":
    omkjp = OmikujiProperties()
    omkjw = OmikujiWriter(omkjp)

    for omkj in omkjw.get_omikuji_object_list():
        print(vars(omkj))

