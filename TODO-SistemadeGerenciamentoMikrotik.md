# TODO - Sistema de Gerenciamento Mikrotik

## Status Atual do Projeto

O projeto está na fase inicial de desenvolvimento com os módulos mínimos implementados para permitir o início do desenvolvimento e integração entre frontend e backend.

### ✅ Concluído

#### Backend (Django + DRF)
- [x] Projeto Django criado com estrutura básica
- [x] Aplicativo `devices` implementado
- [x] Modelo `MikrotikDevice` definido com campos essenciais:
  - `name`: Nome do dispositivo
  - `ip_address`: Endereço IP do dispositivo
  - `api_port`: Porta da API (padrão 8728)
  - `secret_ref`: Referência para credenciais no Vault
  - `status`: Status do dispositivo (online/offline/unknown)
- [x] Serializers DRF para o modelo MikrotikDevice
- [x] ViewSet com operações CRUD completas
- [x] URLs configuradas para API REST
- [x] Configuração CORS para permitir acesso do frontend
- [x] Configuração PostgreSQL para produção
- [x] Migrações do banco de dados executadas

#### Celery e Redis
- [x] Configuração do Celery para processamento assíncrono
- [x] Redis configurado como broker
- [x] Task `test_mikrotik_connection` implementada (básica)
- [x] Task `create_hotspot_user` implementada (placeholder)
- [x] Integração com librouteros para comunicação Mikrotik

#### Infraestrutura
- [x] Docker Compose configurado com todos os serviços:
  - PostgreSQL (banco de dados)
  - Redis (broker Celery)
  - Backend Django
  - Worker Celery
  - Frontend React
- [x] Dockerfiles criados para backend e frontend
- [x] Volumes configurados para persistência de dados
- [x] Variáveis de ambiente organizadas

#### Frontend (React + TypeScript)
- [x] Projeto Vite + React + TypeScript configurado
- [x] Interface básica para listar dispositivos
- [x] Formulário para adicionar novos dispositivos
- [x] Integração com API backend via Axios
- [x] Proxy configurado para comunicação com backend
- [x] Estilização básica com Tailwind CSS

#### Documentação
- [x] README.md com instruções de setup
- [x] Arquivo .env.example com variáveis necessárias
- [x] Exemplos de payloads da API
- [x] Comandos para execução local e Docker

### 🔄 Em Desenvolvimento / Próximos Passos

#### Funcionalidades Essenciais (Prioridade Alta)
- [x] **Autenticação JWT**
  - [x] Implementar sistema de login/logout
  - [x] Proteger rotas da API
  - [x] Contexto de autenticação no frontend
  - [x] Middleware de autenticação
  - [x] Views customizadas de login e registro
  - [x] Configuração JWT com refresh tokens
  - [x] Interface de login no frontend
  - [x] Gerenciamento de estado de autenticação
  - [x] Interceptação de requisições com token JWT

- [ ] **Teste de Conexão Real com Mikrotik**
  - Melhorar a task `test_mikrotik_connection`
  - Implementar tratamento de erros robusto
  - Validação de credenciais
  - Timeout e retry logic

- [ ] **Interface de Administração**
  - Dashboard com estatísticas básicas
  - Logs de atividades
  - Gerenciamento de usuários
  - Configurações do sistema

#### Funcionalidades Intermediárias (Prioridade Média)
- [ ] **Portal de Convidados (Hotspot)**
  - Interface mobile-first
  - Registro de usuários convidados
  - Geração de credenciais temporárias
  - Redirecionamento pós-autenticação

- [ ] **Monitoramento em Tempo Real**
  - WebSockets para status ao vivo
  - Atualização automática de status dos dispositivos
  - Notificações de eventos importantes

- [ ] **Melhorias na Interface**
  - Componentes UI mais robustos
  - Validação de formulários
  - Feedback visual para ações
  - Responsividade aprimorada

#### Funcionalidades Avançadas (Prioridade Baixa)
- [ ] **Integração com HashiCorp Vault**
  - Armazenamento seguro de credenciais
  - Rotação automática de senhas
  - Auditoria de acesso

- [ ] **Histórico e Analytics**
  - Integração com InfluxDB
  - Gráficos de performance
  - Relatórios de uso
  - Métricas de rede

- [ ] **Funcionalidades Avançadas Mikrotik**
  - Configuração de firewall
  - Gerenciamento de DHCP
  - Configuração de VPN
  - Backup e restore de configurações

### 🚧 Problemas Conhecidos

1. **Docker no Ambiente Sandbox**: Não foi possível testar completamente o Docker Compose no ambiente de desenvolvimento devido a problemas de inicialização do serviço Docker.

2. **Credenciais Hardcoded**: As credenciais do banco de dados estão hardcoded no docker-compose.yml. Deve ser movido para variáveis de ambiente em produção.

3. **Segurança**: O sistema atual não possui autenticação, todas as rotas estão abertas.

### 📋 Como Continuar o Desenvolvimento

#### Para Desenvolvedores que Assumirem o Projeto:

1. **Setup Local**:
   ```bash
   cd mikrotik-manager/infra
   docker-compose up --build -d
   ```

2. **Verificar Funcionamento**:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000/api/devices/
   - Admin Django: http://localhost:8000/admin/

3. **Próxima Tarefa Recomendada**: Implementar autenticação JWT
   - Instalar `djangorestframework-simplejwt`
   - Configurar endpoints de login/logout
   - Proteger rotas da API
   - Implementar contexto de autenticação no React

4. **Estrutura de Arquivos Importantes**:
   ```
   backend/
   ├── devices/models.py          # Modelo MikrotikDevice
   ├── devices/views.py           # ViewSets da API
   ├── devices/tasks.py           # Tasks Celery
   └── mikrotik_manager_backend/settings.py  # Configurações Django
   
   frontend/src/
   ├── App.tsx                    # Componente principal
   └── main.tsx                   # Entry point
   ```

### 🔧 Comandos Úteis

```bash
# Executar migrações
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate

# Criar superusuário
docker-compose exec backend python manage.py createsuperuser

# Ver logs
docker-compose logs backend
docker-compose logs celery_worker

# Parar serviços
docker-compose down

# Rebuild completo
docker-compose down -v
docker-compose up --build -d
```

### 📝 Notas Técnicas

- **Banco de Dados**: PostgreSQL configurado, mas pode usar SQLite para desenvolvimento local
- **Celery**: Configurado com Redis, tasks prontas para expansão
- **CORS**: Configurado para permitir acesso de qualquer origem (ajustar em produção)
- **Frontend**: Vite com hot reload, proxy configurado para API
- **Dependências**: Todas listadas em requirements.txt e package.json

### 🎯 Objetivos de Longo Prazo

1. **Escalabilidade**: Suportar centenas de dispositivos Mikrotik
2. **Confiabilidade**: Sistema robusto com tratamento de falhas
3. **Segurança**: Implementação completa de segurança e auditoria
4. **Usabilidade**: Interface intuitiva para administradores e usuários finais
5. **Manutenibilidade**: Código bem documentado e testado

---

**Última Atualização**: Dezembro 2024  
**Versão**: 0.1.0 (MVP Inicial)  
**Status**: Desenvolvimento Ativo

