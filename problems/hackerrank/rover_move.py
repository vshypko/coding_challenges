def roverMove(matrixSize, cmds):
    if matrixSize <= 0:
        return

    row, column = 0, 0
    current_position = (row * matrixSize) + column

    # Update either row or column (based on the command) and
    # current_position handling edges correctly.
    for cmd in cmds:
        if cmd == "UP":
            row = (row - 1) if (row > 0) else 0
        elif cmd == "DOWN":
            row = (row + 1) if (row < matrixSize - 1) else (matrixSize - 1)
        elif cmd == "RIGHT":
            column = (column + 1) if (column < matrixSize - 1) else (matrixSize - 1)
        elif cmd == "LEFT":
            column = (column - 1) if (column > 0) else 0
        current_position = (row * matrixSize) + column

    return current_position


actions = list()
actions.append("RIGHT")
actions.append("RIGHT")
actions.append("RIGHT")
actions.append("RIGHT")
actions.append("RIGHT")
actions.append("RIGHT")
actions.append("RIGHT")
actions.append("RIGHT")
actions.append("RIGHT")
print(roverMove(4, actions))
