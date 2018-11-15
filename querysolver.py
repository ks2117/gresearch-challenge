import webhandler

class QuerySolver(object):
    def __init__(self):
        pass

    def answer_query(self, query):
        expression = query.split(' ')
        for elem in expression:
            if(is_roman(elem)):
                elem = rom_to_dec(elem)
                
        return 85
    
    def is_roman(self, expr):
        romans = "MDCLXVI"
        for char in expr:
            if(not char in romans):
                return False
        return True
            
    
    def rom_to_dec(self, rom, 
    values={'M': 1000, 'D': 500, 'C': 100, 'L': 50, 
                                'X': 10, 'V': 5, 'I': 1}):
        dec = []
        res = 0
        for char in rom:
            dec.append(values[char])
        for a, b in zip(dec, dec[1:]):
            if(a >= b):
                res += a
            else:
                res -= a
        return res + b

a = QuerySolver()