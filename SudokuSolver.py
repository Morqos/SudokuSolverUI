"""

GUI:    The GUI is made with tkinter.
        The Grid is displayed with a 9x9 Matrix of Entry, gray and white colored and positioned with .grid()
        No Buttons, 1 Menu with 'File' cascade and 3 commands: 'Exit', 'Solve' and 'Clear'
        It reset the cell if it's not inserted 1-9 number

ALGORITHM - BRUTE FORCE:
        Starts setting to 0 all empty cells
        Search the next cell to fill checking if is equal to 0
        Tries 1-9 numbers until it finds the first correct one for that cell and puts the number into it
        If going along it will find an error, it will recoursively delete all the inserted cells
        It restarts the algorithm and repeats it until finds the correct numbers

"""


from tkinter import *


root = Tk()
root.geometry('275x283')


# Solve the Sudoku
class SolveSudoku():
    

    def __init__(self):
        self.allZero()
        self.startSolution()


    # Set the empty cells to 0
    def allZero(self):
        for i in range(9):
            for j in range(9):
                if savedNumbers[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    savedNumbers[i][j].set(0)


    # Start the Algorithm
    def startSolution(self, i=0, j=0):
        i,j = self.findNextCellToFill(i, j)

        # If i == -1 the position is Ok or the Sudoku is Solved
        if i == -1:
            return True
        for e in range(1,10):
            if self.isValid(i,j,e):
                savedNumbers[i][j].set(e)
                if self.startSolution(i, j):
                    return True
                # Undo the current cell for backtracking
                savedNumbers[i][j].set(0)
        return False


    # Search the Nearest Cell to fill
    def findNextCellToFill(self, i, j):

        for x in range(i,9):
            for y in range(j,9):
                if savedNumbers[x][y].get() == '0':
                    return x,y

        for x in range(0,9):
            for y in range(0,9):
                if savedNumbers[x][y].get() == '0':
                    return x,y

        return -1,-1


    # Check the Validity of savedNumbers[i][j]
    def isValid(self, i, j, e):

        for x in range(9):
            if savedNumbers[i][x].get() == str(e):
                return False

        for x in range(9):
            if savedNumbers[x][j].get() == str(e):
                return False

        # Finding the Top x,y Co-ordinates of the section containing the i,j cell    
        secTopX, secTopY = 3 *int((i/3)), 3 *int((j/3))
        for x in range(secTopX, secTopX+3):
            for y in range(secTopY, secTopY+3):
                if savedNumbers[x][y].get() == str(e):
                    return False
        
        return True
        



class Launch():
    
    # Set Title, Grid and Menu
    def __init__(self, master):
        
        # Title and settings
        self.master = master
        master.title("Sudoku Solver")

        font = ('Arial', 18)
        color = 'white'
        px, py = 0, 0

        # Front-end Grid
        self.__table = []
        for i in range(1,10):
            self.__table += [[0,0,0,0,0,0,0,0,0]]

        for i in range(0,9):
            for j in range(0,9):
                
                if (i < 3 or i > 5) and (j < 3 or j > 5):
                    color = 'gray'
                elif i in [3,4,5] and j in [3,4,5]:
                    color = 'gray'
                else:
                    color = 'white'

                self.__table[i][j] = Entry(master, width = 2, font = font, bg = color, cursor = 'arrow', borderwidth = 0,
                                          highlightcolor = 'yellow', highlightthickness = 1, highlightbackground = 'black',
                                          textvar = savedNumbers[i][j])
                self.__table[i][j].bind('<Motion>', self.correctGrid)
                self.__table[i][j].bind('<FocusIn>', self.correctGrid)
                self.__table[i][j].bind('<Button-1>', self.correctGrid)
                self.__table[i][j].grid(row=i, column=j)


        # Front-End Menu
        menu = Menu(master)
        master.config(menu = menu)

        file = Menu(menu)
        menu.add_cascade(label = 'File', menu = file)
        file.add_command(label = 'Exit', command = master.quit)
        file.add_command(label = 'Solve', command = self.solveInput)
        file.add_command(label = 'Clear', command = self.clearAll)


    # Correct the Grid if inputs are uncorrect
    def correctGrid(self, event):
        for i in range(9):
            for j in range(9):
                if savedNumbers[i][j].get() == '':
                    continue
                if len(savedNumbers[i][j].get()) > 1 or savedNumbers[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    savedNumbers[i][j].set('')


    # Clear the Grid
    def clearAll(self):
        for i in range(9):
            for j in range(9):
                savedNumbers[i][j].set('')


    # Calls the class SolveSudoku
    def solveInput(self):
        solution = SolveSudoku()

        
        

# Global Matrix where are stored the numbers
savedNumbers = []
for i in range(1,10):
    savedNumbers += [[0,0,0,0,0,0,0,0,0]]
for i in range(0,9):
    for j in range(0,9):
        savedNumbers[i][j] = StringVar(root)


app = Launch(root)
root.mainloop()