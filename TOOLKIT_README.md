# Development Environment Toolkit

This toolkit provides a set of scripts to help you manage your development environment, optimize system performance, and fix common issues with your Vite project.

## Available Scripts

### Master Toolkit

- **`master_toolkit.sh`**: The main entry point that provides access to all tools.
  - Run with: `./master_toolkit.sh`

### Individual Tools

1. **Mac Service Manager**
   - **`mac_service_manager.sh`**: Helps you identify and manage services running on your Mac.
   - Features:
     - List all services listening on ports
     - Group services by type (web servers, databases, system services)
     - Check common development ports
     - Identify potentially unnecessary services
     - Clean up development services and ports

2. **macOS System Optimizer**
   - **`macos_system_optimizer.sh`**: Helps you identify and manage macOS system services.
   - Features:
     - List all running launchd services
     - List user and system launch agents
     - List system launch daemons
     - Check for resource-intensive services
     - Check for third-party startup items
     - Optimize system performance (clear caches)
     - Get recommendations for optimization

3. **Vite Project Fixer**
   - **`fix_vite_project.sh`**: Helps you fix common issues with your Vite project.
   - Features:
     - Check JavaScript syntax
     - Fix script.js syntax issues
     - Create fixed version of script.js
     - Update index.html to use fixed script
     - Fix Vite configuration
     - Clean up development environment

4. **Cassandra Service Manager**
   - **`stop_cassandra.sh`**: Helps you manage the Cassandra service.
   - Features:
     - Check if Cassandra is running
     - Stop Cassandra
     - Start Cassandra
     - Disable Cassandra autostart

5. **Homebrew Service Manager**
   - **`homebrew_service_manager.sh`**: Helps you manage Homebrew services.
   - Features:
     - List all Homebrew services
     - Stop all Homebrew services
     - Disable all Homebrew services from starting at login
     - Start a specific Homebrew service
     - Stop a specific Homebrew service

### Cleanup Scripts

- **`master_cleanup.sh`**: Comprehensive cleanup script that runs all cleanup scripts.
- **`cleanup_all_ports.sh`**: Cleans up common development ports (3000-3004, 8000).
- **`cleanup_java_ports.sh`**: Cleans up Java processes on specific ports.
- **`check_ports.sh`**: Checks all running processes on relevant ports.
- **`cleanup_and_start.sh`**: Kills all processes and starts your application on port 4000.

## Common Issues and Solutions

### Port 5000 in Use by ControlCenter

The macOS ControlCenter service uses port 5000 and will keep restarting if killed. The solution is to configure your application to use a different port (e.g., port 4000), which has been done in the `vite.config.js` file.

### Multiple Development Servers Running

If you have multiple development servers running, they can cause conflicts and consume resources. Use the cleanup scripts to kill unnecessary processes.

### JavaScript Syntax Errors

If you're experiencing syntax errors in your JavaScript files, use the Vite Project Fixer to check and fix syntax issues.

### Cassandra Running in the Background

Cassandra is a database service that might be running in the background and consuming resources. Use the Cassandra Service Manager to stop it if you're not using it.

### Homebrew Services Running Automatically

Homebrew services might be configured to start automatically at login. Use the Homebrew Service Manager to disable autostart for services you don't need.

## System Services

These are common macOS system services that might be running in the background:

- `com.apple.ControlCenter` (uses port 5000)
- `com.apple.Spotlight` (indexing service)
- `com.apple.photoanalysisd` (photo analysis)
- `com.apple.cloudd` (iCloud sync)
- `com.apple.CoreLocationAgent` (location services)

## Homebrew Services

These are common Homebrew services that might be running in the background:

- `cassandra` (uses ports 7000, 7199, 9042)
- `mysql`
- `postgresql`
- `mongodb`
- `redis`

## Useful Commands

- To see all running launchd services:
  ```
  launchctl list | grep -v "^-" | sort
  ```

- To see all services listening on ports:
  ```
  lsof -i -P | grep LISTEN
  ```

- To kill a process on a specific port:
  ```
  lsof -ti:PORT_NUMBER | xargs kill -9
  ```

- To see all running Homebrew services:
  ```
  brew services list
  ```

- To stop all Homebrew services:
  ```
  brew services list | grep started | awk '{print $1}' | xargs -I{} brew services stop {}
  ```

## Getting Started

1. Make all scripts executable:
   ```
   chmod +x *.sh
   ```

2. Run the master toolkit:
   ```
   ./master_toolkit.sh
   ```

3. Follow the on-screen instructions to use the tools.

## Note

Some system services are essential for macOS to function properly. Be careful when disabling or killing system services, as it may affect system stability. The toolkit is designed to help you identify and manage services safely, but use caution when making changes to system services. 