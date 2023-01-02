import sys

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: python scriptname inputFilename")
        exit(1)

    i_file = open(sys.argv[1], "r")

    intersects = 0
    subsets = 0

    for line in i_file:
        ranges = list(list(map(int, s.split("-"))) for s in line.strip().split(","))
        for r in ranges:
            r[1] += 1
        sets = list({x for x in range(*r)} for r in ranges) 
        if (sets[0] & sets[1]):
            intersects += 1
        if (sets[0].issuperset(sets[1]) or sets[0].issubset(sets[1])):
            subsets += 1
    
    print(f"Overlaps: {intersects}\n"
          f"Supersets: {subsets}")
