const API_BASE_URL = import.meta.env.VITE_API_URL

if (!API_BASE_URL) {
    throw new Error("VITE_API_URL is not configured.")
}

type ApiRequestOptions = Omit<RequestInit, 'body'> & {
    body?: unknown
}

export async function apiRequest<T>(path: string, options: ApiRequestOptions = {}): Promise<T> {
    const headers = new Headers(options.headers)

    if (options.body !== undefined) {
        headers.set('Content-Type', 'application/json')
    }

    const response = await fetch(`${API_BASE_URL}${path}`, {
        ...options,
        headers,
        body:
            options.body !== undefined
            ? JSON.stringify(options.body)
            : undefined
    })

    if (!response.ok) {
        throw new Error(`API request failed with status ${response.status}`)
    }

    return response.json() as Promise<T>
}