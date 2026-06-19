import type { ChatMessage } from '../types/chat'

const initialChatHistory: ChatMessage[] = [
  {
    id: '1',
    role: 'assistant',
    content: 'Olá! Sou seu assistente virtual. Como posso ajudar?',
    createdAt: new Date().toISOString(),
  },
  {
    id: '2',
    role: 'user',
    content: 'Quero entender como funciona um projeto React com IA.',
    createdAt: new Date().toISOString(),
  },
  {
    id: '3',
    role: 'assistant',
    content: 'Podemos construir um chat usando React no front-end e FastAPI com LangChain no back-end.',
    createdAt: new Date().toISOString(),
  },
]

let chatHistory: ChatMessage[] = [...initialChatHistory]

function delay(ms: number) {
    return new Promise((resolve) => setTimeout(resolve, ms))
}

export async function getChatHistory(): Promise<ChatMessage[]> {
    await delay(500)

    return [...chatHistory]
}

export async function sendMessageToAssistant(content: string): Promise<ChatMessage> {

    const userMessage: ChatMessage = {
        id: crypto.randomUUID(),
        role: 'user',
        content,
        createdAt: new Date().toISOString()
    }

    chatHistory = [...chatHistory, userMessage]

    await delay(800)

    const assistantMessage: ChatMessage = {
        id: crypto.randomUUID(),
        role: 'assistant',
        content: `Você disse "${userMessage.content}". Em breve essa resposta virá da API.`,
        createdAt: new Date().toISOString()
    }

    chatHistory = [...chatHistory, assistantMessage]

    return assistantMessage
}