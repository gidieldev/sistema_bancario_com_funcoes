#-----------------------------------------------------------------------------------------
#OBJETIVO: PEGAR O MESMO PROGRAMA E DEIXAR CADA MOVIMENTAÇÃO ORGANIZADO EM FUNÇÕES
#CRIANDO FUNCOES PARA CADA TIPO DE MOVIMENTACAO:
#FUNCAO DEPOSITO / FUNCAO SAQUE / FUNCAO EXTRATO
#CRIAR DUAS NOVAS FUNCOES: CADASTRAR CLIENTE E CADASTRAR CONTA BANCÁRIA

#-----------------------------------------------------------------------------------------------------------------------
#FUNCAO PARA EXIBIR O MENU
def menu_inicial():
    print('''
        SISTEMA BANCÁRIO
        
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nu] Novo Usuário
        [nc] Nova Conta
        [lc] Listar Contas
        
        => """ ''')
    opcao = input("Informe a opção: ")
    return opcao 

#FUNCAO PARA DEPOSITO
def depositar(saldo, extrato, /):
    while True:
        valor = float(input('Informe o valor que deseja depositar: '))
        #se o valor for zero ou negativo, ele da erro e fica pedindo um valor válido.
        while valor <= 0:
            valor = float(input('Informe um valor válido:'))
        
        saldo += valor
        #EXTRATO DE DEPÓSITOS
        extrato += f"Depósito: R${valor:.2f}\n"
        print(f'O Depósito de R$ {valor:.2f} foi efetuado com sucesso.')

        Continuar_Deposito = str(input('Deseja continuar a depositar?:[S/N] ')).upper().strip()

        #Se na variavel estiver dentro não, entao o loop irá parar e volta para o menu, pois encerra um ciclo do laço.
        if Continuar_Deposito in ["N", "NÃO", "NAO"]:
            break
    return saldo, extrato    



def sacar(*, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    while True:
        valor = float(input('Informe o valor que deseja sacar: '))
        
        # CAMINHO FELIZ: verificando se nao excedeu o numero de saques diarios e se tem algum dinheiro na conta.
        if numero_saques < LIMITE_SAQUES and saldo > 0:

            #CAMINHO TRISTE.  (OR = "SE TIVER ALGUM DESSES CASOS")
            while (valor <= 0) or (valor > saldo) or (valor > limite):
                #Para cada caso, tem uma mensagem de erro.
                if valor > limite:
                    print(f'O valor é maior do que o limite de R$ 500 por saque.')
                    valor = float(input('Informe um valor válido:'))    
                elif valor > saldo:
                    print("O valor informado é maior do que o saldo disponível.")
                elif valor > limite:
                    print("O valor informado é maior do que o limite de R$500,00 por saque.")

            #CAMINHO FELIZ.
            saldo -= valor 
            #a lista de saques recebe o valor sacado
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
            print(f'O Saque de R$ {valor:.2f} foi efetuado com sucesso.')

            Continuar_Saque = str(input('Deseja sacar novamente?: [S/N] ')).upper().strip()
            if Continuar_Saque in ["N", "NÃO", "NAO"]:
                break

        #CAMINHO TRISTE: (EXTRAPOLOU A QUANTIDADE DE SAQUE DIARIO OU NAO TIVER SALDO)
        else:
            if saldo <= 0:
                print('Você não possui saldo disponível')
                break
            if numero_saques >= LIMITE_SAQUES:
                print('O número diário de 3 saques foi atingido.')
                break
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /,*, extrato):
      
    print("EXTRATO")
    #CAMINHO TRISTE: SE NÃO TEM NADA NO EXTRATO
    if not extrato:
        print("Não foram realizadas movimentações.")
    #CAMINHO FELIZ: EXIBIR O EXTRATO E SALDO
    else:
        print(f"{extrato}")
    print(f"Saldo: R${saldo:.2f}")
                
def criar_usuario(usuarios):
    cpf = input("Informe o cpf do usuário: ")
    #Analisando se esse cpf já foi cadastrado por outro usuário.
    #vou chamar a funcao que procura se existe algum cpf  na lista de usuários igual ao informado
    usuario = filtrar_usuario(cpf, usuarios)

    #se tiver conteúdo dentro de usuario (variavel acima que recebe o retorno da funcao filtrar_usuario)
    if usuario:
        print("Já existe um usuário com esse CPF!")
        
        #um comando return vazio (ou apenas return) encerra imediatamente a execução da função atual e devolve o controle para o ponto do código que a chamou.
        return
    
    #caso não existe nenhum usuário com esse cpf, ou seja, se a funcção filtrar_usuarios retornou None, a gente pode cadastrar o usuário:
    else:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        #criando um dicionario com esse usuario e colocando dentro da lista de usuarios
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("Usuário criado com sucesso.")

def filtrar_usuario(cpf, usuarios):
    #retorna e coloca na variavel todos os dados do usuario (o dicionario dele inteiro) caso o cpf desse usuario seja igual ao informado.
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf']== cpf]
    #returne o conteudo de usuarios_filtrados[0] (indice zero pq se retornar, sempre vai achar um usuário só)  se tiver conteúdo nele, se não, retorna None (vazio)
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(AGENCIA, numero_conta, usuarios):
    cpf = input("Informe o cpf do titular: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Conta cadastrada com sucesso.")
        return {"AGENCIA": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Não existe usuário com esse cpf.")
        return None

def listar_contas(contas):
    if contas:
        for conta in contas:
            #conta['usuario']['nome'] serve para acessar a chave interna ['nome'] dentro da chave maior
            linha = f" Agência: {conta['AGENCIA']}\nNúmero da conta: {conta['numero_conta']}\nUsuário: {conta['usuario']['nome']}"
            print(linha)
    else:
        print("Não existe conta cadastrada.")
        print()

#INICIO DO PROGRAMA PRINCIPAL
def main():
#criando dicionarios e listas


#CRIANDO AS VARIAVEIS
    extrato = ""
    saldo = 0
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    numero_conta = 0
    #o numero da conta vai mudando em ordem crescente. Ex: 1 conta criada: conta 1, depois conta 2, conta 3...

    while True:
        opcao = menu_inicial()
        if opcao == "d":
            #a variavel saldo e extrato vai receber o retorno da funcao depositar
            #colocamos o saldo e extrato como parametro porque o saldo e o extrato vão ser alterados após o depósito
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,  
                extrato=extrato,
                limite=limite,
                LIMITE_SAQUES = LIMITE_SAQUES, 
                numero_saques = numero_saques, 
                )

            
            print(f' Saldo atual: R${saldo:.2f}')
        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
            
        if opcao == "lc":
            listar_contas(contas)
main()