# обработка выражений с комплексными числами
# ограничения:
# есть всего 2 числа и одна операция
# читаются только однозначные числа


def is_expression_ok(expression) -> bool:
    if expression.count('j') != 2:
        return False
    if {'-', '+', '*', '/'}.isdisjoint(expression):
        return False
    try:
        for i in range(expression.count('j')):
            if expression[expression.index('j') - 2] not in {'-', '+'}:
                return False
    except:
        return False
    return True


# создать комплексное число из строки. предполагается, что строка имеет вид a+\-bj, числа однозначные
def make_complex(num: str) -> complex:
    sec_num = float(num[-2]) if num[-3] == '+' else -float(num[-2])
    oper = complex(float(num[0]), sec_num)
    return oper


def parse_c_str(expression: str):
    expression = expression.replace(' ', '')
    firstj = expression.index('j')
    oper1 = make_complex(expression[:firstj + 1])
    sign = expression[firstj + 1:firstj + 2]
    oper2 = make_complex(expression[firstj + 2:])
    return oper1, oper2, sign


def make_operation(x: complex, y: complex, sign: str) -> str:
    res = ''
    match sign:
        case '+':
            res = str(x + y)
        case '-':
            res = str(x - y)
        case '*':
            res = str(x * y)
        case '/':
            res = str(x / y)
    return res.replace('(', '').replace(')', '')
