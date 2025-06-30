#!/bin/bash

echo "🚀 Starting Enterprise AI Sales Agents"
echo "======================================="

# Function to run commands in new terminal tabs/windows
run_in_new_tab() {
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        osascript -e "tell application \"Terminal\" to do script \"cd $(pwd)/$1 && $2\""
    else
        # Linux
        gnome-terminal --tab --title="$1" -- bash -c "cd $1 && $2; exec bash"
    fi
}

echo "📡 Starting FastAPI Agent Server..."
run_in_new_tab "agent" "python main.py"

echo "🌐 Starting Next.js Web App..."
run_in_new_tab "web" "npm run dev"

echo ""
echo "✅ Services starting up:"
echo "   • Agent API: http://localhost:8000"
echo "   • Web App:   http://localhost:3000"
echo ""
echo "💡 Make sure you have:"
echo "   • OpenAI API key in agent/.env"
echo "   • Dependencies installed (pip install -r agent/requirements.txt)"
echo "   • Node modules installed (cd web && npm install)" 