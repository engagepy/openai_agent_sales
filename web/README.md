# Enterprise AI Sales Agents - Frontend

Modern Next.js frontend with dark futuristic theme for the Enterprise AI Sales Agents platform.

## Features

- Dark futuristic theme with gradients (orange to blue, purple)
- Responsive design with glass-morphism effects
- Real-time AI strategy generation
- Enterprise-grade professional interface
- Built with Next.js 14, TypeScript, and Tailwind CSS

## Setup

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

3. Open [http://localhost:3000](http://localhost:3000) in your browser

## Dependencies

- Next.js 14 with App Router
- React 18
- TypeScript
- Tailwind CSS with custom gradients
- Framer Motion for animations
- Heroicons for icons
- AI SDK for streaming responses

## Backend Connection

The frontend connects to the FastAPI backend running on `http://localhost:8000`. Make sure the agent server is running before using the web app.

## Build for Production

```bash
npm run build
npm start
``` 