from math import e


def raiz_quadrada_newton(S, tolerancia=1e-10, max_iteracoes=100):
    """
    Calcula a raiz quadrada de S usando o método de Newton-Raphson.
    
    Parâmetros:
    S (float): O número do qual queremos a raiz quadrada.
    tolerancia (float): A precisão desejada para a resposta.
    max_iteracoes (int): O limite de repetições para evitar loops infinitos.
    """
    if S < 0:
        raise ValueError("Não é possível calcular a raiz quadrada real de um número negativo.")
    if S == 0:
        return 0.0

    # Chute inicial: uma estimativa razoável ajuda a convergir mais rápido

    if S > 1.0:
        x = S / 2.0

    else:
        x = 1.0

    for iteracao in range(max_iteracoes):
        # Aplica a fórmula simplificada de Newton-Raphson
        proximo_x = 0.5 * (x + S / x)

        # Verifica se a diferença entre a tentativa atual e a próxima é menor que a tolerância
        if abs(x - proximo_x) < tolerancia:
            return proximo_x

        # Atualiza o x para a próxima iteração
        x = proximo_x

    print("Aviso: O método não convergiu dentro do número máximo de iterações.")
    return x

# Testando o código
numero = 25
raiz = raiz_quadrada_newton(numero)
print(f"A raiz quadrada de {numero} é aproximadamente: {raiz}")

# Comparando com uma raiz não exata
numero2 = 2
raiz2 = raiz_quadrada_newton(numero2)
print(f"A raiz quadrada de {numero2} é aproximadamente: {raiz2}")