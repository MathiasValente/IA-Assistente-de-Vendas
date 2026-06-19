import os
from dotenv import load_dotenv
from groq import Groq
from prompts import SYSTEM_PROMPT, build_user_prompt
from knowledge_loader import load_knowledge

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def gerar_resposta(tipo_interacao, mensagem_cliente):
    knowledge = load_knowledge()

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT + "\n\nBase de conhecimento:\n" + knowledge
            },
            {
                "role": "user",
                "content": build_user_prompt(tipo_interacao, mensagem_cliente)
            }
        ]
    )

    return response.choices[0].message.content


def menu_interacao():
    print("\nSelecione o tipo de interação:")
    print("1 - Atendimento")
    print("2 - Objeções")
    print("3 - Priorização")
    print("4 - Sair")

    escolha = input("Digite o número da opção: ")

    if escolha == "1":
        return "atendimento"
    elif escolha == "2":
        return "objecoes"
    elif escolha == "3":
        return "priorizacao"
    elif escolha == "4":
        return "sair"
    else:
        print("Opção inválida. Tente novamente.")
        return None


if __name__ == "__main__":
    print("=== Copiloto de Vendas FYS (Groq) ===")

    while True:
        tipo = None
        while tipo is None:
            tipo = menu_interacao()

        if tipo == "sair":
            print("\nEncerrando o Copiloto. Até a próxima!")
            break

        msg = input("\nDigite a mensagem do cliente: ")

        print("\nGerando resposta...\n")
        resposta = gerar_resposta(tipo, msg)

        print("=== RESPOSTA DO COPILOTO ===\n")
        print(resposta)
        print("\n----------------------------------------")
