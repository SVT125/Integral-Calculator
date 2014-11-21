from scipy.integrate import quad
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
			rpn_query = rpn_query + (" " + char)
	return rpn_query.strip()

print(integrate('x+2',0,2))
