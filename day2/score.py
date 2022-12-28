import sys
import time

# Symbolic Constants
rock = 1
paper = 2
scissor = 3
win = 6
draw = 3
loss = 0
transTable = str.maketrans({"A": f"{rock}", "B": f"{paper}", "C": f"{scissor}",
                            "X": f"{loss}", "Y": f"{draw}", "Z": f"{win}"})

class Rock:
    prev = scissor
    cur = rock
    next = paper


class Paper:
    prev = rock
    cur = paper
    next = scissor


class Scissor:
    prev = paper
    cur = scissor
    next = rock


# create a linked map of rock, paper, scissor
roc = Rock()
pap = Paper()
scis = Scissor()
l_dict = {rock: roc, paper: pap, scissor: scis}

def fast_score(gameResult:int, opponentMove:int):
    oppoMove = l_dict[opponentMove]
    score = gameResult
    if (gameResult == win):
        score += oppoMove.next
    elif (gameResult == draw):
        score += opponentMove
    else:
        score += oppoMove.prev

    return score

def naive_score(gameResult:int, opponentMove:int):
    score = gameResult
    if (gameResult == win):
        if (opponentMove == paper):
            score += 3
        elif (opponentMove == scissor):
            score += 1
        else:
            score += 2
    elif (gameResult == draw):
        score += opponentMove
    else:
        if (opponentMove == paper):
            score += 1
        elif (opponentMove == scissor):
            score += 2
        else:
            score += 3

    return score

# Pre generate scores for all possible moves and return a scoremap
# The move by opponent and the game result will be key to the map
# Eg opponent playing rock(1) and a win(6) for game will be int(16)
def gen_scores():
    scoremap = {}
    for x in range(1,4):
        for y in (0,3,6):
            scoremap[x*10+y] = fast_score(y,x)
    return scoremap

scoremap = gen_scores()

def veryfast_score(gameResult:int, opponentMove:int):
    return scoremap[opponentMove*10+gameResult]

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage : python scriptname InputFilename")
        exit(1)

    stratFile = open(sys.argv[1], "r")
    totalScores = [0] * 3
    naiveTime = 0
    fastTime = 0
    veryFastTime = 0
    count = 0
    for line in stratFile:
        assert (len(line) == 4 and line[1] == " ")
        opponentMove = int(line[0].translate(transTable))
        myMove = int(line[2].translate(transTable))

        # Use fast_score()
        perf = time.perf_counter_ns()
        totalScores[0] += fast_score(myMove, opponentMove)
        fastTime += time.perf_counter_ns() - perf

        # Use naive_score()
        perf = time.perf_counter_ns()
        totalScores[1] += naive_score(myMove, opponentMove)
        naiveTime += time.perf_counter_ns() - perf

        # Use veryfast_score()
        perf = time.perf_counter_ns()
        totalScores[2] += veryfast_score(myMove, opponentMove)
        veryFastTime += time.perf_counter_ns() - perf

        count += 1

    print(f"(fast_score({totalScores[0]}) - {count} calculations in {fastTime/1000000} ms...)")
    print(f"(veryfast_score({totalScores[2]}) - {count} calculations in {veryFastTime/1000000} ms...)")
    print(f"(naive_score({totalScores[1]}) - {count} calculations in {naiveTime/1000000} ms...)")


