def cria_lista_ip():
    lista_ip = []
    for i in range(1, 255):
        for j in range(1, 255):
            ip = f"255.255.{i}.{j}"
            lista_ip.append(ip)
    return lista_ip


def main():
    lista_ip = cria_lista_ip()
    print(f"Total de endereços IP gerados: {len(lista_ip)}")
    print("Exemplos de endereços IP gerados:")
    for ip in lista_ip[:10]:  # Imprime os primeiros 10 endereços IP
        print(ip)

if __name__ == "__main__":
    main()  