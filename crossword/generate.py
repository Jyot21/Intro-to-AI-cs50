import sys

from crossword import *
import numpy as np
from collections import deque
import time
class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        print(assignment)
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        
        for key in set(self.domains):
            total_set = self.domains[key].copy()
            for word in total_set:
                if len(word) != key.length:
                    self.domains[key].remove(word)
        #print(self.domains)
                
        
        #raise NotImplementedError

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        revised = False
        overlap = self.crossword.overlaps[x, y]
        #print("first turn", self.domains[x], overlap,self.domains[y])
        if not overlap:
            return revised
        all_words = self.domains[x].copy()
        for word in all_words:
            required = False
            for sec_word in self.domains[y]:
                if word[overlap[0]] == sec_word[overlap[1]]:
                    required = True
                    break
            if not required:
                self.domains[x].remove(word)
            revised = True
        #print("second turn", self.domains[x])
        return revised
        
        
        raise NotImplementedError

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if not arcs:
            arcs = []
            for x in self.crossword.variables:
                for candidate in self.crossword.neighbors(x):
                    if (candidate, x) not in arcs:
                        arcs.append((x,candidate))
            #print(arcs)
        arcs = deque(arcs)      #use arcs.popleft()
        
        
        while len(arcs) != 0:
            (x,y) = arcs.popleft()
            #print((x,y))
            if self.revise(x,y):
                if len(self.domains[x]) == 0:
                    return False
                for Z in self.crossword.neighbors(x) - {y}:
                    arcs.append((Z, x))
            
        return True
            
            
        
        #raise NotImplementedError

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        if len(assignment) != len(self.crossword.variables):
            return False
        
        for variable in set(assignment):
            if  len(assignment[variable]) == 0:
                return False
            
        return True
        #raise NotImplementedError

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        checked = []
        copy = set(assignment.values())
        if len(copy) != len(assignment.values()):
            return False
        for var in set(assignment):
            if len(assignment[var]) == 0:
                continue
            if len(assignment[var]) != var.length:
                return False
            
            for neighbour in self.crossword.neighbors(var):
                if neighbour not in assignment.keys() or neighbour in checked:
                    #print(var, neighbour)
                    continue
                overlap = self.crossword.overlaps[var, neighbour]
                if overlap is not None:
                    if assignment[var][overlap[0]] != assignment[neighbour][overlap[1]] :
                        return False
            checked.append(var)
        return True
        
        #raise NotImplementedError

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        domain_values = self.domains[var].copy()
        ordered_val = {}
        for value in domain_values:
            consist = 0
            for neighbour in self.crossword.neighbors(var):
                for word in self.domains[neighbour]:
                    new_assignment = assignment.copy()
                    new_assignment[var] = value
                    new_assignment[neighbour] = word
                    if self.consistent(new_assignment):
                        consist+=1
            ordered_val[value] = consist
        #print(ordered_val)
        return sorted(ordered_val, key = ordered_val.get, reverse = True)
        #raise NotImplementedError

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        var_list = {}
        alone = 1
        for variable in self.crossword.variables:
            if variable not in assignment.keys() or len(assignment[variable]) == 0:
                var_list[variable] = len(self.domains[variable])
                alone = variable
        #print(var_list,"asdfasdfdf")
        a = sorted(var_list, key=var_list.get)
        return a[0]
        #raise NotImplementedError

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        variable = self.assignment_complete(assignment)
        if variable:
            return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            new_assignment = assignment.copy()
            new_assignment[var] = value
            if self.consistent(new_assignment):
                result = self.backtrack(new_assignment)
                if result is not None:
                    return result
        return None
        
        
        
        #raise NotImplementedError


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None
    
    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    startTime = time.time()
    assignment = creator.solve()
    endtime = time.time()
    total = endtime-startTime
    print(f"time taken : {total} seconds" )
    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
