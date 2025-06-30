export interface Industry {
  [key: string]: string
}

export interface SalesStrategyResponse {
  success: boolean
  strategy?: string
  error?: string
  elapsed_time: number
  isStreaming?: boolean
  status?: string
} 