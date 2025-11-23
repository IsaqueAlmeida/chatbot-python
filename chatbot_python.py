""" Criando um ChatBot com a biblioteca ChatterBot em Python """

# Imortando todas as bilbiotecas necessárias
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Configurando o algoritmo sobre as informações de tempo e especifica
# as novas versões da linguagem python
import time
# import sys
time.clock = time

# Iniciando o treinamento do assistente virtual para perguntas e
# respostas simples, para que o diálogo tenha um ponto inicial
bot = ChatBot('Bot')
trainer = ListTrainer(bot)
conversa = ['Olá!', 'Tudo bem?', 'Que bom!', 'Como vai?',
            'Aconteceu algo?', 'O que aconteceu?',
            'Me fala sobre as novidades!',
            'Quer conversar hoje?',
            'Muito bem, vamos falar sobre o quê hoje?', 'Não quero!',
            'Não!', 'Não podemos conversar agora!',
            'Estou ocupado! Volte depois!']

# Construindo uma arquitetura de repetição para montar uma conversa
# entre a máquina e o usuário
# Treinando o bot
trainer.train(conversa)

# Loop principal do chatbot
while True:
    pergunta = input('Você: ').strip()
    # Normalizando para comparação de saída
    lower = pergunta.lower()

    # confere as palavras de saída
    if lower in ['tchau', 'adeus', 'até mais']:
        print('Bot: Até mais! Foi bom conversar com você.')
        break

    # Obtem respostas
    resposta = bot.get_response(pergunta)

    # converte confiança com segurança
    try:
        confidence = float(resposta.confidence)
    except Exception:
        confidence = 0.0
    
    if confidence > 0.5:
        print(f'Bot: {resposta}')
    else:
        print('Bot: Desculpe, não entendi sua pergunta. Pode reformular?')
