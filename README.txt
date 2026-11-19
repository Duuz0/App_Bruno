API - TESTE DE CONSUMO DIGITAL

ARQUIVOS
- perguntas.py: API Python com Flask.
- index.html: interface conectada à API usando Fetch.
- requirements.txt: dependência necessária.

COMO EXECUTAR
1. Instale Python 3.
2. Abra o terminal na pasta deste projeto.
3. (Opcional, recomendado) Crie um ambiente virtual:
   python -m venv .venv

   Windows:
   .venv\Scripts\activate

   Linux/macOS:
   source .venv/bin/activate

4. Instale a dependência:
   pip install -r requirements.txt

5. Inicie o servidor:
   python perguntas.py

6. Abra no navegador:
   http://127.0.0.1:5000

IMPORTANTE
Não abra o index.html diretamente pelo arquivo. Acesse pelo endereço acima,
pois é o servidor Flask que disponibiliza a página e recebe as respostas.

ROTAS DA API
GET  /api/health     -> verifica se a API está online.
GET  /api/perguntas  -> retorna as 10 perguntas e opções em JSON.
POST /api/resultado  -> recebe as respostas e retorna pontuação/classificação.

EXEMPLO DE JSON PARA POST /api/resultado
{
  "respostas": {
    "q1": 1, "q2": 2, "q3": 3, "q4": 4, "q5": 1,
    "q6": 2, "q7": 3, "q8": 4, "q9": 1, "q10": 2
  }
}

A API valida se todas as 10 respostas foram enviadas e se cada valor está entre 1 e 4.
