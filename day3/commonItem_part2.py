import sys

def common(*strs):
    """ Returns a list of chars common to arguments """
    c_set = set(strs[0])
    for s in strs:
        c_set &= set(s)
    return list(c_set)

def priority(item:str):
    return ((ord(item)-38) if item.isupper() else (ord(item)-96))

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage : python scriptname InputFilename")
        exit(1)
        
    i_file = open(sys.argv[1], "r")

    p_sum = 0
    lines = i_file.readlines()
    i = 0
    while (i < len(lines)):
        p_sum += priority(common(lines[i].strip(), lines[i+1].strip(), 
                                 lines[i+2].strip())[0])
        i += 3
    print(p_sum)

