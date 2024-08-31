# Exercício 2

name = input("Digite um nome: ")


def count_letters_A(name):
    count = 0
    contupper = 0
    contlower = 0
    for letter in name:
        
        if letter == 'A':
            contupper += 1
            count += 1
        if letter == 'a':
            contlower += 1
            count += 1
    return count, contupper, contlower   

count, contupper, contlower = count_letters_A(name)

print(f"O nome {name} possui {count} letras 'A', {contupper} 'A' maiúsculas e {contlower} 'a' minúsculas.")



