# 1. Usando a versão mais atual e a variante "slim" para reduzir tamanho e vulnerabilidades
FROM python:3.14-slim

# 2. Atualizar o sistema logo no início. 
# 'rm -rf /var/lib/apt/lists/*' no final, é uma boa prática para apagar os ficheiros temporários do apt-get e deixar a imagem ainda menor.
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 3. Copiar APENAS o requirements.txt
COPY requirements.txt .

# 4. Instalar as dependências do Python.
RUN pip install --no-cache-dir -r requirements.txt

# 5. copiar o restante do código (main.py, etc.)
COPY . .

CMD ["python", "main.py"]