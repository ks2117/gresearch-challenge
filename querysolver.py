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
                        
            

                
                
