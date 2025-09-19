class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = {}
    
    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value
    
    def resetCell(self, cell: str) -> None:
        if cell in self.cells:
            del self.cells[cell]
    
    def getValue(self, formula: str) -> int:
        idx = formula.index('+')
        left = formula[1:idx]
        right = formula[idx+1:]
        
        if left[0].isalpha():
            valLeft = self.cells.get(left, 0)
        else:
            valLeft = int(left)
        
        if right[0].isalpha():
            valRight = self.cells.get(right, 0)
        else:
            valRight = int(right)
        
        return valLeft + valRight
