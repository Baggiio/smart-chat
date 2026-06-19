import React, { useState } from 'react'

type MessageInputProps = {
    onSendMessage: (message: string) => void,
    disabled: boolean
}

export function MessageInput({ onSendMessage, disabled }: MessageInputProps) {
    const [message, setMessage] = useState('')

    function handleSubmit(event: React.SubmitEvent<HTMLFormElement>) {
        event.preventDefault()

        const trimmedMessage = message.trim()

        if (!trimmedMessage) {
            return
        }

        onSendMessage(trimmedMessage)
        setMessage('')
    }

    return (
        <form onSubmit={handleSubmit} className="border-t border-zinc-800 bg-zinc-950 p-4">
            <div className="mx-auto flex max-w-3xl gap-2">
                <input value={message} onChange={(event) => setMessage(event.target.value)} placeholder="Digite sua mensagem..." disabled={disabled} className="flex-1 rounded-xl border border-zinc-700 bg-zinc-900 px-4 py-3 text-sm text-zinc-100 outline-none placeholder:text-zinc-500 focus:border-blue-500" />
                <button type="submit" disabled={disabled} className="rounded-xl bg-blue-600 px-5 py-3 text-sm font-medium text-white hover:bg-blue-500">Enviar</button>
            </div>
        </form>
    )
}