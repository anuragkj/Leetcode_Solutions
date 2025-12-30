class Solution:
    def numMagicSquaresInside(self, g: List[List[int]]) -> int:
        return sum(''.join(map(str,g[i][j:j+3]+g[i+1][j:j+3]+g[i+2][j:j+3])) in 
                {'276951438','294753618','438951276','492357816','618753294','672159834','816357492','834159672'} 
                for i,j in product(range(len(g)-2), range(len(g[0])-2)))
