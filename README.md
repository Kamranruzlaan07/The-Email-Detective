# 🕵️ The Email Detective

> A full-stack email investigation platform built with **FastAPI** and **React** for analyzing email headers, validating email authentication, reconstructing email routes, and generating an overall Trust Score.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-Build-646CFF?logo=vite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 Overview

The Email Detective is a modern email investigation platform designed for Microsoft 365 administrators, SOC analysts, security engineers, and IT professionals.

The application analyzes raw email headers and `.eml` files to verify sender authenticity, inspect authentication records, reconstruct message routes, identify sending providers, geolocate sender IP addresses, assess security risks, and calculate an overall Trust Score.

The project demonstrates full-stack development using Python, FastAPI, React, and modern web technologies.

---

## ✨ Features

### 📧 Email Analysis

- Analyze raw email headers
- Upload and inspect `.eml` files
- MIME Subject decoding
- RFC-compliant header parsing

### 🔐 Email Authentication

- SPF validation
- DKIM validation
- DMARC validation

### 🔍 Investigation

- Public IP detection
- Sender IP geolocation
- Email route reconstruction
- Provider detection
- Risk assessment engine
- Trust Score (0–100)

### 🎨 Interactive Dashboard

- Email Verdict
- Header Details
- Authentication Results
- Risk Analysis
- Geolocation
- Provider Information
- Trust Score

---

## 🏗 Architecture

```
React + Vite
      │
      ▼
 FastAPI REST API
      │
      ▼
──────────────────────────
 Header Parser
 SPF Checker
 DKIM Checker
 DMARC Checker
 Route Parser
 Geo Locator
 Provider Detector
 IP Validator
 Risk Engine
 Trust Engine
 Report Builder
──────────────────────────
```

---

## 🛠 Tech Stack

### Backend

- Python
- FastAPI
- Uvicorn
- Pydantic

### Frontend

- React
- Vite
- Axios

---

## 📁 Project Structure

```
The-Email-Detective/
│
├── backend/
│   └── app/
│       ├── api/
│       ├── models/
│       ├── modules/
│       │   ├── header_parser.py
│       │   ├── spf_checker.py
│       │   ├── dkim_checker.py
│       │   ├── dmarc_checker.py
│       │   ├── route_parser.py
│       │   ├── geo_locator.py
│       │   ├── provider_detector.py
│       │   ├── ip_validator.py
│       │   ├── risk_engine.py
│       │   ├── trust_engine.py
│       │   └── report_builder.py
│       └── main.py
│
├── frontend/
│   └── src/
│       ├── components/
│       ├── App.jsx
│       └── main.jsx
│
├── docs/
├── samples/
├── tests/
└── README.md
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/<your-username>/The-Email-Detective.git
cd The-Email-Detective
```

---

### Backend

```bash
cd backend

python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

The backend will run at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

The frontend will run at:

```
http://localhost:5173
```

---

## 📡 API

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/analyze-header` | Analyze raw email headers |
| POST | `/analyze-eml` | Analyze uploaded `.eml` files |

---

## 📸 Screenshots

### Dashboard

> Add screenshot after deployment

### Trust Score

> Add screenshot after deployment

### Email Analysis

> Add screenshot after deployment

---

## 🚀 Deployment

### Frontend

- Vercel

### Backend

- Render

---

## 🗺 Roadmap

### ✅ Version 1.0

- Header parsing
- MIME decoding
- SPF validation
- DKIM validation
- DMARC validation
- Route analysis
- Provider detection
- IP geolocation
- Risk assessment
- Trust Score engine
- React dashboard

### 🔜 Future Improvements

- PDF report export
- AI-assisted phishing explanations
- URL reputation checks
- Attachment analysis
- Threat intelligence integration

---

## 👨‍💻 Author

**Kamran**

Built as a portfolio project demonstrating full-stack software development, REST API design, email security analysis, and modern React application development.

---

## 📄 License

This project is licensed under the MIT License.