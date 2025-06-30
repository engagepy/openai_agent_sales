'use client'

import { motion } from 'framer-motion'
import { 
  SparklesIcon, 
  RocketLaunchIcon
} from '@heroicons/react/24/outline'

export default function InfoCards() {
  return (
    <div className="grid md:grid-cols-2 gap-8 mb-16 max-w-6xl mx-auto">
      <motion.div
        initial={{ opacity: 0, x: -80 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ duration: 0.6, delay: 0.2 }}
        className="backdrop-blur-md bg-white/5 border border-white/10 rounded-xl p-6 shadow-xl hover:shadow-2xl transition-all duration-300 hover:-translate-y-1"
      >
        <div className="flex items-center mb-4">
          <SparklesIcon className="h-8 w-8 text-orange-500 mr-3" />
          <h3 className="text-xl font-semibold text-white">About This App</h3>
        </div>
        <p className="text-gray-300">
          Built by <strong className="text-orange-500">M37Labs</strong>, this app empowers sales teams with intelligent, 
          real-time AI agents. These agents generate customised sales strategies, regional insights, 
          and ROI-focused recommendations for any target client.
        </p>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, x: 80 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ duration: 0.6, delay: 0.3 }}
        className="backdrop-blur-md bg-white/5 border border-white/10 rounded-xl p-6 shadow-xl hover:shadow-2xl transition-all duration-300 hover:-translate-y-1"
      >
        <div className="flex items-center mb-4">
          <RocketLaunchIcon className="h-8 w-8 text-blue-500 mr-3" />
          <h3 className="text-xl font-semibold text-white">How It Works</h3>
        </div>
        <ul className="text-gray-300 space-y-2">
          <li>• Select an industry-specific AI agent</li>
          <li>• Provide your target enterprise client and region</li>
          <li>• Get a tailored sales playbook instantly</li>
        </ul>
      </motion.div>
    </div>
  )
} 