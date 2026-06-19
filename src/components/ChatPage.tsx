import { useState } from 'react' 
import type { ChatMessage } from '../types/chat'
import { MessageInput } from './MessageInput'
import { MessageList } from './MessageList'
import { sendMessageToAssistant } from '../services/chatService'

const initialMessages: ChatMessage[] = [
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

export function ChatPage() {
    const [messages, setMessages] = useState<ChatMessage[]>(initialMessages)
    const [isAssistantTyping, setIsAssistantTyping] = useState(false)

    async function handleSendMessage(content: string) {
        const userMessage: ChatMessage = {
            id: crypto.randomUUID(),
            role: 'user',
            content,
            createdAt: new Date().toISOString()
        }

        setMessages((currentMessages) => [...currentMessages, userMessage])
        setIsAssistantTyping(true)

        try {
            const assistantMessage = await sendMessageToAssistant(content)

            setMessages((currentMessages) => [...currentMessages, assistantMessage])
        } catch {
            const errorMessage: ChatMessage = {
                id: crypto.randomUUID(),
                role: 'assistant',
                content: 'Não foi possível processar sua mensagem.',
                createdAt: new Date().toISOString()
            }

            setMessages((currentMessages) => [...currentMessages, errorMessage])
        } finally {
            setIsAssistantTyping(false)
        }
    }

    return (
        <main className="flex min-h-screen flex-col bg-zinc-950 text-zinc-100">
            <header className="border-b border-zinc-800 px-6 py-4">
                <div className="mx-auto max-w-3xl">
                    <h1 className="text-lg font-semibold">Smart Chat</h1>
                    <p className="text-sm text-zinc-400">
                        Assistente virtual com React, FastAPI e LangChain
                    </p>
                </div>
            </header>

            <section className="mx-auto flex w-full max-w-3xl flex-1 flex-col">
                <MessageList messages={messages} isAssistantTyping={isAssistantTyping} />
                <MessageInput onSendMessage={handleSendMessage} disabled={isAssistantTyping} />
            </section>
        </main>
    )
}