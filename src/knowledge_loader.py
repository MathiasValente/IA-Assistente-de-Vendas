import os


def load_knowledge():
    base_dir = os.path.join(os.getcwd(), "knowledge")

    # Preferência de ordem quando possível
    preferred = [
        "transcricao-live-fys",
        "produtos",
        "perguntas-frequentes",
        "objecoes",
        "contexto-do-negocio",
    ]

    files = []

    # Tenta encontrar arquivos preferidos com .md ou .txt
    for name in preferred:
        for ext in (".md", ".txt"):
            p = os.path.join(base_dir, name + ext)
            if os.path.exists(p):
                files.append(os.path.basename(p))
                break

    # Adiciona quaisquer outros .md/.txt presentes, mantendo ordem
    if os.path.isdir(base_dir):
        for f in sorted(os.listdir(base_dir)):
            if f.endswith((".md", ".txt")) and f not in files:
                files.append(f)

    knowledge = ""

    for file in files:
        path = os.path.join(base_dir, file)
        try:
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()
                knowledge += f"\n\n### ARQUIVO: {file}\n{content}"
        except Exception:
            # Ignora arquivos que não possam ser lidos
            continue

    return knowledge
