import sys
import time

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: python scriptname inputFilename")
        exit(1)

    i_file = open(sys.argv[1], "r")

    intersects = 0
    subsets = 0
    supersets = 0

    time1 = 0
    time2 = 0

    for line in i_file:
        ranges = list(list(map(int, s.split("-"))) for s in line.strip().split(","))
        for r in ranges:
            r[1] += 1
        sets = list({x for x in range(*r)} for r in ranges) 
        if (sets[0] & sets[1]):
            intersects += 1

        # 1
        perf = time.perf_counter_ns()
        if (sets[0].issuperset(sets[1]) or sets[0].issubset(sets[1])):
            subsets += 1
        time1 += time.perf_counter_ns() - perf

        #2
        perf = time.perf_counter_ns()
        if (sets[0].issubset(sets[1]) if (len(sets[0])<len(sets[1])) 
            else sets[1].issubset(sets[0])):
            supersets += 1
        time2 += time.perf_counter_ns() - perf
    
    print(f"Overlaps: {intersects}\n"
          f"Supersets: ({subsets}/{supersets}) | #1 {time1/1000000} ms | #2 {time2/1000000} ms")
