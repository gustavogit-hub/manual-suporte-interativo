import datetime

def mostrar_menu():
    print("=" * 40)
    print("    MANUAL INTERATIVO DE SUPORTE    ")
    print("=" * 40)
    print("1. Problemas de Rede")
    print("2. Problemas de Software")
    print("3. Problemas de Hardware")
    print("4. Sair")
    print("=" * 40)

def iniciar_manual():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            suporte_rede()
        elif escolha == "2":
            suporte_software()
        elif escolha == "3":
            suporte_hardware()
        elif escolha == "4":
            print("Encerrando o manual. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

def registrar_acesso(topico):
    with open("historico_manual.txt", "a", encoding="utf-8") as log:
        data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        log.write(f"{data} - Consulta: {topico}\n")

def suporte_rede():
    registrar_acesso("Problemas de Rede")
    print("\n📡 Suporte a Problemas de Rede:")
    print("- Verifique se o cabo de rede está conectado.")
    print("- Reinicie o modem e o roteador.")
    print("- Execute o comando 'ping google.com' para testar a conexão.")
    print("- Verifique as configurações de IP e DNS.\n")

def suporte_software():
    registrar_acesso("Problemas de Software")
    print("\n🧩 Suporte a Problemas de Software:")
    print("- Reinicie o programa ou o computador.")
    print("- Verifique se há atualizações disponíveis.")
    print("- Reinstale o software se o erro persistir.")
    print("- Consulte o log de erros, se disponível.\n")

def suporte_hardware():
    registrar_acesso("Problemas de Hardware")
    print("\n💻 Suporte a Problemas de Hardware:")
    print("- Certifique-se de que os cabos estão bem conectados.")
    print("- Verifique se o equipamento faz algum som (cooler, bip, etc.).")
    print("- Teste o hardware em outro computador, se possível.")
    print("- Verifique LEDs ou mensagens no painel frontal.\n")

# Iniciar o programa
iniciar_manual()
