import json
import urllib.request
from datetime import date
import re

# 1. data de hoje
hoje = date.today().isoformat()
print("Data:", hoje)

# 2. endpoint da API
url = f"https://api-liturgia.edicoescnbb.com.br/contents/in/date/{hoje}"
print("URL:", url)

# 3. headers para parecer navegador
headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://liturgiadiaria.edicoescnbb.com.br/",
    "Origin": "https://liturgiadiaria.edicoescnbb.com.br",
    "Accept": "application/json"
}

# 4. monta request
req = urllib.request.Request(url, headers=headers)

try:
    # 5. baixa JSON
    with urllib.request.urlopen(req) as resposta:
        dados = json.load(resposta)

    # debug
    print("Chaves:", dados.keys())

    if "content" not in dados:
        print("Resposta inesperada:")
        print(dados)
        exit()

    # 6. pega HTML bruto
    body_html = dados["content"]["body"]

    # 7. salva HTML completo
    with open("liturgia.html", "w", encoding="utf-8") as arquivo:
        arquivo.write(body_html)

    print("Arquivo liturgia.html salvo")

    # 8. remove tags HTML → texto simples
    texto = re.sub(r"<[^>]+>", "", body_html)
    texto = re.sub(r"\n\s*\n", "\n\n", texto)

    # 9. salva texto limpo
    nome = f"liturgia-{hoje}.txt"

    with open(nome, "w", encoding="utf-8") as arquivo: arquivo.write(texto)

    print(f"Arquivo salvo: {nome}")

except Exception as e:
    print("Erro:", e)
