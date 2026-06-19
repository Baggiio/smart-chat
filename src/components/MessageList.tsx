import type { ChatMessage } from '../types/chat'
import { MessageBubble } from './MessageBubble'

type MessageListProps = {
    messages: ChatMessage[],
    isAssistantTyping: boolean
}

export function MessageList({ messages, isAssistantTyping }: MessageListProps) {
    return (
        <div className="flex-1 space-y-4 overflow-y-auto px-4 py-6">
            {messages.map((message) => (
                <MessageBubble key={message.id} message={message} />
            ))}

            {isAssistantTyping && (
                <div className="flex justify-start">
                    <div className="rounded-2xl bg-zinc-800 px-4 py-3 text-sm text-zinc-400">
                        ...
                    </div>
                </div>
            )}
        </div>
    )
}