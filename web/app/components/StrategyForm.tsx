'use client'

import { motion } from 'framer-motion'
import { ChartBarIcon } from '@heroicons/react/24/outline'
import { Industry, SalesStrategyResponse } from './types'

interface StrategyFormProps {
  industries: Industry
  selectedIndustry: string
  setSelectedIndustry: (industry: string) => void
  client: string
  setClient: (client: string) => void
  region: string
  setRegion: (region: string) => void
  loading: boolean
  setLoading: (loading: boolean) => void
  setResult: (result: SalesStrategyResponse | null) => void
}

export default function StrategyForm({
  industries,
  selectedIndustry,
  setSelectedIndustry,
  client,
  setClient,
  region,
  setRegion,
  loading,
  setLoading,
  setResult
}: StrategyFormProps) {
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    
    if (!client.trim() || !region.trim()) {
      setResult({
        success: false,
        error: 'Please enter both the target enterprise client and region of focus.',
        elapsed_time: 0
      })
      return
    }

    setLoading(true)
    setResult(null)

    const startTime = Date.now()

    try {
      const response = await fetch('/api/strategy', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          industry: selectedIndustry,
          client: client.trim(),
          region: region.trim(),
        }),
      })

      if (!response.ok) {
        throw new Error('Failed to connect to the server')
      }

      const reader = response.body?.getReader()
      const decoder = new TextDecoder()

      if (!reader) {
        throw new Error('No response stream available')
      }

      let streamingContent = ''
      
      // Initialize with streaming state
      setResult({
        success: true,
        strategy: '',
        elapsed_time: 0,
        isStreaming: true
      })

      while (true) {
        const { done, value } = await reader.read()
        
        if (done) break

        const chunk = decoder.decode(value, { stream: true })
        const lines = chunk.split('\n')

        for (const line of lines) {
          if (line.startsWith('data: [DONE]')) {
            // Stream finished
            break
          }
          
          if (line.startsWith('data: ') && line.slice(6).trim()) {
            try {
              const jsonStr = line.slice(6).trim()
              if (jsonStr) {
                const data = JSON.parse(jsonStr)
                
                if (data.error) {
                  setResult({
                    success: false,
                    error: data.error,
                    elapsed_time: Math.round((Date.now() - startTime) / 1000)
                  })
                  setLoading(false)
                  return
                }

                if (data.status) {
                  // Show status updates during agent execution
                  setResult({
                    success: true,
                    strategy: '',
                    elapsed_time: Math.round((Date.now() - startTime) / 1000),
                    isStreaming: true,
                    status: data.status
                  })
                }

                if (data.content !== undefined) {
                  streamingContent = data.content
                  setResult({
                    success: true,
                    strategy: streamingContent,
                    elapsed_time: Math.round((Date.now() - startTime) / 1000),
                    isStreaming: !data.isComplete && data.type !== 'complete',
                    status: undefined // Clear status when content starts
                  })
                }

                if (data.type === 'complete' || data.isComplete) {
                  setResult({
                    success: true,
                    strategy: data.content,
                    elapsed_time: Math.round((Date.now() - startTime) / 1000),
                    isStreaming: false,
                    status: undefined
                  })
                }
              }
            } catch (parseError) {
              // Ignore parse errors for incomplete JSON
              console.log('Parse error:', parseError, 'Line:', line)
            }
          }
        }
      }
    } catch (error) {
      setResult({
        success: false,
        error: 'Failed to generate strategy. Please try again.',
        elapsed_time: Math.round((Date.now() - startTime) / 1000)
      })
    } finally {
      setLoading(false)
    }
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 80 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6, delay: 0.4 }}
      className="backdrop-blur-md bg-white/5 border border-white/10 rounded-xl p-8 shadow-xl hover:shadow-2xl transition-all duration-300 hover:-translate-y-1 max-w-5xl mx-auto shadow-blue-500/25 hover:shadow-blue-500/40"
    >
      <form onSubmit={handleSubmit} className="space-y-8">
        <div className="grid md:grid-cols-3 gap-8 justify-center items-end">
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">
              Industry Specialisation
            </label>
            <select
              value={selectedIndustry}
              onChange={(e) => setSelectedIndustry(e.target.value)}
              className="w-full px-4 py-4 bg-gray-800/50 border border-white/20 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 text-lg"
            >
              {Object.entries(industries).map(([key, value]) => (
                <option key={key} value={value}>
                  {key}
                </option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">
              Target Enterprise Client
            </label>
            <input
              type="text"
              value={client}
              onChange={(e) => setClient(e.target.value)}
              placeholder="e.g., Microsoft, Tesla, JPMorgan"
              className="w-full px-4 py-4 bg-gray-800/50 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 text-lg"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">
              Region of Focus
            </label>
            <input
              type="text"
              value={region}
              onChange={(e) => setRegion(e.target.value)}
              placeholder="e.g., North America, EMEA, APAC"
              className="w-full px-4 py-4 bg-gray-800/50 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 text-lg"
            />
          </div>
        </div>

        <div className="flex justify-center pt-4">
          <button
            type="submit"
            disabled={loading}
            className="bg-gradient-to-r from-orange-500 via-blue-500 to-purple-500 hover:opacity-90 transition-all duration-300 text-white font-semibold py-5 px-12 rounded-xl shadow-lg hover:shadow-xl transform hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed min-w-[250px] text-lg"
          >
            {loading ? (
              <div className="flex items-center justify-center">
                <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
                Generating...
              </div>
            ) : (
              <div className="flex items-center justify-center">
                <ChartBarIcon className="h-5 w-5 mr-2" />
                Generate Sales Strategy
              </div>
            )}
          </button>
        </div>
      </form>
    </motion.div>
  )
} 