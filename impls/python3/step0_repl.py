IS_RUNNING = True


def READ(*, input: str) -> str:
    return input


def EVAL(*, input: str) -> str:
    return input


def PRINT(*, input: str) -> str:
    return input


def rep(*, input: str) -> str:
    read_output = READ(input=input)
    eval_output = EVAL(input=read_output)
    print_output = PRINT(input=eval_output)
    return print_output


while IS_RUNNING:
    try:
        print('user> ')
        line = str(input())
        output = rep(input=line)
        print(output)
    except EOFError:
        IS_RUNNING = False
        print('Exitting...')
