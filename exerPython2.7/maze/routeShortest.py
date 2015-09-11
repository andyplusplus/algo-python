"""
Implemented based on Java Implementation: ShortestPathInMaze.java
"""

from collections import deque

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def getNextCells(self):
        arr = []
        i, j = self.row, self.col
        arr.append(Cell(i+1, j))
        arr.append(Cell(i, j+1))
        arr.append(Cell(i-1, j))
        arr.append(Cell(i, j-1))
        return arr

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __str__(self):
        return "(" + str(self.row) + "," + str(self.col) + ")"



NOT_PASSABLE = -1
WALL_CHAR = "#"
FOOT_CHAR = "."
class Maze:
    def __init__(self, maze):
        self.maze = maze


    def __createLevelMatrix(self):
        rows = len(self.maze)
        cols = len(self.maze[0])
        matrix = []
        for i in range(rows):
            ra = []
            for j in range(cols):
                ra.append(0)
            matrix.append(ra)

        for i in range(rows):
            for j in range(cols):
                if self.maze[i][j] == WALL_CHAR:
                    matrix[i][j] = -1
        return matrix

    def __isCellNotPassable(self, matrix, cell):
        if cell.row < len(matrix) and cell.col < len(matrix[cell.row]):
            return matrix[cell.row][cell.col] == NOT_PASSABLE
        return True

    def __markLevels(self, matrix, start, end):
        pass

    def find_shortest_path(self):
        matrix = self.__createLevelMatrix()
        start = self.__find_start()
        end = self.__find_end()

        print("solving...")

        queue = deque()
        queue.append(start)

        #///////////////////////////////////////////////////
        #     set start row, col
        #     marked a path from 1 to n
        #///////////////////////////////////////////////////
        matrix[start.row][start.col] = 1
        while len(queue) != 0:            #cell = queue[0]
            cell = queue.popleft()
            if cell == end:
                break
            level = matrix[cell.row][cell.col]
            nextCells = cell.getNextCells()
            for nextCell1 in nextCells:
                if self.__isCellNotPassable(matrix, nextCell1):
                    continue
                if matrix[nextCell1.row][nextCell1.col] == 0:
                    queue.append(nextCell1)
                    matrix[nextCell1.row][nextCell1.col] = level + 1

        #///////////////////////////////////////////////////////////
        # put the path into queue
        #///////////////////////////////////////////////////////////
        if(matrix[end.row][end.col] == 0):
            return None

        path = deque()
        cell = end
        while not cell == start:
            path.appendleft(cell)
            level = matrix[cell.row][cell.col]
            nextCells = cell.getNextCells()
            for nextCell2 in nextCells:
                if self.__isCellNotPassable(matrix, nextCell2):
                    continue
                if matrix[nextCell2.row][nextCell2.col] == level -1:
                    cell = nextCell2
                    break
        return path

    def __find_start(self):
        for y,line in enumerate(self.maze):
            try:
                x = line.index("S")
                return Cell(y, x)
            except ValueError:
                pass

    def __find_end(self):
        for y,line in enumerate(self.maze):
            try:
                x = line.index("E")
                return Cell(y, x)
            except ValueError:
                pass

    def print_mazeWithPath(self, path):
        path.pop()
        for cell in path:
            self.maze[cell.row][cell.col] = "."
        print(self)

    def __str__(self):
        return "\n".join(''.join(line) for line in self.maze)

    @classmethod
    def print_path(cls, path):
        print(",".join(str(cell) for cell in path))

    @classmethod
    def load_maze(cls, fname):
        with open(fname) as inf:
            lines = (line.rstrip("\r\n") for line in inf)
            maze  = [list(line) for line in lines]
        return cls(maze)

def main():
    maze = Maze.load_maze("route.txt")
    path = maze.find_shortest_path()
    maze.print_mazeWithPath(path)
    Maze.print_path(path)
    #print(path)

if __name__=="__main__":
    main()
