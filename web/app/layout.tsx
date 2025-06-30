import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Enterprise AI Sales Agents',
  description: 'AI-powered sales strategy generation for enterprise clients',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="dark">
      <body className={`${inter.className} min-h-screen bg-gradient-to-br from-slate-950 via-gray-900 to-indigo-950`}>
        <div className="min-h-screen bg-grid-pattern">
          {children}
        </div>
      </body>
    </html>
  )
} 