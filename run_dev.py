
import subprocess
import sys
import threading
import time
import os

def run_backend():
    """Run the FastAPI backend server"""
    print("Starting backend server...")
    subprocess.run(["python3", "-m", "uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"])

def run_frontend():
    """Run the Vite frontend server"""
    print("Starting frontend server...")
    try:
        # Ensure we're in the client directory
        if os.path.exists("client"):
            os.chdir("client")
            print(f"Changed to client directory: {os.getcwd()}")
        elif not os.path.exists("package.json"):
            print("Error: No package.json found in current or client directory")
            return None
        
        print("Contents of current directory:", os.listdir("."))
        
        # Run npm install first to ensure dependencies are installed
        print("Installing dependencies...")
        subprocess.run(["npm", "install"], check=True)
        
        # Start the dev server
        print("Starting Vite dev server...")
        result = subprocess.run(["npm", "run", "dev"], check=True)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Frontend failed to start: {e}")
        return None
    except FileNotFoundError:
        print("npm not found. Make sure Node.js is installed.")
        return None

if __name__ == "__main__":
    print("Current working directory:", os.getcwd())
    print("Available files:", os.listdir("."))
    
    # Start backend in a separate thread
    backend_thread = threading.Thread(target=run_backend)
    backend_thread.daemon = True
    backend_thread.start()
    
    # Give backend time to start
    print("Waiting for backend to start...")
    time.sleep(3)
    
    # Start frontend (this will block)
    try:
        print("About to start frontend...")
        run_frontend()
    except KeyboardInterrupt:
        print("\nShutting down servers...")
        sys.exit(0)
