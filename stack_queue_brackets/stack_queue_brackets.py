
open_brackets = ["[","{","("]
close_brackets = ["]","}",")"]


def validate_brackets(input_string):
    stack = []
    for i in input_string:
        if i in open_brackets:
            stack.append(i)
        elif i in close_brackets:
            pos = close_brackets.index(i)
            if ((len(stack) > 0) and
                (open_brackets[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(validate_brackets('{}'))
    print(validate_brackets('{}(){}	'))
    print(validate_brackets('()[[Extra Characters]]	'))
    print(validate_brackets('(){}[[]]	'))
    print(validate_brackets('{}{Code}[Fellows](())	'))
    print(validate_brackets('[({}]'))
    print(validate_brackets('(]('))
    print(validate_brackets('{(})'))

    print(validate_brackets('{'))
    print(validate_brackets(')'))
    print(validate_brackets('[}'))



# def validate_brackets(str):
#     stack = []
#     for char in str:
#         if char in ["(", "{", "["]:
#             stack.append(char)
#         else:
#             if not stack:
#                 return False
#             current_char = stack.pop()
#             if current_char == '(':
#                 if char != ")":
#                     return False
#             if current_char == '{':
#                 if char != "}":
#                     return False
#             if current_char == '[':
#                 if char != "]":
#                     return False
#     if stack:
#         return False
#     return True
