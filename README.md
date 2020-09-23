# juglan
Programs to solve discrete optimization problems.  
They try to solve NP hard problems approximately in linear time/reasonable time.

### Working 
1. Sudoku CLI
    * Create a file with the grid, first line must be number of rows, the following lines the rows themselves
    * Pass the file's data, e.g input.txt, as input while executing sudoku.py
    * POSIX: ```python3 sudoku.py < input.txt```
    * Windows Powershell: ```Get-Content input.txt | python sudoku.py ```

## Targets
   - [ ] Convert into Django Web-App
   - [ ] Host on AWS/Heroku with custom domain
   - [ ] Add more programs
   - [ ] Make fancy front-end
   - [ ] Add solutions to really hard problems
