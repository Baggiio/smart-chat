# Back-end do Smart Chat

O back-end utiliza Python e FastAPI.

A aplicação separa suas responsabilidades entre routers, schemas, services, tools e core.

Os schemas Pydantic validam os contratos de entrada e saída. O router HTTP recebe a requisição e delega o processamento ao chat service.

O chat service coordena o histórico e chama o agent service. O agent service utiliza LangChain e um modelo OpenAI.

A rota GET /api/messages retorna o histórico. A rota POST /api/messages recebe uma nova mensagem e retorna a resposta do assistente.