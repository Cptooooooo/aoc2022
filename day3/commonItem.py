import sys
import time

def common(str1:str, str2:str):
    """ Returns a set of chars common to str1 and str2"""
    com_str = ""
    for char1 in str1:
        for char2 in str2:
            if (char1 == char2):
                com_str += char1
                break
    return list(set(com_str))

def priority(item:str):
    return ((ord(item)-38) if item.isupper() else (ord(item)-96))

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage : python scriptname InputFilename")
        exit(1)
        
    i_file = open(sys.argv[1], "r")
    
    # Some benchmarking
    perf_time = 0
    count = 0
    
    # 1
    commonItems = []
    for line in i_file:
        perf = time.perf_counter_ns()
        l_len = len(line) - 1 # exclude '\n'
        assert (l_len%2 == 0)
        commonItems.extend(common(line[:(l_len//2)], line[(l_len//2):l_len]))
        perf_time += time.perf_counter_ns() - perf
        count += 1
       
    perf = time.perf_counter_ns()
    p_sum = sum(map(priority, commonItems))
    perf_time += time.perf_counter_ns() - perf

    print("#1\n", p_sum)
    print(f"{count} lines processed in {perf_time/1000000} ms")

    i_file.seek(0)
    perf_time = 0
    count = 0

    # 2
    p_sum = 0
    for line in i_file:
        perf = time.perf_counter_ns()
        l_len = len(line) - 1 # exclude '\n'
        assert (l_len%2 == 0)
        for item in common(line[:(l_len//2)], line[(l_len//2):l_len]):
            p_sum += priority(item)
        perf_time += time.perf_counter_ns() - perf
        count += 1


    print("#2\n", p_sum)
    print(f"{count} lines processed in {perf_time/1000000} ms")
