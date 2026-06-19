import type { ChatMessage } from '../types/chat'

function delay(ms: number) {
    return new Promise((resolve) => setTimeout(resolve, ms))
}

export async function sendMessageToAssistant(content: string): Promise<ChatMessage> {
    await delay(800)

    return {
        id: crypto.randomUUID(),
        role: 'assistant',
        content: `Você disse "${content}". Em breve essa resposta virá da API.`,
        createdAt: new Date().toISOString()
    }
}