import unittest
from OmikujiWriter import OmikujiWriter
from OmikujiProperties import OmikujiProperties
from Omikuji import Omikuji


class TestOmikujiWriter(unittest.TestCase):

    def setUp(self):
        self.omkjp = OmikujiProperties("./TestOmikujiData.yaml")
        self.omkjw = OmikujiWriter(self.omkjp)
        self.omikuji_objects = self.omkjw.get_omikuji_object_list()

    def test_get_omikuji_list(self):
        expect = {'index': 'daikichi', 'name': '大吉', 'rate': 5, 'kinun': '金運,詳細1', 'tenkyoun': '旅行運,詳細3',
                  'shigotoun': '仕事運,詳細5'}

        self.assertDictEqual(vars(self.omikuji_objects[0]), expect)

    def test_get_rate(self):
        self.assertEqual(self.omikuji_objects[0].get_rate(), 5)


if __name__ == '__main__':
    unittest.main()
