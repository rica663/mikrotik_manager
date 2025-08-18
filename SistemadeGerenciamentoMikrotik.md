# Sistema de Gerenciamento Mikrotik

Este projeto visa criar um sistema de gerenciamento para dispositivos Mikrotik, com foco inicial no backend e infraestrutura.

## Estrutura do Projeto

```
mikrotik-manager/
├── backend/          # Django + DRF
├── frontend/         # React (Vite) - Fornecido pelo usuário
├── celery_tasks/     # Workers
└── infra/            # Docker compose
```

## Setup Inicial (Desenvolvimento)

1.  **Pré-requisitos:**
    *   Docker e Docker Compose instalados.
    *   Python 3.11 e pip instalados (para desenvolvimento local sem Docker).

2.  **Configuração do Ambiente:**

    Navegue até o diretório `mikrotik-manager/backend` e crie um arquivo `.env` com base no `.env.example`:

    ```bash
    cd mikrotik-manager/backend
    cp .env.example .env
    # Edite o arquivo .env com suas configurações, especialmente a SECRET_KEY
    ```

3.  **Executar com Docker Compose (Recomendado):**

    Navegue até o diretório `mikrotik-manager/infra` e execute:

    ```bash
    cd mikrotik-manager/infra
    docker-compose up --build
    ```

    Isso irá:
    *   Construir as imagens Docker para o backend e Celery.
    *   Iniciar os serviços de banco de dados (PostgreSQL), Redis, backend Django e worker Celery.

    Após a inicialização, o backend estará disponível em `http://localhost:8000`.

4.  **Executar Localmente (Alternativo - Apenas Backend):**

    Se você preferir rodar o backend localmente (sem Docker para o backend, mas ainda precisando de Redis e PostgreSQL):

    a.  **Inicie o Banco de Dados e Redis com Docker Compose:**

        Navegue até `mikrotik-manager/infra` e execute apenas os serviços de `db` e `redis`:

        ```bash
        cd mikrotik-manager/infra
        docker-compose up -d db redis
        ```

    b.  **Instale as dependências do Backend:**

        Navegue até o diretório `mikrotik-manager/backend` e instale as dependências:

        ```bash
        cd mikrotik-manager/backend
        pip install -r requirements.txt # Você precisará criar este arquivo
        ```

    c.  **Realize as Migrações do Banco de Dados:**

        ```bash
        python manage.py makemigrations
        python manage.py migrate
        ```

    d.  **Inicie o Servidor de Desenvolvimento Django:**

        ```bash
        python manage.py runserver
        ```

    e.  **Inicie o Worker Celery (em outro terminal):**

        ```bash
        celery -A mikrotik_manager_backend worker -l info
        ```

## Endpoints da API (DRF)

### Autenticação
*   `POST /api/auth/login/`: Login customizado (retorna user info + tokens)
*   `POST /api/auth/register/`: Registro de usuário
*   `POST /api/token/`: Obter token JWT (padrão DRF)
*   `POST /api/token/refresh/`: Renovar token JWT

### Dispositivos Mikrotik
*   `GET /api/devices/`: Listar todos os dispositivos (requer autenticação)
*   `POST /api/devices/`: Criar um novo dispositivo (requer autenticação)
*   `GET /api/devices/{id}/`: Obter detalhes de um dispositivo específico (requer autenticação)
*   `PUT /api/devices/{id}/`: Atualizar um dispositivo existente (requer autenticação)
*   `DELETE /api/devices/{id}/`: Excluir um dispositivo (requer autenticação)
*   `POST /api/devices/{id}/test_connection/`: Testar conexão com dispositivo (requer autenticação)

### Exemplo de Payload para Login

```json
{
  "username": "admin",
  "password": "senha123"
}
```

### Exemplo de Payload para Criar Dispositivo

```json
{
  "name": "Mikrotik Principal",
  "ip_address": "192.168.1.1",
  "api_port": 8728,
  "secret_ref": "vault_secret_ref_123",
  "status": "unknown"
}
```

## Acesso à Aplicação

Após executar o `docker-compose up --build -d`:

*   **Frontend:** http://localhost:3000 (agora com autenticação JWT)
*   **Backend API:** http://localhost:8000/api/
*   **Admin Django:** http://localhost:8000/admin/

### Primeiro Acesso

1. Crie um superusuário para acessar o sistema:
   ```bash
   docker-compose exec backend python manage.py createsuperuser
   ```

2. Acesse o frontend em http://localhost:3000 e faça login com as credenciais criadas.

## Próximos Passos

*   **Teste de Conexão Real com Mikrotik:** Melhorar a task de teste de conexão com tratamento de erros robusto
*   **Interface de Administração:** Dashboard com estatísticas e logs de atividades
*   **Portal de Convidados (Hotspot):** Interface mobile-first para usuários convidados
*   **Monitoramento em Tempo Real:** WebSockets e integração com InfluxDB
*   **Integração com HashiCorp Vault:** Armazenamento seguro de credenciais
*   **Funcionalidades Avançadas Mikrotik:** Configuração de firewall, DHCP, VPN


