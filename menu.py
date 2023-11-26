from cofrinho import Cofrinho, Item, Moeda

if __name__ == "__main__":
    cor_cofre = input("Digite uma cor para o cofre: ")
    tamanho_cofre = int(input(f"Digite o tamanho desejado para o cofre: "))
    cofre = Cofrinho(cor_cofre, tamanho_cofre)

    while True:
        print("\nEscolha uma opção:")
        print("1. Inserir moeda")
        print("2. Inserir item")
        print("3. Quebrar cofre")
        print("4. Verificar volume livre")
        print("5. Mostrar conteúdo do cofre")
        print("6. Calcular valor total em moedas")
        print("7. Ver cor do cofre")
        print("8. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            escolha_moeda = input("Escolha a moeda (10, 25, 50, 100): ")
            if escolha_moeda.isdigit() and int(escolha_moeda) in [10, 25, 50, 100]:
                cofre.adicionar_moeda(Moeda(int(escolha_moeda)))
            else:
                print("Moeda inválida. Tente novamente.")

        elif opcao == "2":
            descricao_item = input("Digite a descrição do item: ")
            volume_item = int(input("Digite o volume do item: "))
            item = Item(descricao_item, volume_item)
            cofre.adicionar_item(item)

        elif opcao == "3":
            cofre.quebrar_cofre()
    
        elif opcao == "4":
            print(f"Volume livre no cofre: {cofre.volume_disponivel()}")

        elif opcao == "5":
            cofre.olhar_conteudo()

        elif opcao == "6":
            cofre.valor_total()

        elif opcao == "7":
            print(f"Cor do cofre: {cofre.cor}")

        elif opcao == "8":
            break

        else:
            print("Opção inválida. Tente novamente.")
