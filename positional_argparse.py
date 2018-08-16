import argparse


def sum(x, y):
    return x + y


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-int1',
                        help='integer1 to be added',
                        type=int)
    parser.add_argument('-int2',
                        help='integer2 to be added',
                        type = int)
    
    args = parser.parse_args()
    
    sum(integer1, integer2)

