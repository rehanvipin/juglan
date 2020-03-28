# juglan
A Web Application built with Django to solve Sudoku grids of sizes 4x4, 9x9 and 16x16  
Will be hosted on Heroku later(Hopefully)

### Working 
1. The command line version
    * Create a file with the grid, first line must be number of rows, the following lines the rows themselves
    * Pass the file's data, e.g input.txt, as input while executing sudoku.py
    * POSIX: ```python3 sudoku.py < input.txt```
    * Windows Powershell: ```Get-Content input.txt | python sudoku.py ```
