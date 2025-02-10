def somar(n1, n2):
    """SOMA N1 POR N2"""
    return n1 + n2

def subtrair(n1, n2):
    """SUBTRAI N1 POR N2"""
    return n1 - n2

def multiplicar(n1, n2):
    """MULTIPLICA N1 POR N2"""
    return n1 * n2

def dividir(n1, n2):
    """DIVIDE N1 POR N2"""
    return n1 / n2

operation = {
    "+":somar,
    "-":subtrair,
    "*":multiplicar,
    "/":dividir
}

while True:
    answer = 0
    
    n1 = int(input("What's the first number?: "))
    
    should_accumulate = True
    while should_accumulate:
        for op in operation:
            print(op)
        selected_op = input("Pick an operation: ").lower()
        n2 = int(input("What's the next number?: "))

        answer = operation[selected_op](n1, n2)

        print(f"{n1} {selected_op} {n2} = {answer}")

        option = input(f"Type \'y\' to continue calculating with \'{answer}\', or type \'n\' to start a new calculation: ").lower()
        
        match option:
            case 'y':
                n1 = answer
                continue
            case 'n':
                should_accumulate = False
                break