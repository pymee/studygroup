import yaml

OMIKUJI_DATA = './OmikujiData.yaml'


class OmikujiPropertiesFromYaml:

    def __init__(self):
        self.omikuji = {}
        self.load_omikuji()

    def load_omikuji(self):
        with open(OMIKUJI_DATA, 'r') as f:
            self.omikuji = yaml.load(f)

    def get_omikuji_raw_data(self):
        return self.omikuji


if __name__ == '__main__':
    omkj = OmikujiPropertiesFromYaml()
    print(omkj.get_omikuji_raw_data())
