### Sudoku Solver

#### Solver Explanation:

This sudoku solver uses a tree search method in order to find the solution. However the algorithm *does not try every possibility in the tree* --- this would take forever. Instead, the solver first finds the numbers which can go into a given empty-entry and stores this in an array that is the same shape as the board. 

After finding the array of allowed entries, the solver takes the empty-entry with the smallest list of allowed numbers and stores a copy of the board with each of the allowed numbers in the position of the empty-entry in a list (this is the *tree*). At this point the solver runs the same process on each of these entries in the tree:

1. Find the array of allowed numbers
2. Remove any incomplete boards for which the array of possibilities is empty.
3. Find the empty-entry with the smallest number of allowed entries
4. Store each of the smallest number of options
5. Remove any boards from the previous round

At each iteration the solver removes boards from the previous round together with any board whose array of possible entries is empty. Unless the reason it has no possible entries is because it is solved.

#### What actually happens:

When this solver runs, the tree often blows up to contain 1000s of possible entries at the peak. This means making all of the above checks on 1000s of boards. Unsuprisingly this means the code can be slow for any but the simplest Sudoku. Most run-of-the-mill newspaper sudoku are solved in < 5 minutes. However, there are difficult puzzles designed by Arto Inkala and Andrew Stuart which can take > 30 minutes to solve. 

#### Solver Alterations:

In order to make a faster solver I see two possibilities:

- Reduce the number of checks at each stage of the tree-search solver
- Use backtracking-recursion to explore the solution space more efficiently

