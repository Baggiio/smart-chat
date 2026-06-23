import type { ChatMessage } from '../types/chat'
import { apiRequest } from './api'

export async function getChatHistory(signal?: AbortSignal): Promise<ChatMessage[]> {
	return apiRequest<ChatMessage[]>('/api/messages', {signal})
}

export async function sendMessageToAssistant(content: string): Promise<ChatMessage> {
	return apiRequest<ChatMessage>('/api/messages', {
		method: 'POST',
		body: {
			content,
		}
	})
}