from flask import Flask, jsonify, request, send_from_directory
from pathlib import Path

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent

# Cada resposta vale de 1 a 4 pontos.
PERGUNTAS = [
    {
        "id": 1,
        "texto": "Quanto tempo por dia você passa rolando feeds de redes sociais?",
        "opcoes": [
            "Menos de 30 min",
            "Entre 30 min e 2h",
            "Entre 2 a 4 horas",
            "Mais de 4 horas",
        ],
    },
    {
        "id": 2,
        "texto": "Qual é o seu primeiro hábito ao acordar?",
        "opcoes": [
            "Levanto, tomo café ou faço outras tarefas antes de pegar o celular",
            "Checo apenas mensagens urgentes ou previsão do tempo",
            "Abro redes sociais ou notícias na cama por alguns minutos",
            "Fico mais de 20 min consumindo conteúdo antes de levantar",
        ],
    },
    {
        "id": 3,
        "texto": "Quantas horas de vídeo (YouTube, streaming, lives) você assiste diariamente?",
        "opcoes": [
            "Menos de 1 hora",
            "Entre 1 e 2 horas",
            "Entre 2 e 4 horas",
            "Mais de 4 horas ou deixo rodando o dia todo",
        ],
    },
    {
        "id": 4,
        "texto": "Com que frequência você consome conteúdos de áudio (podcasts, músicas)?",
        "opcoes": [
            "Raramente ou apenas em viagens longas",
            "Algumas vezes na semana",
            "Todos os dias, em momentos específicos (trânsito/academia)",
            "O tempo todo, enquanto trabalho, estudo e faço tarefas",
        ],
    },
    {
        "id": 5,
        "texto": "Como é a sua rotina de leitura de notícias, artigos ou newsletters?",
        "opcoes": [
            "Leio apenas quando algo muito importante acontece",
            "Leio um resumo diário ou semanal",
            "Acesso sites de notícias e newsletters várias vezes ao dia",
            "Acompanho atualizações em tempo real o dia inteiro",
        ],
    },
    {
        "id": 6,
        "texto": "Você costuma consumir mais de um conteúdo ao mesmo tempo?",
        "opcoes": [
            "Nunca, prefiro focar em uma coisa de cada vez",
            "Raramente, apenas durante intervalos comerciais",
            "Com frequência, especialmente quando o programa está entediante",
            "Quase sempre, preciso de estímulos simultâneos",
        ],
    },
    {
        "id": 7,
        "texto": "Como você usa o celular durante as refeições?",
        "opcoes": [
            "Não uso, deixo o aparelho longe da mesa",
            "Deixo na mesa, mas só olho se tocar",
            "Assisto a vídeos ou leio algo quando estou comendo sozinho",
            "Sempre consumo conteúdo, mesmo acompanhado",
        ],
    },
    {
        "id": 8,
        "texto": "Qual é a sua relação com vídeos curtos (Reels, TikTok, Shorts)?",
        "opcoes": [
            "Não assisto ou não tenho esses aplicativos",
            "Assisto ocasionalmente por alguns minutos",
            "Assisto todos os dias e às vezes perco a noção do tempo",
            "Passo horas deslizando a tela continuamente",
        ],
    },
    {
        "id": 9,
        "texto": "O que você costuma fazer nos últimos 30 minutos antes de dormir?",
        "opcoes": [
            "Leio livro físico, medito ou descanso longe de telas",
            "Coloco música calma ou podcast com temporizador",
            "Dou uma última olhada rápida nas redes sociais",
            "Fico navegando na internet até pegar no sono com o celular",
        ],
    },
    {
        "id": 10,
        "texto": "Como você se sente quando fica sem acesso à internet ou celular por algumas horas?",
        "opcoes": [
            "Tranquilo e aliviado por ter tempo desconectado",
            "Normal, apenas sinto falta se precisar comunicar alguém",
            "Um pouco entediado e curioso para saber o que perdi",
            "Ansioso, inquieto e com sensação de estar por fora",
        ],
    },
]


def classificar(resultado):
    if 10 <= resultado <= 16:
        return {
            "nivel": "Consumo Baixo (Equilibrado)",
            "descricao": "Você tem ótimo controle sobre seu tempo de tela e prioriza atividades offline.",
        }
    if 17 <= resultado <= 24:
        return {
            "nivel": "Consumo Moderado",
            "descricao": "Você usa a internet de forma saudável no dia a dia, mas já tem alguns hábitos automáticos.",
        }
    if 25 <= resultado <= 32:
        return {
            "nivel": "Consumo Alto",
            "descricao": "Grande parte do seu tempo livre é ocupada por telas, o que pode gerar cansaço mental.",
        }
    return {
        "nivel": "Consumo Muito Alto (Hiperconectado)",
        "descricao": "O consumo digital domina sua rotina e pode estar afetando seu sono, foco e bem-estar.",
    }


@app.get("/")
def pagina_inicial():
    return send_from_directory(BASE_DIR, "index.html")


@app.get("/api/perguntas")
def obter_perguntas():
    """Retorna as perguntas para qualquer cliente que consumir a API."""
    return jsonify({
        "total": len(PERGUNTAS),
        "pontuacao_minima": 10,
        "pontuacao_maxima": 40,
        "perguntas": PERGUNTAS,
    })


@app.post("/api/resultado")
def calcular_resultado():
    """Recebe { respostas: { q1: 1, ..., q10: 4 } } e devolve o resultado."""
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict) or not isinstance(dados.get("respostas"), dict):
        return jsonify({
            "erro": "Envie um JSON no formato {\"respostas\":{\"q1\":1,...,\"q10\":4}}."
        }), 400

    respostas = dados["respostas"]
    esperadas = {f"q{i}" for i in range(1, 11)}
    recebidas = set(respostas.keys())

    faltantes = sorted(esperadas - recebidas)
    extras = sorted(recebidas - esperadas)

    if faltantes:
        return jsonify({
            "erro": "Responda todas as 10 perguntas.",
            "perguntas_faltantes": faltantes,
        }), 400

    if extras:
        return jsonify({"erro": "Foram enviadas perguntas inválidas.", "extras": extras}), 400

    respostas_validas = {}
    for chave in esperadas:
        valor = respostas[chave]
        # bool é subclasse de int em Python; por isso é rejeitado explicitamente.
        if isinstance(valor, bool) or not isinstance(valor, int) or valor not in (1, 2, 3, 4):
            return jsonify({
                "erro": f"A resposta de {chave} deve ser um número inteiro entre 1 e 4."
            }), 400
        respostas_validas[chave] = valor

    pontuacao = sum(respostas_validas.values())
    classificacao = classificar(pontuacao)

    return jsonify({
        "pontuacao": pontuacao,
        "pontuacao_maxima": 40,
        "nivel": classificacao["nivel"],
        "descricao": classificacao["descricao"],
        "respostas_recebidas": len(respostas_validas),
    })


@app.get("/api/health")
def verificar_api():
    return jsonify({"status": "online", "mensagem": "API de Consumo Digital funcionando."})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
