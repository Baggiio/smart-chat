import type { ChatMessage } from '../types/chat'

type MessageBubbleProps = {
    message: ChatMessage
}

export function MessageBubble({ message }: MessageBubbleProps) {
    const isUser = message.role === 'user'

    return (
        <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
            <div className={`max-w-[75%] rounded-2xl px-4 text-sm leading-relaxed ${isUser ? 'bg-blue-600 text-white' : 'bg-zinc-800 text-zinc-100'}`}>
                {message.content}
            </div>
        </div>
    )
}