def raiz_enesima_newton(S, n, tolerancia=1e-10, max_iteracoes=100):
    """
    Calcula a raiz de índice 'n' de 'S' usando o método de Newton-Raphson.
    
    Parâmetros:
    S (float): O número base.
    n (int): O índice da raiz (ex: 2 para quadrada, 3 para cúbica).
    tolerancia (float): A precisão desejada para a resposta.
    max_iteracoes (int): O limite de repetições.
    """
    if n == 0:
        raise ValueError("O índice da raiz não pode ser zero.")
        
    # Tratamento para números negativos
    sinal = 1
    if S < 0:
        if n % 2 == 0:
            raise ValueError("Não existe raiz real de índice par para um número negativo.")
        else:
            # Se for ímpar e negativo (ex: raiz cúbica de -8), guardamos o sinal e calculamos do valor positivo
            sinal = -1
            S = abs(S)

    if S == 0:
        return 0.0

    # Chute inicial
    x = S / n if S > 1.0 else 1.0

    for iteracao in range(max_iteracoes):
        # Aplica a fórmula generalizada
        proximo_x = (1.0 / n) * ((n - 1) * x + S / (x ** (n - 1)))

        # Verifica a convergência
        if abs(x - proximo_x) < tolerancia:
            return proximo_x * sinal

        # Atualiza para a próxima iteração
        x = proximo_x

    print("Aviso: O método não convergiu dentro do número máximo de iterações.")
    return x * sinal

# Testando o código
n = 3
s = 10
#n = int(input("Digite o índice da raiz (n): "))
#s = int(input("Digite o número base (S): "))

resultado = raiz_enesima_newton(s, n, tolerancia=1e-40, max_iteracoes=10000000)
print(f"A raiz de índice {n} de {s} é aproximadamente: {resultado}")