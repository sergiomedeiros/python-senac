# Receba quatro notas, calcule a média e mostre o seguinte
# resultado :>= 7 Aprovado, >= 5 e < 7 Recuperação e < 5 reprovado.

v_nota1 = int(input('Informe 1a nota  ..: '))
v_nota2 = int(input('Informe 2a nota  ..: '))
v_nota3 = int(input('Informe 3a nota  ..: '))
v_nota4 = int(input('Informe 4a nota  ..: '))
v_media = ((v_nota1 + v_nota2 + v_nota3 + v_nota4) / 4)
print(v_media)

if v_media >= 7:
    print('Aprovado')
elif v_media >= 5 and v_media < 7:
    print('Recuperação')
else:
    print('Reprovado')
    
