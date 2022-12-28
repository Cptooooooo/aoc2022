import sys

class Elf:
    """A class to represent an Elf and its inventory"""
    __calsPerItem = []
    __totalCals:float

    def __init__(self, calsPerItem:list):
        self.__totalCals = 0.0
        for cal in calsPerItem:
            assert (cal >= 0)
            self.__calsPerItem.append(cal)
            self.__totalCals += cal

    def getCalForItem(self, index:int):
        """Returns calories for item at 'index' in the ELf's inventory"""
        return self.__calsPerItem[index]

    def getTotalCalories(self):
        """Returns the total calories an ELf is carrying"""
        return self.__totalCals


def readElfFile(filename:str):
    """Reads an elf file and returns a list of Elf objects"""
    elfFile = open(filename, "r")
    elfs = []
    calsPerElf = []
    for line in elfFile:
        if (line.strip() == ""):
            elfs.append(Elf(calsPerElf))
            calsPerElf.clear()
        else:
            calsPerElf.append(float(line))

    elfFile.close()
    return elfs


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage : python scriptname elfInputFilename")
        exit(1)

    elfs = readElfFile(sys.argv[1])
    # Instead of sorting the list, I just iterated over it 3 times to get top 3 values
    top3_cals = [float("-inf")] * 3
    for i in range(len(top3_cals)):
        larger_val = float("inf") if (i==0) else top3_cals[(i-1)]
        for elf in elfs:
            if (elf.getTotalCalories() > top3_cals[i] and elf.getTotalCalories() < larger_val):
                top3_cals[i] = elf.getTotalCalories()
    print(sum(top3_cals))
