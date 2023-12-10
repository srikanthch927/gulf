import argparse

parser=argparse.ArgumentParser(description="process data")

parser.add_argument('--startdate',type=str,help='startingdate')
parser.add_argument('--enddate',type=str,help='endingdate')


args=parser.parse_args()

print(args)