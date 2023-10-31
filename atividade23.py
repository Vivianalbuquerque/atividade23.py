# Exercício Python 23: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.
numero =(range (1, 501))
soma = 0
for item in numero:
    while item % 3 == 0: 
    print(f"a soma de todos os multiplos é {item}")