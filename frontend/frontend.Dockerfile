FROM node:18

WORKDIR /app

# Copia package.json e package-lock.json primeiro
COPY package*.json ./

# Instala TODAS as dependências, incluindo devDependencies
RUN npm install --legacy-peer-deps --include=dev

# Adiciona o PATH dos binários locais (onde o vite fica instalado)
ENV PATH="./node_modules/.bin:$PATH"

# Copia o resto do código
COPY . .

# Expoe a porta padrão do Vite
EXPOSE 5173

# Comando padrão (host liberado para acesso externo)
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
