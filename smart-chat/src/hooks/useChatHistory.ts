import { useQuery } from '@tanstack/react-query'

import { getChatHistory } from '../services/chatService'
import { chatHistoryQueryKey } from './chatQueryKeys'

export function useChatHistory() {
    return useQuery({
        queryKey: chatHistoryQueryKey,
        queryFn: ({ signal }) => getChatHistory(signal)
    })
}