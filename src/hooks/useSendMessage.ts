import { useMutation, useQueryClient } from '@tanstack/react-query'
import { sendMessageToAssistant } from '../services/chatService'
import { chatHistoryQueryKey } from './chatQueryKeys'
import type { ChatMessage } from '../types/chat'

export function useSendMessage() {

    const queryClient = useQueryClient()

    return useMutation({
        mutationFn: sendMessageToAssistant,

        onMutate: async (content:string) => {
            await queryClient.cancelQueries({
                queryKey: chatHistoryQueryKey
            })

            const previousMessages = queryClient.getQueryData<ChatMessage[]>(
                chatHistoryQueryKey,
            ) ?? []

            const optimisticUserMessage: ChatMessage = {
                id: crypto.randomUUID(),
                role: 'user',
                content,
                createdAt: new Date().toISOString()
            }

            queryClient.setQueryData<ChatMessage[]>(
                chatHistoryQueryKey, (currentMessages = []) => [...currentMessages, optimisticUserMessage]
            )

            return { previousMessages }
        },

        onError: (_error, _content, onMutateResult) => {
            if (!onMutateResult) {
                return
            }

            queryClient.setQueryData(
                chatHistoryQueryKey,
                onMutateResult.previousMessages,
            )
        },

        onSettled: () => {
            return queryClient.invalidateQueries({
                queryKey: chatHistoryQueryKey
            })
        }
    })
}

