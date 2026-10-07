# 1. Usando a variante slim para reduzir tamanho e vulnerabilidades
FROM python:3.14-slim

# 2. Atualizar o sistema
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 3. Copiar apenas o requirements.txt
COPY requirements.txt .

# 4. Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar o código
COPY . .

# 6. Remover o pip da imagem final
RUN rm -rf /usr/local/lib/python3.14/site-packages/pip \
           /usr/local/bin/pip \
           /usr/local/bin/pip3

CMD ["python", "main.py"]