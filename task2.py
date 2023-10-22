"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""

def is_pythagorean_triple(a, b, c):
    return a**2 + b**2 == c**2

def pythagoreantriplesin_file(filename):
    count = 0
    
    with open(filename, 'r') as file:
        for line in file:
           
            numbers = line.strip().split()
            if len(numbers) == 3:
                try:
                    a, b, c = map(int, numbers)
                    
                    if is_pythagorean_triple(2*a, 2*b, 2*c):
                        count += 1
                except ValueError:
                    pass

    return count

filename = "task02a.txt"  
pythagorean_triples_count = pythagoreantriplesin_file(filename)

print("Number of Pythagorean triples in the file:", pythagorean_triples_count)
