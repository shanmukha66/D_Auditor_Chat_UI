#!/bin/bash

echo "====================================================="
echo "KILLING ALL PROCESSES ON COMMON DEVELOPMENT PORTS"
echo "====================================================="

# Common development ports
PORTS=(3000 3001 3002 3003 3004 4000 4001 4002 4003 4004 5000 8000 8080 8888 9000)

# Kill processes on each port
for port in "${PORTS[@]}"; do
    pid=$(lsof -ti:$port)
    if [ -n "$pid" ]; then
        echo "Killing process $pid on port $port"
        kill -9 $pid 2>/dev/null
    else
        echo "No process running on port $port"
    fi
done

# Kill Node.js processes (which might be running your Vite server)
echo "Killing Node.js processes related to your project..."
ps aux | grep "node" | grep -v grep | grep -v "Code" | grep -v "Visual Studio" | grep -v "IntelliJ" | awk '{print $2}' | xargs kill -9 2>/dev/null || echo "No Node.js processes found"

# Kill Python HTTP servers
echo "Killing Python HTTP servers..."
ps aux | grep "python.*http" | grep -v grep | awk '{print $2}' | xargs kill -9 2>/dev/null || echo "No Python HTTP servers found"

echo "====================================================="
echo "CLEANUP COMPLETED"
echo "====================================================="
echo "You can now start your application on a clean port."
echo "Run: npm run dev" 