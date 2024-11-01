# OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y), '*': (2, lambda x, y: x * y),
#              '/': (2, lambda x, y: x / y if y != 0 else False)}
#
#
# def eval_(start_formula):
#     def parser(formula):
#         result = []
#         number = ""
#         for elem in formula:
#             if elem.isdigit() or elem == '.':
#                 number += elem
#             elif number:
#                 result.append(number)
#                 number = ''
#             if elem in OPERATORS or elem in '()':
#                 result.append(elem)
#         if number:
#             result.append(number)
#         return result
#
#     def polish_notation(parsed_formula):
#         stack = []
#         result = []
#         for elem in parsed_formula:
#             if elem == '(':
#                 stack.append(elem)
#             elif elem in OPERATORS:
#                 while stack and stack[-1] != '(' and OPERATORS[stack[-1]][0] >= OPERATORS[elem][0]:
#                     result.append(stack.pop())
#                 stack.append(elem)
#             elif elem == ')':
#                 while stack and stack[-1] != '(':
#                     result.append(stack.pop())
#                 if not stack:
#                     print("Отсутствует открывающая скобка!")
#                     return None
#                 stack.pop()
#             else:
#                 result.append(elem)
#         while stack:
#             result.append(stack.pop())
#         print(result)
#         return result
#
#     def calc_from_notation(notation_formula):
#         stack = []
#         for elem in notation_formula:
#             if elem in OPERATORS and len(stack) > 1:
#                 y, x = stack.pop(), stack.pop()
#                 if isinstance(y, float) and isinstance(x, float):
#                     action = OPERATORS[elem][1](float(x), float(y))
#                     if action:
#                         stack.append(action)
#                     else:
#                         print("Делить на ноль нельзя!")
#                         return None
#                 else:
#                     print("Формула неверна!")
#                     print(x, y)
#                     return None
#             else:
#                 stack.append(elem)
#         return stack[0]
#
#     return calc_from_notation(polish_notation(parser(start_formula)))
#
#
# print(eval_(str(input("Enter the formula: "))))
