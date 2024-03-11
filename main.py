
def check_brackets(input_str):
    stack = []
    output_str = ""
    for i, char in enumerate(input_str):
        if char == '(':
            stack.append(i)
            output_str += ' '
        elif char == ')':
            if stack:
                stack.pop()
                output_str += ' '
            else:
                output_str += '?'
        else:
            output_str += ' '

    while stack:
        index = stack.pop()
        output_str = output_str[:index] + 'x' + output_str[index + 1:]

    output_str = input_str + '\n' + output_str
    return output_str


# 测试用例
test_cases = [
    "bge)))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()",
]

for test_case in test_cases:
    print(check_brackets(test_case))

