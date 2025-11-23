# README — ChatBot simples com ChatterBot

**Autor:** Isaque Almeida

---

## Descrição

Este README descreve, linha a linha, o código fornecido que cria um ChatBot simples usando a biblioteca **ChatterBot** em Python. Inclui também instruções de instalação, bibliotecas necessárias, como rodar o projeto, análise de pontos problemáticos do código original, uma versão corrigida pronta para uso e sugestões de melhorias.

---

## Sumário

* O que o projeto faz
* Requisitos
* Instalação passo a passo
* Como executar
* Explicação linha a linha do código original
* Versão corrigida e comentada do script
* Arquivo `requirements.txt` sugerido
* Boas práticas e observações finais

---

## O que este projeto faz

O script é um protótipo de chatbot para console que usa o ChatterBot. Ele treina o bot a partir de uma lista de frases (ListTrainer) e então mantém um loop de interação com o usuário no terminal. É útil para estudos e protótipos, não recomendado para produção.

---

## Requisitos

* Python 3.8 ou 3.9 (recomendado). Algumas versões mais recentes podem ter problemas de compatibilidade com dependências do ChatterBot.
* pip
* Ambiente virtual (recomendado: `venv`)

### Bibliotecas utilizadas

* `chatterbot` — núcleo do chatbot
* `chatterbot_corpus` — (opcional) corpus para treinos mais ricos
* `time` — módulo padrão do Python (usado no código original de forma insegura)

> Observação: o ChatterBot historicamente possui incompatibilidades com versões recentes do Python e com algumas dependências nativas. Se encontrar erros de instalação, tente Python 3.8/3.9.

---

## Instalação (passo a passo)

1. Crie e ative um ambiente virtual (recomendado):

```bash
python3 -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# Windows (cmd)
venv\Scripts\activate.bat
```

2. Atualize o pip:

```bash
pip install --upgrade pip
```

3. Instale as dependências sugeridas (versões recomendadas):

```bash
pip install chatterbot==1.0.8 chatterbot_corpus python-Levenshtein
```

Se houver erro ao instalar `python-Levenshtein`, tente instalar `wheel` e `build-essential` (Linux) ou os componentes de build do Windows.

---

## Como executar

1. Salve o script (veja seção da versão corrigida) em um arquivo `chatbot.py`.
2. Ative o ambiente virtual.
3. Execute:

```bash
python chatbot.py
```

4. Interaja no terminal: digite mensagens e pressione Enter. Para sair, digite `Tchau`, `Adeus` ou `Até mais`.

---

## Código original (fornecido pelo usuário)

```python
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
```

---

## Explicação linha a linha (comentários e problemas)

Abaixo eu comento bloco a bloco e indico pontos de atenção e correções.

### Header / Docstring

```python
""" Criando um ChatBot com a biblioteca ChatterBot em Python """
```

* Apenas um comentário explicando o propósito do script. OK.

### Imports do ChatterBot

```python
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
```

* Importa o mecanismo principal `ChatBot` e o treinador `ListTrainer`.
* Observação:  a API do ChatterBot pode variar por versão; use a documentação correspondente.

### Import do time e atribuição problemática

```python
import time
# import sys
time.clock = time.perf_counter
```

* **Problema:** `time.clock` foi removido em Python 3.8; sobrescrever atributos do módulo `time` é uma prática insegura. Essa linha tenta contornar incompatibilidade, mas pode causar erros ou comportamento indefinido.
* **Correção:** Remover essa atribuição. Use `time.perf_counter()` ou `time.time()` diretamente quando precisar de medições.

### Criação do bot e treinamento

```python
bot = ChatBot('Bot')
conversa = ListTrainer(bot)
conversa.train([...])
```

* `ChatBot('Bot')` cria instância com o nome 'Bot'. Por padrão, o ChatterBot cria/adota um adaptador de armazenamento (SQLite) que persistirá frases aprendidas.
* `ListTrainer(bot)` cria um treinador simples. `train()` com uma lista considera que cada item é uma resposta ao anterior, portanto a lista deve representar uma conversa lógica (pergunta → resposta). Na versão original, as frases não estão perfeitamente pareadas, o que reduz a qualidade do aprendizado.

### Loop principal

```python
while True:
    pergunta = input('Você: ')
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print(f'Bot: {resposta}')
    else:
        print('Bot: Desculpe! Não entendi!')

    if pergunta == (['Tchau', 'Adeus', 'Até mais']):
        break
```

* `pergunta = input('Você: ')` lê o texto do usuário.
* `bot.get_response(pergunta)` retorna um objeto `Response` com atributos `text` e `confidence`.
* `resposta.confidence` é um float entre 0 e 1 (às vezes comportamento depende do training). Comparar > 0.5 é uma prática comum.
* **Erro lógico ao verificar saída:** `pergunta == (['Tchau', 'Adeus', 'Até mais'])` compara string com lista; isso sempre será `False`. O correto é `if pergunta in ['Tchau', 'Adeus', 'Até mais']:` (e normalizar com `.strip().lower()` para robustez).

---

## Versão corrigida e comentada do script (recomendada)

Salve como `chatbot.py`.

```python
"""
chatbot.py
Versão corrigida do ChatBot com ChatterBot.
Autor: Isaque Almeida
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Nota: não sobrescreva funções em time. Use time.perf_counter diretamente quando precisar.
import time

# === Configuração do ChatBot ===
bot = ChatBot(
    'Bot',
    # Aqui você pode adicionar configurações, por exemplo:
    # storage_adapter='chatterbot.storage.SQLStorageAdapter',
    # database_uri='sqlite:///database.sqlite3'
)

# Treinamento (pares mais coerentes — pergunta e resposta)
trainer = ListTrainer(bot)
conversa = [
    'Olá!', 'Olá! Como posso ajudar?',
    'Tudo bem?', 'Estou bem, obrigado. E você?',
    'Como vai?', 'Vou bem. Em que posso ajudar hoje?',
    'Não quero!', 'Tudo bem — se quiser conversar depois, estarei aqui.',
    'Tchau', 'Até logo!'
]
# Treina o bot
trainer.train(conversa)

print("Chat iniciado. Digite 'Tchau', 'Adeus' ou 'Até mais' para sair.")

# Loop principal
while True:
    pergunta = input('Você: ').strip()
    # Normaliza para comparação de saída
    lower = pergunta.lower()

    # Confere palavras de saída
    if lower in ['tchau', 'adeus', 'até mais', 'ate mais']:
        print('Bot: Até logo!')
        break

    # Obtem resposta
    resposta = bot.get_response(pergunta)

    # Converte confiança com segurança
    try:
        confidence = float(resposta.confidence)
    except Exception:
        confidence = 0.0

    if confidence > 0.5:
        print(f'Bot: {resposta}')
    else:
        print('Bot: Desculpe! Não entendi. Pode reformular?')
```

### O que foi melhorado

* Remoção do hack com `time.clock`.
* Normalização da entrada do usuário para verificação de saída.
* Treino com pares coerentes (melhora a qualidade das respostas).
* Tratamento seguro de `confidence`.

---

## Arquivo `requirements.txt` sugerido

```
chatterbot==1.0.8
chatterbot_corpus
python-Levenshtein
```

Instale com:

```bash
pip install -r requirements.txt
```

---

## Observações finais, limitações e boas práticas

* **Versão do Python:** Caso encontre problemas na instalação, use Python 3.8 ou 3.9.
* **Ambiente virtual:** Sempre trabalhe com virtualenv/venv para isolar dependências.
* **Persistência:** O ChatterBot cria um banco (SQLite por padrão). Se quiser recomeçar, delete o arquivo do banco.
* **Produção:** ChatterBot é adequado para protótipos. Para produção, prefira arquiteturas com serviços mais robustos (APIs, modelos transformer, etc.).
* **Treinamento:** Quanto melhores os pares (pergunta/resposta), melhor o bot.

---

## Próximos passos (opcionais)

* Gerar `run.sh` ou `run.bat` para facilitar execução.
* Treinar com `chatterbot_corpus` (ex.: `trainer.train("chatterbot.corpus.portuguese")`).
* Criar frontend simples com Flask ou Streamlit para transformar o bot de console em chat web.

---

## Licença

MIT License

---

Se quiser, eu gero automaticamente o `requirements.txt`, o `run.sh` e um `Dockerfile` simples para empacotar o bot. Quer que eu gere esses arquivos também?
