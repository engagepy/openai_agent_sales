'use client'

import { motion } from 'framer-motion'

export default function Header() {
  return (
    <header className="relative overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-r from-orange-500 via-blue-500 to-purple-500 opacity-20"></div>
      <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-center"
        >
          <h1 className="text-5xl md:text-7xl font-bold mb-6">
            <span className="bg-gradient-to-r from-orange-500 via-blue-500 to-purple-500 bg-clip-text text-transparent">Enterprise AI</span>
            <br />
            <span className="text-white">Sales Agents</span>
          </h1>
          <p className="text-xl md:text-2xl text-gray-300 max-w-3xl mx-auto">
            Powered by <span className="text-orange-500 font-semibold">M37Labs</span> - 
            Generate intelligent, real-time AI sales strategies for any enterprise client
          </p>
        </motion.div>
      </div>
    </header>
  )
} 