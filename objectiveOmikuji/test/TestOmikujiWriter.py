import unittest
from OmikujiWriter import OmikujiWriter
from OmikujiProperties import OmikujiProperties
from Omikuji import Omikuji


class TestOmikujiWriter(unittest.TestCase):

    def setUp(self):
        self.omkjp = OmikujiProperties()
        self.omkjw = OmikujiWriter(self.omkjp)
        self.omikuji_objects = self.omkjw.get_omikuji_object_list()

    def test_get_omikuji_list(self,filename='./TestOmikujiData.yaml'):
        expect = {'index': 'daikichi', 'name': '大吉', 'rate': 5, 'kinun': '金運,持ち主不明の2億円を拾う', 'tenkyoun': '旅行運,ステキな出会いがある',
                  'shigotoun': '仕事運,他人の手柄で評価アップ'}

        self.assertDictEqual(vars(self.omikuji_objects[0]), expect)

    def test_get_rate(self):
        self.assertEqual(self.omikuji_objects[0].get_rate(), 5)


if __name__ == '__main__':
    unittest.main()
