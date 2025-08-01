# Smart Inventory Finder 
AI-powered search, real-time stock status, and Node-RED IoT alert simulation.

## Overview
A practical demo: Python FastAPI backend with semantic (AI) search and a Node-RED dashboard that simulates stock alerts. No hardware needed!

## Features
- Semantic Search: Find items by description (not just keywords!)
- Live Status: See if any inventory is low
- Node-RED dashboard: Visualizes alerts with a simulated LED indicator

## Backend Usage
- Start backend:
  cd backend
  pip install -r requirements.txt
  uvicorn app:app --reload

- Endpoints:
  /search?q=desc  (semantic search)
  /status         (check if any low stock)

## Node-RED
- Import iot/node_red_flow.json
- Visit Node-RED dashboard at /ui
- LED shows green (OK) or red (low stock) based on backend status

## Project Structure
- backend/: FastAPI app, search logic, inventory
- iot/: Node-RED flow for dashboard simulation
