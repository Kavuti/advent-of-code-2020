import copy

class Cube:
    
    def __init__(self, initial_layer):
        self.initial_layer = initial_layer
        self.matrix = [[]]
        for row in initial_layer:
            self.matrix[0].append([c for c in row])
       

    def enlarge(self):
        for z in self.matrix:
            for x in z:
                x.insert(0, '.')
                x.append('.')
            z.insert(0, ['.' for i in range(len(x))])
            z.append(['.' for i in range(len(x))])
        self.matrix.insert(0, [['.' for i in range(len(x))] for j in range(len(z))])
        self.matrix.append([['.' for i in range(len(x))] for j in range(len(z))])


    def check(self, elem, z, x, y):
        counter = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    if not all([num == 0 for num in [i, j, k]]):
                        if (z+i >= 0 and z+i < len(self.matrix)) and (x+j >= 0 and x+j < len(self.matrix[z+i])) and \
                            (y+k >= 0 and y+k < len(self.matrix[z+i][x+j])):
                            if self.matrix[z+i][x+j][y+k] == '#':
                                # print(f"Found # in {z} {x} {y}")
                                counter += 1
        if elem == '#':
            if counter in [2, 3]:
                return '#'
            return '.'
        else:
            if counter == 3:
                return '#'
            return '.'


    def elaborate(self):
        self.enlarge()
        parallel_matrix = copy.deepcopy(self.matrix)
        for i, z in enumerate(self.matrix):
            for j, x in enumerate(z):
                for k, elem in enumerate(x):
                    parallel_matrix[i][j][k] = self.check(elem, i, j, k)
        
        self.matrix = parallel_matrix


    def count_actives(self):
        counter = 0
        for z in self.matrix:
            for x in z:
                for elem in x:
                    if elem == '#':
                        counter += 1
        return counter