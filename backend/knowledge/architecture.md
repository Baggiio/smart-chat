# Arquitetura do Smart Chat

O projeto é um monorepo simples com dois diretórios independentes: smart-chat para o front-end e backend para a API.

Durante o desenvolvimento, o front-end roda na porta 5173 e o FastAPI roda na porta 8000.

O front-end comunica-se com o back-end por HTTP REST. A URL da API é configurada pela variável VITE_API_URL.

O PostgreSQL com a extensão pgvector é executado com Docker Compose. Inicialmente, apenas o banco de dados está em container, enquanto front-end e back-end executam diretamente no ambiente de desenvolvimento.

O React Query é responsável pelo cache no cliente. O PostgreSQL será responsável pela persistência dos dados e dos vetores.