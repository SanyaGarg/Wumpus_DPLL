import copy

class Solver:
  call = 0
  def __init__(self, cnf,call):
    self.clauses = cnf
    self.call = call

  def solve(self):
    lst = copy.deepcopy(self.clauses)
    symbols = self.getSymbolsFromClauses(lst)
    val = self.dpll(copy.deepcopy(self.clauses), copy.deepcopy(symbols))
    return val
  
  def getCalls(self):
     return self.call

  def setCalls(self,x):
     self.call = x

  def dpll(self, clauses, symbols):
    x = self.getCalls()
    x = x+1
    self.setCalls(x)
    if self.isAllTrue(clauses):
      #print("gtd")
      return True

    if self.isAnyFalse(clauses):
      #print("gfd")
      return False
    
    if len(symbols) == 0:
      return False
    extndSym = self.findPureSymbols(symbols, clauses)
    if not self.isEmpty(extndSym):
      cls, p = self.extend(clauses, extndSym)
      return self.dpll(copy.deepcopy(cls), copy.deepcopy(symbols - p))

    
    extndSym = self.findUnitClauses(copy.deepcopy(clauses), max(symbols))
    if not self.isEmpty(extndSym):
      cls, p = self.extend(clauses, extndSym)
      return self.dpll(copy.deepcopy(cls), copy.deepcopy(symbols - p))
    
    
    extndSym1 = [None for i in range(0, max(symbols) + 1)]
    extndSym2 = [None for i in range(0, max(symbols) + 1)]
    p, rest = self.getFirstAndRest(symbols)
    extndSym1[p] = True
    extndSym2[p] = False
    cls1,sym1= self.extend(copy.deepcopy(clauses), extndSym1)
    cls2,sym2= self.extend(copy.deepcopy(clauses), extndSym2)
    return (self.dpll(copy.deepcopy(cls1), copy.deepcopy(rest)) or self.dpll(copy.deepcopy(cls2), copy.deepcopy(rest)))
  
 
  def isAllTrue(self, clauses):
    
    if len(clauses) == 0:
      return True
    
    return False
 
  def isAnyFalse(self, clauses):
    
    if len(clauses) < 1:
      return False
    
    flag = True
    for c in clauses:
      if len(c) > 0:
        flag = False
        break
      
    return flag
 
  def extend(self, clauses, extendedSymbols):
    
    sym = set()
    cls = []
    count = 0
    for e in extendedSymbols:
      if not (e is None):
        sym.add(count)

      count = count + 1
      
    for c in clauses:
      flag = False
      for s in sym:
        val = extendedSymbols[s]
        if (s in c) and val:
          flag = True
          break

        if(-s in c) and (not val):
          flag = True
          break

      if not flag:
        cls.append(c)
    
    for s in sym:
      val = extendedSymbols[s]
      for c in cls:
        if (s in c) and (not val):
          c.remove(s)
          continue

        if(-s in c) and val:
          c.remove(-s)
          continue
    
    return cls, sym

  def findPureSymbols(self, symbols, clauses):
    
    pureSymbols = [None for i in range(0, max(symbols) + 1)]
    
    for s in symbols:
      isPositive = False
      isNegative = False

      for c in clauses:
        if s in c:
          isPositive = True
        if -s in c:
          isNegative = True

      if isPositive and not isNegative:
        pureSymbols[abs(s)] = True
        continue

      if isNegative and not isPositive:
        pureSymbols[abs(s)] = False
        
    
    return pureSymbols

 
  def findUnitClauses(self, clauses, n):
    
    unitClauses = [None for i in range(0, n+1)]
    for c in clauses:
      if len(c) == 1:
        s = c.pop()
        c.append(s)
        if s > 0:
          unitClauses[s] = True
          continue

        if s < 0:
          unitClauses[-s] = False
          continue
    
    return unitClauses

  def getFirstAndRest(self, symbols):
    x = symbols.pop()
    return x, symbols
    
  def getSymbolsFromClauses(self, clauses):
    symbols = set()
    #print(clauses)
    for c in clauses:
     #print(c)
      while len(c) > 0:
        symbols.add(abs(c.pop()))
        
    return symbols
 
  def isEmpty(self, symbols):
    
    for s in symbols:
      if not s is None:
        return False

    return True
  