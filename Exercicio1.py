
# Exercício 1
def fibonacciSequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def checkFibonacci(n):
    fib_sequence = fibonacciSequence(n)
    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
print(checkFibonacci(numero))