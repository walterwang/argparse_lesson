import argparse

parser = argparse.ArgumentParser()

parser.add_argument('print_string',
                    help='string to print')
args = parser.parse_args()

print(args.print_string)
