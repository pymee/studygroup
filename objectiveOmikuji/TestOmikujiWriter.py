import unittest
from OmikujiWriter import OmikujiWriter
from OmikujiProperties import OmikujiProperties


class TestOmikujiWriter(unittest.TestCase):

    def test_get_omikuji_list(self):
        expect = {'key': 'daikichi', 'name': '大吉', 'rate': 5, 'kinun': '金運,詳細1', 'tenkyoun': '旅行運,詳細3',
                  'shigotoun': '仕事運,詳細5'}

        omkjp = OmikujiProperties("./TestOmikujiData.yaml")
        omkjw = OmikujiWriter(omkjp)

        self.assertDictEqual(vars(omkjw.get_omikuji_list()[0]), expect)


if __name__ == '__main__':
    unittest.main()
