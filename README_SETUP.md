
# Shift Your Shape - Setup Guide

## Quick Start (Recommended)

### Option 1: Production Mode (Single Command)
```bash
python3 run_production.py
```
This will:
- Build the React frontend
- Start the FastAPI server
- Serve everything on http://localhost:5000

### Option 2: Development Mode (Two Terminals)
```bash
# Terminal 1: Start the backend
cd server
python3 main.py

# Terminal 2: Start the frontend
cd client
npm install
npm run dev
```

## Local Installation

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd shift-your-shape
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Node.js dependencies**
   ```bash
   cd client
   npm install
   cd ..
   ```

4. **Run the application**
   ```bash
   python3 run_production.py
   ```

5. **Open your browser**
   - Navigate to http://localhost:5000
   - Your data will be automatically saved in a `data/` folder

## Data Storage

- **Local Deployment**: Data is stored in a `data/user_profiles.json` file in your project directory
- **Backup**: Simply copy the `data/` folder to backup your information
- **Reset**: Delete the `data/` folder to start fresh

## Troubleshooting

### Port Already in Use
If you get a "port already in use" error:
```bash
# Kill any process using port 5000
pkill -f "uvicorn\|python.*5000"
```

### Dependencies Missing
```bash
# Reinstall Python dependencies
pip install -r requirements.txt

# Reinstall Node dependencies
cd client && npm install
```

### Build Errors
```bash
# Clean and rebuild
rm -rf client/dist client/node_modules
cd client && npm install && npm run build
```

## Features

- **Weight Tracking**: Log daily weight with trend analysis
- **Calorie Management**: Set and track daily calorie targets
- **Step Counting**: Monitor daily activity levels
- **Progress Insights**: View charts and statistics
- **Research-Based**: Calculations based on peer-reviewed studies

## Technical Details

- **Frontend**: React + TypeScript + Tailwind CSS
- **Backend**: FastAPI (Python)
- **Data**: Local JSON file storage
- **Deployment**: Single-server production mode
