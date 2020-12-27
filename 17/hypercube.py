import copy
from pprint import pprint

class HyperCube:
    
    def __init__(self, initial_layer):
        self.initial_layer = initial_layer
        self.matrix = [[[]]]
        for row in initial_layer:
            self.matrix[0][0].append([c for c in row])
       

    def enlarge(self):
        for w in self.matrix:
            for z in w:
                for x in z:
                    x.insert(0, '.')
                    x.append('.')
                z.insert(0, ['.' for i in range(len(x))])
                z.append(['.' for i in range(len(x))])
            w.insert(0, [['.' for i in range(len(x))] for j in range(len(z))])
            w.append([['.' for i in range(len(x))] for j in range(len(z))])
        self.matrix.insert(0, [[['.' for i in range(len(x))] for j in range(len(z))] for k in range(len(w))])
        self.matrix.append([[['.' for i in range(len(x))] for j in range(len(z))] for k in range(len(w))])


    def check(self, elem, w, z, x, y):
        counter = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    for l in [-1, 0, 1]:
                        if not all([num == 0 for num in [i, j, k, l]]):
                            if (w+i >= 0 and w+i < len(self.matrix)) and (z+j >= 0 and z+j < len(self.matrix[w+i])) and \
                                (x+k >= 0 and x+k < len(self.matrix[w+i][z+j])) and (y+l >= 0 and y+l < len(self.matrix[w+i][z+j][x+k])):
                                if self.matrix[w+i][z+j][x+k][y+l] == '#':
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
        for i, w in enumerate(self.matrix):
            for j, z in enumerate(w):
                for k, x in enumerate(z):
                    for l, elem in enumerate(x):
                        parallel_matrix[i][j][k][l] = self.check(elem, i, j, k, l)
        
        self.matrix = parallel_matrix


    def count_actives(self):
        counter = 0
        for w in self.matrix:
            for z in w:
                for x in z:
                    for elem in x:
                        if elem == '#':
                            counter += 1
        return counter