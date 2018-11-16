import webhandler

class RpnEvaluator(object):
    def __init__(self):
        pass

    def evaluate_rpn(self, rpn):
        """Evaluate RPN"""
        args = rpn.split()
            
        nums = []

        for i in args:
            if i.isdigit():
                nums += [int(i)]
            else:
                arg1 = nums.pop()
                arg2 = nums.pop()
            
                if i == "+":
                    nums += [arg2 + arg1]

                elif i == "-":
                    nums += [arg2 - arg1]
                elif i == "/":
                    nums += [arg2 / arg1]

                elif i == "*":
                    nums += [arg1*arg2]

        return str(int(nums[0]))          
                    
        
