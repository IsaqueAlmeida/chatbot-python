""" Criando um ChatBot com a biblioteca ChatterBot em Python """

# Imortando todas as bilbiotecas necessárias
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Configurando o algoritmo sobre as informações de tempo e especifica
# as novas versões da linguagem python
import time
# import sys
time.clock = time.perf_counter

# Iniciando o treinamento do assistente virtual para perguntas e
# respostas simples, para que o diálogo tenha um ponto inicial
bot = ChatBot('Bot')
conversa = ListTrainer(bot)
conversa.train(['Olá!', 'Tudo bem?', 'Que bom!', 'Como vai?',
                'Aconteceu algo?',
                'O que aconteceu?', 'Me fala sobre as novidades!',
                'Quer conversar hoje?',
                'Muito bem, vamos falar sobre o quê hoje?', 'Não quero!',
                'Não!', 'Não podemos conversar agora!',
                'Estou ocupado! Volte depois!'])

# Construindo uma arquitetura de repetição para montar uma conversa
# entre a máquina e o usuário
while True:
    pergunta = input('Você: ')
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print(f'Bot: {resposta}')
    else:
        print('Bot: Desculpe! Não entendi!')

    if pergunta == (['Tchau', 'Adeus', 'Até mais']):
        break
