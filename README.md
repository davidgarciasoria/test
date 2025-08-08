
# Shift Your Shape - Fitness Tracking App

A full-stack fitness tracking application built with React/TypeScript frontend and Python FastAPI backend.

## Features

- Weight tracking with progress visualization
- Calorie and step counting
- BMR and TDEE calculations
- Progress insights and achievements
- Data export/import functionality

## Getting Started

### Prerequisites
- Node.js (v18 or higher)
- Python (v3.8 or higher)

### Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Install frontend dependencies:
```bash
cd client
npm install
```

### Running the Application

**Option 1: Using the development script**
```bash
python run_dev.py
```

**Option 2: Manual startup**
1. Start the backend server:
```bash
python -m uvicorn server.main:app --host 0.0.0.0 --port 5000 --reload
```

2. In a new terminal, start the frontend:
```bash
cd client
npm run dev
```

The frontend will be available at `http://localhost:5173` and the backend API at `http://localhost:5000`.

## Tech Stack

- **Frontend:** React 18, TypeScript, Vite, Tailwind CSS
- **Backend:** Python, FastAPI, Uvicorn
- **Charts:** Recharts
- **Icons:** Lucide React
