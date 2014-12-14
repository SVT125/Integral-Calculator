from scipy.integrate import quad
import math

# Shunting Yard algorithm used as a calculator -> scipy.integrate.
# Assume for now, query strings will have all characters separated by whitespace.
# Handle square roots later, for now assume ^ .5.
def integrate(query:str, a:float, b:float) -> float:
        expr = convert_rpn(query)
        result = quad(lambda x: eval(expr),a,b)
        return result[0]
        
def has_precedence(op1:str,op2:str,operators:'list of str') -> bool:
        return operators.find(op1) > operators.find(op2)
        
def convert_rpn(query:str) -> str:
        '''Converts query using Shunting-Yard to RPN.'''
        characters = query.split()
        rpn_query = ''
        operator_stack = []
        operators = ['+', '-','/', '*','^', '(', ')']
        for char in characters:
                if char in operators:
                        while has_precedence(char,operators[-1],operators): #that this new token > last operator on stack
                                rpn_query = rpn_query + (" " + operator_stack.pop())
                        operator_stack.append(char)
                else:
                        converted_char = adjust_char(char)
                        rpn_query = rpn_query + (" " + converted_char)
                        
        return rpn_query.strip()

def adjust_char(c:str) -> str:
        '''Converts the given character into something parseable.'''
        old_chars = ['^','e','sin','cos','tan','cot','sec','csc','arcsin','arccos','arctan'] #fill
        new_chars = ['**','math.e','math.sin','math.cos','math.tan','1/math.tan','1/math.cos','1/math.sin','math.asin','math.acos','math.atan'] #fill
        for i in range(len(old_chars)):
                c = c.replace(old_chars[i],new_chars[i])
        return c

print(integrate('x+2',0,2))
print(integrate('x^2',0,3))
print(integrate('e^x',0,1))
print(integrate('cot(tan(x))',0.5,1))
#print(integrate('arctan(x^2)',0.1))
