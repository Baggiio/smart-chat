import { useMutation } from '@tanstack/react-query'
import { sendMessageToAssistant } from '../services/chatService'

export function useSendMessage() {
    return useMutation({
        mutationFn: sendMessageToAssistant
    })
}

