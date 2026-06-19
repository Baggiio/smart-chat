import { MessageInput } from './MessageInput'
import { MessageList } from './MessageList'
import { useSendMessage } from '../hooks/useSendMessage'
import { useChatHistory } from '../hooks/useChatHistory'

export function ChatPage() {

    const chatHistoryQuery = useChatHistory()
    const sendMessageMutation = useSendMessage()

    function handleSendMessage(content: string) {
        sendMessageMutation.mutate(content)
    }

    const messages = chatHistoryQuery.data ?? []

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
                {chatHistoryQuery.isPending ? (
                    <div className='flex flex-1 items-center justify-center'>
                        <p className='text-sm text-zinc-400'>
                            Carregando Histórico...
                        </p>
                    </div>
                ) : chatHistoryQuery.isError ? (
                    <div className='flex flex-1 flex-col items-center justify-center gap-3'>
                        <p className='text-sm text-red-400'>
                            Não foi possível carregar o histórico.
                        </p>

                        <button type='button' onClick={() => chatHistoryQuery.refetch()} className='rounded-lg bg-zinc-800 px-4 py-2 text-sm hover:bg-zinc-700'>
                            Tentar novamente
                        </button>
                    </div>
                ) : (
                    <MessageList messages={messages} isAssistantTyping={sendMessageMutation.isPending} />
                )}

                {sendMessageMutation.isError && (
                    <p className='px-4 pb-2 text-center text-sm text-red-400'>
                        Não foi possível enviar a mensagem. Tente novamente.
                    </p>
                )}

                <MessageInput onSendMessage={handleSendMessage} disabled={sendMessageMutation.isPending || chatHistoryQuery.isPending || chatHistoryQuery.isError} />
            </section>
        </main>
    )
}