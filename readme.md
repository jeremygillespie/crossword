Generating NYT-style dense crossword puzzles in Python

Assumptions:
- The puzzle is an X\*Y grid. X\*Y = N
- Every square in the grid is a character A-Z or # (a black square).
- In every row and column, every sequence of characters (delineated by black squares and the edges of the puzzle) is a valid word according to some wordlist.

Aesthetic considerations:
- Puzzles with fewer '#'s are desireable.
- Puzzles with a mix of long and short words are desireable.
- Generally one- and two-letter words are not allowed.
- Bonus points for having the distribution of spaces in the puzzle be symmetrical, either 2-way or 4-way, rotational or mirror symmetry.

What we have here is a boolean satisfiability problem (or satisfiability maximization if you include the aesthetic considerations).

The atoms are every possible character in every possible location in the puzzle. They are ordered by value, x, and y in that order, e.g. (#, 0, 0), (#, 0, 1) etc.

Now we gotta put these statements in CNF:
- every square has a value (easy)
- no square has two values (easy)
- for every vertical or horizontal sequence of squares, if that sequence is delinieated by #s and/or edges, it must be included in the word list
- for every vertical or horizontal sequence of squares, if that sequence is delinieated by #s and/or edges, it must not be identical to any other such sequence