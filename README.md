# GUI-Sudoku-Solver

Graphic User Interface Sudoku Solver made with Python3, tkinter and Brute-Force algorithm

## GUI:

* The GUI is made with tkinter
* The Grid is displayed with a 9x9 Matrix of Entry, gray and white colored and positioned with .grid()
* No Buttons, 1 Menu with 'File' cascade and 3 commands: 'Exit', 'Solve' and 'Clear'
* It reset the cell if it's not inserted 1-9 number

## ALGORITHM - BRUTE FORCE:

* Starts setting to 0 all empty cells
* Search the next cell to fill checking if is equal to 0
* Tries 1-9 numbers until it finds the first correct one for that cell and puts the number into it
* If going along it will find an error, it will recoursively delete all the inserted cells
* It restarts the algorithm and repeats it until finds the correct numbers
