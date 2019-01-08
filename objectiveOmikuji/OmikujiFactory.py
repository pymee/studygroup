import copy


class OmikujiFactory:

    def __init__(self, number_of_omikuji, omikuji_writer_obj, omikuji_box_obj):
        self.omikuji_box = omikuji_box_obj
        self._make_omikuji_box(number_of_omikuji, omikuji_writer_obj.get_omikuji_object_list())

    def _make_omikuji_box(self, number, omikuji_object_list):
        for omikuji_obj in omikuji_object_list:
            count = int(omikuji_obj.get_rate() / 100 * number)
            for i in range(count):
                self.omikuji_box.set_omikuji(copy.copy(omikuji_obj))

    def get_omikuji_box(self):
        return self.omikuji_box
