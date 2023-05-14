import re
operators = ['^', '*', '/', '-', '+']


#get brackets expression
def get_brackets(s):
    ex = re.findall(r"\(([^()]+)\)", s)
    return ex


#conduct an operation 
def conduct(operator, operand_1, operand_2):  
    if operator == '+':
        return operand_1 + operand_2
    elif operator == '-':
        return operand_1 - operand_2
    elif operator == '*':
        return operand_1 * operand_2
    elif operator == '^':
        return operand_1 ** operand_2
    elif operator == '/':
        return operand_1 / operand_2


#separate all operands and operations
def separate(s):
    op = []
    nums = []
    num = ''
    for i in s:
        if i not in operators or (num == '' and i == '-') : num += i
        else: 
            op.append(i)
            nums.append(float(num))
            num = ''
    nums.append(float(num))
    return op, nums    


#assemble an expression replacing all the "subexpressions" with their calculated values
def assemble(o, n):
    while o:    
        for op in operators:
            if op in o:
                i = o.index(op)
                number = conduct(op, n[i], n[i+1])
                n[i] = number
                n.pop(i+1)
                o.pop(i)
                break
          
    return n[0]


if __name__ == '__main__':
    expression = input('Enter an expression: ').replace(' ','')
    e = get_brackets(expression)
    while e:
        for i in e:
            solution = assemble(*separate(i))
            expression = expression.replace('('+ i +')', str(solution))
        e = get_brackets(expression)

    answer = assemble(*separate(expression))
    if answer.is_integer(): 
        answer = int(answer)
  
    print('Answer is: ' + str(answer))
  