def criar_usuario(usuarios):
    cpf = input("CPF (somente números): ")
    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("Usuário já existe.")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, número - bairro - cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário criado com sucesso.")
