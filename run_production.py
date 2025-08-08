#!/usr/bin/env python3
import subprocess
import sys
import os
import signal
import psutil

def kill_port_processes(port):
    """Kill any processes using the specified port"""
    try:
        for proc in psutil.process_iter(['pid', 'connections']):
            try:
                for conn in proc.connections():
                    if conn.laddr.port == port:
                        print(f"Killing process {proc.pid} using port {port}")
                        proc.terminate()
                        proc.wait(timeout=3)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
    except Exception as e:
        print(f"Error killing processes on port {port}: {e}")

def build_frontend():
    """Build the React frontend for production"""
    print("Building frontend...")
    try:
        # Ensure we're in the client directory
        if os.path.exists("client"):
            os.chdir("client")
            print(f"Changed to client directory: {os.getcwd()}")

        # Install dependencies
        print("Installing frontend dependencies...")
        subprocess.run(["npm", "install"], check=True)

        # Build for production
        print("Building frontend for production...")
        subprocess.run(["npm", "run", "build"], check=True)

        # Return to parent directory
        os.chdir("..")
        print("Frontend build completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Frontend build failed: {e}")
        return False
    except FileNotFoundError:
        print("npm not found. Make sure Node.js is installed.")
        return False

def run_server():
    """Run the production server"""
    print("Starting production server...")
    try:
        subprocess.run(["python3", "server/static_server.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Server failed to start: {e}")
    except KeyboardInterrupt:
        print("\nShutting down server...")

if __name__ == "__main__":
    print("=== Shift Your Shape - Production Build ===")

    # Kill any existing processes on port 5000
    print("Cleaning up port 5000...")
    kill_port_processes(5000)

    # Build frontend
    if not build_frontend():
        print("❌ Frontend build failed. Exiting.")
        sys.exit(1)

    # Start production server
    run_server()