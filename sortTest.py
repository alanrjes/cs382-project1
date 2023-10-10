import argparse #documentation: https://docs.python.org/3/library/argparse.html
import time
import random
import time
import csv
import copy

from quickSort import quick_sort
from mergeSort import merge_sort
from insertionSort import insertion_sort

# define positional arguments
parser = argparse.ArgumentParser()
parser.add_argument('sizeMin', type=int, help="Minimum input size to test")
parser.add_argument('sizeIncr', type=int, help="Increment for input size")
parser.add_argument('sizeMax', type=int, help="Maximum input size to test")
parser.add_argument('numTrials', type=int, help="Number of trials for each input size")

# define optional arguments
parser.add_argument('--whichsorts', '-w',
                    choices=["quicksort", "mergesort", "insertionsort"],
                    nargs='+',
                    type=str.lower,
                    default=["quicksort", "mergesort", "insertionsort"],
                    help="One or more sorts to test. Default is to test all sorts."
                    )

parser.add_argument('--generator', '-g',
                    choices=["random", "ordered", "evil"],
                    type=str.lower,
                    default = "random",
                    help="Specifies the input generator to use. Default is random."
                    )

parser.add_argument('--save', '-s',
                    type=str.lower,
                    help="Provide a filename to save the output as a .csv file."
                    )

# parse command line arguments based on definitions
args = parser.parse_args()

def sequence_generator(gen, k):
    if (gen == "evil"):
        return list(range(k, 0, -1))
    elif (gen == "ordered"):
        return list(range(0, k))
    else:
        sequence = []
        random.seed()
        while (len(sequence) < k):
            sequence.append(random.randint(0, k-1))
        return sequence

def analyze_runtime(fun, seq):
    start = time.time()
    fun(seq)
    return time.time() - start

# results summary as an array/table for outputting
results = [["N"] + args.whichsorts]

k = args.sizeMin
while (k <= args.sizeMax):
    runtimeResults = {key: 0 for key in args.whichsorts}
    for i in range(args.numTrials):
        sequence = sequence_generator(args.generator, k)

        if ("quicksort" in args.whichsorts):
            runtimeResults["quicksort"] +=  analyze_runtime(quick_sort, copy.deepcopy(sequence))
        if ("mergesort" in args.whichsorts):
            runtimeResults["mergesort"] += analyze_runtime(merge_sort, copy.deepcopy(sequence))
        if ("insertionsort" in args.whichsorts):
            runtimeResults["insertionsort"] += analyze_runtime(insertion_sort, sequence)

    # add avg for this trial size to output summary
    resultK = [str(k)]
    for key in runtimeResults:
        avg = round(runtimeResults[key]/args.numTrials, 12)
        resultK.append(str(avg))
    results.append(resultK)

    k += args.sizeIncr

if (args.save):
    with open(args.save+'.csv', 'w') as f:
        writer = csv.writer(f)
        for row in results:
            writer.writerow(row)

# print summary nicely
printstr = ""
for row in results:
    for i in range(len(row)):
        item = row[i]
        printstr += item + ","
        if (i==0):
            printstr += " "*(6-len(item))
        elif (i!=len(row)-1):
            printstr += " "*(18-len(item))
    printstr += "\n"
print(printstr)
