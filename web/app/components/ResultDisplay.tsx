'use client'

import { motion } from 'framer-motion'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import { 
  ClockIcon,
  ExclamationTriangleIcon
} from '@heroicons/react/24/outline'
import { SalesStrategyResponse } from './types'

interface ResultDisplayProps {
  result: SalesStrategyResponse | null
}

export default function ResultDisplay({ result }: ResultDisplayProps) {
  if (!result) return null

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6 }}
      className="mt-8 max-w-4xl mx-auto"
    >
      {result.success ? (
        <div className="backdrop-blur-md bg-white/5 border border-white/10 rounded-xl p-6 shadow-xl hover:shadow-2xl transition-all duration-300 hover:-translate-y-1">
          <div className="flex items-center justify-between mb-6">
            <h3 className="text-2xl font-semibold text-white">Recommended Strategy</h3>
            <div className="flex items-center text-green-400">
              <ClockIcon className="h-5 w-5 mr-1" />
              <span className="text-sm">{result.elapsed_time}s</span>
            </div>
          </div>
          <div className="prose prose-invert max-w-none">
            <ReactMarkdown
              remarkPlugins={[remarkGfm]}
              className="text-gray-200 leading-relaxed"
              components={{
                h1: ({ children }) => <h1 className="text-3xl font-bold text-white mb-4 border-b border-gray-600 pb-2">{children}</h1>,
                h2: ({ children }) => <h2 className="text-2xl font-bold text-white mb-3 mt-6">{children}</h2>,
                h3: ({ children }) => <h3 className="text-xl font-semibold text-white mb-2 mt-4">{children}</h3>,
                p: ({ children }) => <p className="text-gray-200 mb-4 leading-relaxed">{children}</p>,
                ul: ({ children }) => <ul className="list-disc list-inside text-gray-200 mb-4 space-y-1">{children}</ul>,
                ol: ({ children }) => <ol className="list-decimal list-inside text-gray-200 mb-4 space-y-1">{children}</ol>,
                li: ({ children }) => <li className="text-gray-200">{children}</li>,
                strong: ({ children }) => <strong className="text-white font-semibold">{children}</strong>,
                em: ({ children }) => <em className="text-blue-300">{children}</em>,
                a: ({ children, href }) => (
                  <a 
                    href={href} 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="text-blue-400 hover:text-blue-300 underline transition-colors"
                  >
                    {children}
                  </a>
                ),
                blockquote: ({ children }) => (
                  <blockquote className="border-l-4 border-orange-500 pl-4 py-2 bg-gray-800/30 rounded-r-lg mb-4">
                    {children}
                  </blockquote>
                ),
              }}
            >
              {result.strategy || ''}
            </ReactMarkdown>
          </div>
        </div>
      ) : (
        <div className="backdrop-blur-md bg-white/5 border border-red-500/20 bg-red-500/5 rounded-xl p-6 shadow-xl hover:shadow-2xl transition-all duration-300 hover:-translate-y-1">
          <div className="flex items-center mb-4">
            <ExclamationTriangleIcon className="h-6 w-6 text-red-400 mr-2" />
            <h3 className="text-lg font-semibold text-red-400">Guardrail Triggered</h3>
          </div>
          <p className="text-red-300">{result.error}</p>
        </div>
      )}
    </motion.div>
  )
} 