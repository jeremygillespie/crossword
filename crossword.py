square_values = [
    '#', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I',
    'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X',
    'Y', 'Z']
num_square_values = len(square_values)

class Puzzle:
    def __init__(self, x_axis=5, y_axis=5):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.num_squares = x_axis * y_axis
        self.num_atoms = self.num_squares * num_square_values

    def square_to_atom(self, square=('#', 0, 0)):
        """square is a tuple of (value, x, y)"""
        result = square_values.index(square[0]) * self.num_squares
        result +=  self.y_axis * square[1]
        result +=  square[2]
        result += 1
        return result

    def atom_to_square(self, atom=1):
        atm = atom
        if atm < 0:
            atm = -atm
        atm -= 1

        value = square_values[atm // self.num_squares]
        x = atm // self.y_axis % self.x_axis
        y = atm % self.y_axis
        return (value, x, y)

    def atoms_to_grid(self, atoms=[]):
        result = []
        for x in range(self.x_axis):
            result.append([])
            for y in range(self.y_axis):
                result[x].append('#')
        for atm in atoms:
            if atm > 0:
                square = self.atom_to_square(atm)
                result[square[1]][square[2]] = square[0]
        return result

    def print_grid(self, atoms=[]):
        grid = self.atoms_to_grid(atoms)
        for x in range(self.x_axis):
            for y in range(self.y_axis):
                print(grid[x][y] + ' ', end='')
            print()