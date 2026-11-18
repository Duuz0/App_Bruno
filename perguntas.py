# Função que apenas retorna a resposta do usuário
def somar_pontos(resposta):
    return resposta

# Lista com todas as perguntas e opções
perguntas = [
    (
        "1. Quanto tempo por dia você passa rolando feeds de redes sociais?",
        ["Menos de 30 min", "Entre 30 min e 2h", "Entre 2 a 4 horas", "Mais de 4 horas"]
    ),
    (
        "2. Qual é o seu primeiro hábito ao acordar?",
        ["Levanto, tomo café ou faço outras tarefas antes de pegar o celular", "Checo apenas mensagens urgentes ou previsão do tempo", "Abro redes sociais ou notícias na cama por alguns minutos", "Fico mais de 20 min consumindo conteúdo antes de levantar"]
    ),
    (
        "3. Quantas horas de vídeo (YouTube, streaming, lives) você assiste diariamente?",
        ["Menos de 1 hora", "Entre 1 e 2 horas", "Entre 2 e 4 horas", "Mais de 4 horas ou deixo rodando o dia todo"]
    ),
    (
        "4. Com que frequência você consome conteúdos de áudio (podcasts, músicas)?",
        ["Raramente ou apenas em viagens longas", "Algumas vezes na semana", "Todos os dias, em momentos específicos (trânsito/academia)", "O tempo todo, enquanto trabalho, estudo e faço tarefas"]
    ),
    (
        "5. Como é a sua rotina de leitura de notícias, artigos ou newsletters?",
        ["Leio apenas quando algo muito importante acontece", "Leio um resumo diário ou semanal", "Acesso sites de notícias e newsletters várias vezes ao dia", "Acompanho atualizações em tempo real o dia inteiro"]
    ),
    (
        "6. Você costuma consumir mais de um conteúdo ao mesmo tempo (ex: mexer no celular enquanto vê TV)?",
        ["Nunca, prefiro focar em uma coisa de cada vez", "Raramente, apenas durante intervalos comerciais", "Com frequência, especialmente quando o programa está entediante", "Quase sempre, preciso de estímulos simultâneos"]
    ),
    (
        "7. Como você usa o celular durante as refeições?",
        ["Não uso, deixo o aparelho longe da mesa", "Deixo na mesa, mas só olho se tocar", "Assisto a vídeos ou leio algo quando estou comendo sozinho", "Sempre consumo conteúdo, mesmo acompanhado"]
    ),
    (
        "8. Qual é a sua relação com vídeos curtos (Reels, TikTok, Shorts)?",
        ["Não assisto ou não tenho esses aplicativos", "Assisto ocasionalmente por alguns minutos", "Assisto todos os dias e às vezes perco a noção do tempo", "Passo horas deslizando a tela continuamente"]
    ),
    (
        "9. O que você costuma fazer nos últimos 30 minutos antes de dormir?",
        ["Leio livro físico, medito ou descanso longe de telas", "Coloco música calma ou podcast com temporizador", "Dou uma última olhada rápida nas redes sociais", "Fico navegando na internet até pegar no sono com o celular"]
    ),
    (
        "10. Como você se sente quando fica sem acesso à internet ou celular por algumas horas?",
        ["Tranquilo e aliviado por ter tempo desconectado", "Normal, apenas sinto falta se precisar comunicar alguém", "Um pouco entediado e curioso para saber o que perdi", "Ansioso, inquieto e com sensação de estar 'por fora'"]
    )
]

resultado = 0

print("=== QUIZ: QUAL É O SEU NÍVEL DE CONSUO DIGITAL? ===\n")

# Loop para rodar todas as perguntas automaticamente
for i, (pergunta, opcoes) in enumerate(perguntas, start=1):
    print(pergunta)
    for index, opcao in enumerate(opcoes, start=1):
        print(f"  {index} - {opcao}")
    
    # Validação simples para garantir que o usuário digite de 1 a 4
    while True:
        try:
            r = int(input("\nSua escolha (1-4): "))
            if 1 <= r <= 4:
                break
            print("Por favor, digite um número entre 1 e 4.")
        except ValueError:
            print("Entrada inválida. Digite apenas o número da opção.")
            
    resultado += somar_pontos(r)
    print("-" * 40)

# Lógica para exibir a faixa de resultado baseada na pontuação total
print("\n=== RESULTADO FINAL ===")
print(f"Sua pontuação total: {resultado} de 40 pontos\n")

if 10 <= resultado <= 16:
    print("Nível: Consumo Baixo (Equilibrado)")
    print("Descrição: Você tem ótimo controle sobre seu tempo de tela e prioriza atividades offline.")
elif 17 <= resultado <= 24:
    print("Nível: Consumo Moderado")
    print("Descrição: Você usa a internet de forma saudável no dia a dia, mas já tem alguns hábitos automáticos.")
elif 25 <= resultado <= 32:
    print("Nível: Consumo Alto")
    print("Descrição: Grande parte do seu tempo livre é ocupada por telas, o que pode gerar cansaço mental.")
else:
    print("Nível: Consumo Muito Alto (Hiperconectado)")
    print("Descrição: O consumo digital domina sua rotina e pode estar afetando seu sono, foco e bem-estar.")