
#!/usr/bin/env python3
import subprocess
import sys
import os

def check_python():
    """Check if Python 3.8+ is available"""
    if sys.version_info < (3, 8):
        print("Error: Python 3.8 or higher is required")
        return False
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def check_node():
    """Check if Node.js is available"""
    try:
        result = subprocess.run(["node", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ Node.js {result.stdout.strip()} detected")
            return True
    except FileNotFoundError:
        pass
    
    print("❌ Node.js not found. Please install Node.js 16+ from https://nodejs.org/")
    return False

def install_python_deps():
    """Install Python dependencies"""
    print("Installing Python dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("✓ Python dependencies installed")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install Python dependencies")
        return False

def install_frontend_deps():
    """Install frontend dependencies"""
    print("Installing frontend dependencies...")
    try:
        os.chdir("client")
        subprocess.run(["npm", "install"], check=True)
        os.chdir("..")
        print("✓ Frontend dependencies installed")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install frontend dependencies")
        return False

def main():
    print("=== Shift Your Shape - Setup Script ===")
    print("This script will check your system and install dependencies.\n")
    
    # Check prerequisites
    if not check_python():
        return False
    
    if not check_node():
        return False
    
    # Install dependencies
    if not install_python_deps():
        return False
    
    if not install_frontend_deps():
        return False
    
    print("\n=== Setup Complete! ===")
    print("To run the application:")
    print("• Development mode: python3 run_dev.py")
    print("• Production mode: python3 run_production.py")
    print("• The app will be available at http://localhost:5000")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
