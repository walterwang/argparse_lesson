import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-t', '--takeoff', action='store_true')
    group.add_argument('-l', '--landing', action='store_true')

    args=parser.parse_args()
    if args.takeoff:
        print('The plane is taking off')
    elif args.landing:
        print('The plane is landing')
    else:
        print('The plane is neither landing or taking off')
        
