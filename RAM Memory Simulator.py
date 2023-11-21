class SimuladorMemoria:
    def __init__(self, enderecos, tamanho_celula=8):
        self.memoria = {}
        self.enderecos = enderecos
        self.bits_endereco = len(bin(enderecos - 1)[2:])
        self.tamanho_celula = tamanho_celula

    def armazenar(self, endereco, dados):
        if endereco < self.enderecos:
            if 0 <= dados < 2**self.tamanho_celula:
                self.memoria[endereco] = dados
                print(f"Armazenando {dados} no endereço {endereco}")
            else:
                print(
                    f"Erro: Valor {dados} fora do alcance da célula de {self.tamanho_celula} bits.")
        else:
            print("Erro: Endereço inválido!")

    def carregar(self, endereco):
        if endereco < self.enderecos:
            if endereco in self.memoria:
                dados = self.memoria[endereco]
                print(f"Lendo {dados} do endereço {endereco}")
            else:
                print(f"Erro: Nenhum dado encontrado no endereço {endereco}")
        else:
            print("Erro: Endereço inválido!")


def main():
    enderecos = int(input("Digite o número de endereços da memória: "))
    tamanho_celula = int(
        input("Digite o tamanho da célula de memória (em bits): "))
    print(f"Tamanho da memória: {enderecos}")
    print(f"Tamanho da célula: {tamanho_celula} bits")
    simulador_memoria = SimuladorMemoria(enderecos, tamanho_celula)

    while True:
        comando = input(
            "Digite um comando (ST <endereço> <dados> ou LD <endereço>): ")
        if comando.lower() == "parar":
            break

        partes = comando.split()
        if len(partes) < 2:
            print(f"Comando inválido: {comando}")
            continue

        operacao = partes[0]
        if operacao == "ST":
            if len(partes) == 3:
                endereco = int(partes[1], 16)
                dados = int(partes[2])
                simulador_memoria.armazenar(endereco, dados)
            else:
                print(f"Comando ST malformado: {comando}")

        elif operacao == "LD":
            if len(partes) == 2:
                endereco = int(partes[1], 16)
                simulador_memoria.carregar(endereco)
            else:
                print(f"Comando LD malformado: {comando}")

        else:
            print(f"Comando desconhecido: {comando}")


if __name__ == '__main__':
    main()
