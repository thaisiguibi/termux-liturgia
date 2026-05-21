# Liturgia Diária CNBB — Script para Termux

Script simples em Python para baixar automaticamente a liturgia diária da CNBB no Termux, usando apenas bibliotecas padrão do Python.

Projeto pensado para uso pessoal, educacional e pastoral.

---

# Funcionalidades

- Busca a liturgia do dia automaticamente
- Salva o conteúdo em `.txt`
- Remove HTML básico
- Funciona no Termux
- Não depende de bibliotecas externas

---

# Como funciona

O site da liturgia utiliza uma aplicação web que carrega os dados dinamicamente.

Observando as requisições públicas feitas pelo próprio frontend, foi possível identificar o endpoint utilizado para obter a liturgia diária.

O script utiliza esse mesmo endpoint público para baixar o conteúdo do dia.

Exemplo de endpoint:

https://api-liturgia.edicoescnbb.com.br/contents/in/date/YYYY-MM-DD

---

# Instalação no Termux

Atualizar pacotes:

pkg update && pkg upgrade

Instalar Python:

pkg install python -y

Clonar o repositório:

git clone https://github.com/SEU-USUARIO/SEU-REPO.git

Entrar na pasta:

cd SEU-REPO

Executar:

python main.py

---

# Script principal

import json
import re
import urllib.request
from datetime import date

hoje = date.today().isoformat()

url = f"https://api-liturgia.edicoescnbb.com.br/contents/in/date/{hoje}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

req = urllib.request.Request(url, headers=headers)

resposta = urllib.request.urlopen(req)

dados = json.load(resposta)

body_html = dados["content"]["body"]

texto = re.sub("<[^>]+>", "", body_html)

with open("liturgia.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(texto)

print("Liturgia salva em liturgia.txt")
```

---

# Estrutura do projeto

.
├── main.py
├── liturgia.txt
└── README.md

---

# Exemplo de saída

PRIMEIRA LEITURA

Vós recebestes o Espírito Santo quando abraçastes a fé?

Leitura dos Atos dos Apóstolos...
```

---

# Objetivo do projeto

Este projeto foi criado para facilitar o acesso à liturgia diária em ambientes simples, especialmente:
- celular Android com Termux;
- uso pessoal;
- apoio pastoral;
- leitura offline.

---

# Observações

- Conteúdo obtido a partir do endpoint público utilizado pelo próprio frontend da Liturgia Diária CNBB.
- O projeto não possui vínculo oficial com a CNBB.
- Uso recomendado de forma moderada e responsável.

---

# Possíveis melhorias futuras

- Geração automática diária

---

# Créditos

Fonte do conteúdo litúrgico:

---

# Licença

Uso livre para fins pessoais, educacionais e pastorais.
