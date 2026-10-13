import json

dados = {"nome":"Bruno", "idade": 28}

with open ("dados.json", "w",
           encoding="utf-8") as f:
    json.dump(dados, f,
              ensure_ascii=False,
              indent=2)