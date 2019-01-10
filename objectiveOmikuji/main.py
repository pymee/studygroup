#!/usr/bin/env python3

NUMBERS_OF_OMIKUJI = 100

def main():
    from OmikujiProperties import OmikujiProperties
    from OmikujiWriter import OmikujiWriter
    from OmikujiBox import OmikujiBox
    from OmikujiFactory import OmikujiFactory

    omikuji_properties = OmikujiProperties()
    omikuji_writer = OmikujiWriter(omikuji_properties)
    omikuji_box = OmikujiBox()

    omkjf = OmikujiFactory(NUMBERS_OF_OMIKUJI, omikuji_writer, omikuji_box)
    omkjb = omkjf.get_omikuji_box()
    for i in range(5):
        omkj = omkjb.get_omikuji()
        print(omkj.get_vars())

if __name__ == '__main__':
    main()
