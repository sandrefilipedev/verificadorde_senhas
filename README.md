 Password Checker 🔐

Sistema de validação de senhas desenvolvido em Python com foco em lógica de programação, estruturas de decisão, laços de repetição e validação de entrada do usuário.

 📋 Sobre o Projeto

Este projeto verifica se uma senha atende a critérios mínimos de segurança definidos pelo sistema.

Enquanto a senha não atender aos requisitos estabelecidos, o usuário será solicitado a informar uma nova senha.

O objetivo principal foi praticar conceitos fundamentais de desenvolvimento em Python através da implementação de um mecanismo simples de validação de credenciais.

 🚀 Funcionalidades

- Validação de senha em tempo real.
- Verificação de quantidade mínima de caracteres.
- Verificação de presença de letra maiúscula.
- Verificação de presença de número.
- Verificação de presença de caractere especial.
- Repetição automática da validação até que uma senha válida seja informada.
- Feedback claro ao usuário sobre os critérios exigidos.

 ✅ Critérios de Validação

Para que uma senha seja considerada forte, ela deve conter:

- Pelo menos 9 caracteres.
- No mínimo uma letra maiúscula.
- No mínimo um número.
- No mínimo um caractere especial.

### Exemplo de senha válida

```text
Python2026@
```

### Exemplo de senha inválida

```text
python123
```

Motivos:

- Não possui letra maiúscula.
- Não possui caractere especial.

🛠️ Tecnologias Utilizadas

- Python 3
- VS Code
- Git
- GitHub

 📚 Conceitos Praticados

Durante o desenvolvimento foram aplicados os seguintes conceitos:

- Variáveis
- Tipos de dados
- Estruturas condicionais (`if`, `elif`, `else`)
- Estruturas de repetição (`while`, `for`)
- Métodos de strings
  - `isupper()`
  - `isdigit()`
  - `isalnum()`
- Operadores lógicos
  - `and`
  - `not`
- Controle de fluxo com `break`
- Boas práticas de validação de dados

💻 Exemplo de Execução

text
Cadastre sua senha: python123

Senha fraca! A senha deve ter pelo menos 9 caracteres,
uma letra maiúscula, um número e um caractere especial.

Tente novamente.

Cadastre sua senha: Python123@

Senha forte!
Senha cadastrada com sucesso!

---

## 🎯 Objetivo de Aprendizado

Este projeto foi desenvolvido com o objetivo de fortalecer a base em
