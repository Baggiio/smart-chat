import { useMutation, useQueryClient } from '@tanstack/react-query'
import { sendMessageToAssistant } from '../services/chatService'
import { chatHistoryQueryKey } from './chatQueryKeys'

export function useSendMessage() {

    const queryClient = useQueryClient()

    return useMutation({
        mutationFn: sendMessageToAssistant,

        onSuccess: async () => {
            await queryClient.invalidateQueries({
                queryKey: chatHistoryQueryKey
            })
        }
    })
}

