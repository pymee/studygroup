from argparse import ArgumentParser
import os


def parser():
    # argparseのArgumentParserを使って引数が足りるかの判定してみた。
    usage = "{} <csv_filename>".format(os.path.basename(__file__))
    argparser = ArgumentParser(usage=usage)
    argparser.add_argument("csv_file", type=str, help="csv_filename")

    return argparser.parse_args()


if __name__ == "__main__":
    args = parser()
    print(args.csv_file)
