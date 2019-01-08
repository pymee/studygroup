import yaml


class OmikujiPropertiesFromYaml:
    DEFAULT_OMIKUJI_FILE = './OmikujiData.yaml'

    def __init__(self):
        pass

    def get_omikuji_raw_data(self, filename=DEFAULT_OMIKUJI_FILE):
        with open(filename, 'r') as f:
           omikuji_raw_data = yaml.load(f)
        return omikuji_raw_data


if __name__ == '__main__':
    omkj = OmikujiPropertiesFromYaml()
    print(omkj.get_omikuji_raw_data())
