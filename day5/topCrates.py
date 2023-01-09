
# Python program to read a puzzle input file containing a stack of crates and
# and a bunch of moves to rearrange the crates and computes the final 
# configuration.

# eg. for test input:-
################################
#    [D]                       #
#[N] [C]                       #
#[Z] [M] [P]                   #
# 1   2   3                    #
#                              #
#move 1 from 2 to 1            #
#move 3 from 1 to 3            #
#move 2 from 2 to 1            #
#move 1 from 1 to 2            #
################################

# Note: each crate is moved one at a time.
# The final config is:
##########################
#        [Z]             #
#        [N]             #
#        [D]             #
#[C] [M] [P]             #
# 1   2   3              #
##########################

import re
import cProfile

def getStackConfig(ifile):
    """ Reads a stack configuration from ifile and puts it into a list to 
        return. The topmost crate is an the end of stack list """

    ifile.seek(0)

    stacks = None

    for line in ifile:
        # Initialize `stacks` based on number of stacks in the input.
        # Representing each stack takes 4 chars in each line.
        if stacks == None:
            stacks = [[] for i in range(len(line)//4)]

        i = 1
        for lst in stacks:
            # Upon reaching last line in the stack portion of input, ignore 
            # empty line, rearrange each stack such that topmost crate is moved
            # to the end of the list and return the `stacks`
            if (line[i] == str(i)):
                ifile.readline()
                for stack in stacks:
                    stack.reverse()
                return stacks

            # Get each crate for corresponding stack. " " means no stack there.
            if (line[i] != " "):
                lst.append(line[i])

            # Move index to next crate on the line
            i += 4

def processMoves(ifile, crateStacks:list):
    """ Reads moves from `ifile` and applies thesm onto the `crateStack`
        Warning: seek position of ifile must point to the starting of moves"""
    
    for line in ifile:
        # Extract the numbers from each line
        nums = re.findall(r"\d+", line)
        assert len(nums) == 3
        src = int(nums[1])
        dest = int(nums[2])
        quantity = int(nums[0])

        # Apply the move one crate at a time
        #for x in range(quantity):
        #    crateStacks[dest-1].append(crateStacks[src-1].pop())

        # Apply the move.
        crateStacks[dest-1].extend(crateStacks[src-1][-quantity:])
        del crateStacks[src-1][-quantity:]


if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()

    f = open("puzzleinput.txt", "r")
    crateStacks = getStackConfig(f)
    processMoves(f, crateStacks)

    # Grab the topmost crates and join them 
    print("".join(s[-1] for s in crateStacks))
    
    profiler.disable()
    profiler.print_stats()
