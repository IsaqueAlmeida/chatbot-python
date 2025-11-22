""" Criando um ChatBot com a biblioteca ChatterBot em Python """

# Imortando todas as bilbiotecas necessárias
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Configurando o algoritmo sobre as informações de tempo e especifica
# as novas versões da linguagem python
import time
import sys
time.clock = time.perf_counter
