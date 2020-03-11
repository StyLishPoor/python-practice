def hanoi(numRings,startPeg,endPeg):
    numMoves = 0
    if numRings > 0:
        numMoves += hanoi(numRings-1,startPeg,6-startPeg-endPeg)
        print('Move ring',numRings,'from peg',startPeg,'to peg',endPeg)
        numMoves += 1
        numMoves += hanoi(numRings-1,6-startPeg-endPeg,endPeg)
    return numMoves
print(hanoi(3,1,3))