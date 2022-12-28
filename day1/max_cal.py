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
    max_cals = elfs[0].getTotalCalories()
    for elf in elfs:
        if (elf.getTotalCalories() > max_cals):
            max_cals = elf.getTotalCalories()
    print(max_cals)
