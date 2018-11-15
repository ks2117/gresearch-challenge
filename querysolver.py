
import webhandler
import Queue
def is_left_associative(op):
    ops = "+-*/)"

    return op in ops

def get_precedence(op):
    order = {"&":3, "-":0, "+":0, "*":1, "/":1, "(": 2, ")":2}
    return order[op]

                
class QuerySolver(object):
    def __init__(self):
        pass

    def answer_query(self, query):
        """Answer a query"""
        output_queue = []
        operator_queue = Queue.queue()
        
        precedence = ["&*/+-"]
        args = query.split()
        operation = []
        for j in args:
            if not j.isdigit():
                operator_queue += [j]
        for i in args:
            print(i)
            if i.isdigit():
                output_queue += [i]

            else:
                if len(output_queue) > 0:
                    while True:
                        op = operator_queue[-1]
                        prec = get_precedence(op)
                        precown = get_precedence(i)
                      
                
                        if (prec >precown or (prec == precown and is_left_associative(prec)) and op != "("):
                            del operator_queue[-1]
                            output_queue.put(op)

                            if op == "(":
                                operator_queue += [op]

                            if op == ")":
                                while True:
                                    b = operator_queue[-1]
                                    if b == "(":
                                        del operator_queue[-1]
                                        break

                                    del operator_queue[-1]
                                    output_queue.put(op)

                        else:
                            break
        while len(operator_queue) != 0:
            output_queue.put(operator_queue.pop())

        return output_queue                      
                        
            

class QuerySolver2(object):
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

