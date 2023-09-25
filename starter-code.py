import argparse #documentation: https://docs.python.org/3/library/argparse.html
import time

# define positional arguments
parser = argparse.ArgumentParser()
parser.add_argument('sizeMin', type=int, help="Minimum input size to test")
parser.add_argument('sizeIncr', type=int, help="Increment for input size")
parser.add_argument('sizeMax', type=int, help="Maximum input size to test")
parser.add_argument('numTrials', type=int, help="Number of trials for each input size")

# define optional arguments
parser.add_argument('--whichsorts', '-w',
                    nargs='+',
                    type=str,
                    help="One or more sorts to test. Default is to test all sorts."
                    )

parser.add_argument('--generator', '-g',
                    choices=["random", "ordered", "evil"],
                    default = "random",
                    help="Specifies the input generator to use. Default is random."
                    )

# parse command line arguments based on definitions
args = parser.parse_args()
print(args.whichsorts)
print(args.generator)
# your code here

