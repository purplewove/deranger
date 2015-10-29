'''
Created on Oct 23, 2015

@author: templetonc

n is the number of items in the permutation

'''
class Deranger():
    def __init__(self):
        pass
    
    def derange(self, n):
        self.n = n 
        self.solution = []
        self.backtrack()
        
    
    def backtrack(self):
        if self.is_solution():
            self.process_solution()
        else:
            candidates = self.construct_candidates()
            for candidate in candidates:
                self.make_move(candidate)
                self.backtrack()
                self.unmake_move()
    
    
    def construct_candidates(self):
        forbidden = len(self.solution)
        return [x for x in range(self.n) if x not in self.solution and x not in [forbidden]]  
        
    def is_solution(self):
        if len(self.solution) == self.n: 
            return True
        else:
            return False
        
    def process_solution(self):
        print [n + 1 for n in self.solution]
    
    def make_move(self, candidate):
        self.solution.append(candidate)
    
    def unmake_move(self):
        self.solution.pop()
        
        
if __name__ == '__main__':
    deranger = Deranger()
    deranger.derange(4)
