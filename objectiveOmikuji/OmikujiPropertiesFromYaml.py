import yaml


class OmikujiPropertiesFromYaml:

    def __init__(self):
        self.omikuji_raw_data = {}
        self.load_omikuji()

    def load_omikuji(self):
        filename = './OmikujiData.yaml'
        with open(filename, 'r') as f:
            self.omikuji_raw_data = yaml.load(f)

    def get_omikuji_raw_data(self):
        return self.omikuji_raw_data


if __name__ == '__main__':
    omkj = OmikujiPropertiesFromYaml()
    print(omkj.get_omikuji_raw_data())
