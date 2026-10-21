# Repete até que o usuário informe uma senha válida
while True:

    # Solicita a senha ao usuário
    senha = input("Cadastre sua senha: ")

    # Variáveis de controle
    has_upper = False
    has_number = False
    has_special = False

    # Percorre cada caractere da senha
    for char in senha:

        # Verifica se existe letra maiúscula
        if char.isupper():
            has_upper = True

        # Verifica se existe número
        elif char.isdigit():
            has_number = True

        # Verifica se existe caractere especial
        elif not char.isalnum():
            has_special = True

    # Esta verificação deve ficar FORA do for
    if len(senha) >= 9 and has_upper and has_number and has_special:

        print("Senha forte!")
        print("Senha cadastrada com sucesso!")

        # Sai do loop
        break

    else:

        print(
            "Senha fraca! Senha deve ter pelo menos "
            "9 caracteres, uma letra maiúscula, "
            "um número e um caractere especial."
        )

        print("Tente novamente.\n")