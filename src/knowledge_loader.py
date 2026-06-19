import os

def load_knowledge():
    base_dir = os.path.join(os.getcwd(), "knowledge")

    files = [
        "transcricao-live-fys.txt",
        "produtos.md",
        "perguntas-frequentes.md",
        "objecoes.md",
        "contexto-do-negocio.md"
    ]

    knowledge = ""

    for file in files:
        path = os.path.join(base_dir, file)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                knowledge += f"\n\n### ARQUIVO: {file}\n{content}"

    return knowledge
