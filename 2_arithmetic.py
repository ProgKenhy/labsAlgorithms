OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y), '*': (2, lambda x, y: x * y),
             '/': (2, lambda x, y: x / y)}


def eval_(start_formula):
    if '/0' in start_formula:
        print("Делить на ноль нельзя!")
        return None
    if '()' in start_formula:
        print("Недопустимые пустые скобки!")
        return None
    is_any_digits = False
    for i in range(10):
        if str(i) in start_formula:
            is_any_digits = True
    if not is_any_digits:
        print("Отсутствуют цифры в формуле!")
        return None

    parentheses = 0
    previous = ''
    for i in start_formula:
        if not (i in '0123456789.()' or i in OPERATORS):
            print("Недопустимый символ:", i)
            return None
        if previous in OPERATORS and i in OPERATORS:
            print("В формуле два подряд идущих оператора!")
            return None
        previous = i

        if i == '(':
            parentheses += 1
        elif i == ')':
            parentheses -= 1
            if parentheses < 0:
                print("Закрывающая скобка перед открывающей!")
                return None
    if parentheses != 0:
        print("Не хватает закрывающей скобки!")
        return None

    def parser(formula):
        number = ""
        for elem in formula:
            if elem in '0123456789.':
                number += elem
            elif number:
                yield number
                number = ''
            if elem in OPERATORS or elem in '()':
                yield elem
        if number:
            yield number

    def polish_notation(parsed_formula):
        stack = []
        for elem in parsed_formula:
            if elem == '(':
                stack.append(elem)
            elif elem in OPERATORS:
                while stack and stack[-1] != '(' and OPERATORS[stack[-1]][0] >= OPERATORS[elem][0]:
                    yield stack.pop()
                stack.append(elem)
            elif elem == ')':
                while stack and stack[-1] != '(':
                    yield stack.pop()
                if not stack:
                    print("Формула неверна!")
                    return None
                stack.pop()
            else:
                yield elem
        while stack:
            yield stack.pop()

    def calc_from_notation(notation_formula):
        stack = []
        for elem in notation_formula:
            if elem in OPERATORS and len(stack) > 1:
                y, x = stack.pop(), stack.pop()
                stack.append(OPERATORS[elem][1](float(x), float(y)))
            else:
                stack.append(elem)
        yield stack[0]

    parsed_formula = parser(start_formula)
    if parsed_formula is None:
        return None

    return calc_from_notation(polish_notation(parsed_formula))


formula = ''
print("Enter the formula, where '=' - last symbol: ")
while True:
    formula += str(input())
    if '=' in formula[-1]:
        if len(formula) == 1:
            print('Repeat please')
        result = eval_(formula[:-1])
        if result:
            print(*result)
        print("Enter the formula, where '=' - last symbol: ")
        formula = ''
