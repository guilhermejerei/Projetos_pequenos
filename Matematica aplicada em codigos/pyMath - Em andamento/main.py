def validar_numero(num) -> bool:
    if num.isdigit():
        return True
    return False
    
def digitar_termos(qtd_termos):
    termos = []
    for qtd in range(qtd_termos):
        termo = input(f"Digite o valor {qtd+1}:     ")
        if validar_numero(termo) == True:
         termos.append(termo)

    return termos

def somatorio(termos):
    soma = 0
    for termo in termos:
        soma += int(termo)
    return soma



quantidade = input("\nDigite quantos números serão somados:     ")

if validar_numero(quantidade) == True:
    termos = digitar_termos(int(quantidade))
    print("\n" + str(somatorio(termos)) + "\n")
else:
    print("\nQuantidade inválida.")