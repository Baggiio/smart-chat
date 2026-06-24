# Front-end do Smart Chat

O front-end do Smart Chat utiliza React com TypeScript e foi criado com Vite.

A interface é dividida nos componentes ChatPage, MessageList, MessageBubble e MessageInput.

O MessageInput utiliza estado local com useState para controlar o texto digitado.

O histórico de mensagens é tratado como estado de servidor pelo TanStack Query. O hook useChatHistory utiliza useQuery para buscar mensagens, enquanto useSendMessage utiliza useMutation para enviar novas mensagens.

Durante o envio, o cache recebe uma atualização otimista. Caso a requisição falhe, o estado anterior do cache é restaurado.