import yaml


class OmikujiPropertiesFromYaml:

    def __init__(self, filename):
        self.filename = filename
        self.omikuji_raw_data = {}
        self.load_omikuji()

    def load_omikuji(self):
        with open(self.filename, 'r') as f:
            self.omikuji_raw_data = yaml.load(f)

    def get_omikuji_raw_data(self):
        return self.omikuji_raw_data


if __name__ == '__main__':
    OMIKUJI_DATA = './OmikujiData.yaml'
    omkj = OmikujiPropertiesFromYaml(OMIKUJI_DATA)
    print(omkj.get_omikuji_raw_data())
