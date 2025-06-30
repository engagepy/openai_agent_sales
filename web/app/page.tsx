'use client'

import { useState, useEffect } from 'react'
import { 
  Header,
  InfoCards,
  StrategyForm,
  ResultDisplay,
  Footer,
  Industry,
  SalesStrategyResponse
} from './components'

export default function HomePage() {
  const [industries, setIndustries] = useState<Industry>({})
  const [selectedIndustry, setSelectedIndustry] = useState('')
  const [client, setClient] = useState('')
  const [region, setRegion] = useState('')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState<SalesStrategyResponse | null>(null)

  useEffect(() => {
    // Fetch available industries
    fetch('/api/industries')
      .then(res => res.json())
      .then(data => {
        setIndustries(data.industries)
        // Set first industry as default
        const firstKey = Object.keys(data.industries)[0]
        if (firstKey) {
          setSelectedIndustry(data.industries[firstKey])
        }
      })
      .catch(err => console.error('Failed to fetch industries:', err))
  }, [])

  return (
    <div className="min-h-screen flex flex-col">
      <Header />

      {/* Main Content */}
      <main className="flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 flex flex-col justify-center">
        <InfoCards />

        <StrategyForm
          industries={industries}
          selectedIndustry={selectedIndustry}
          setSelectedIndustry={setSelectedIndustry}
          client={client}
          setClient={setClient}
          region={region}
          setRegion={setRegion}
          loading={loading}
          setLoading={setLoading}
          setResult={setResult}
        />

        <ResultDisplay result={result} />
      </main>

      <Footer />
    </div>
  )
} 