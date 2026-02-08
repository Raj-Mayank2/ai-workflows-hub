# AI Resume Screening & Candidate Ranking System

## Overview

An **AI-powered Resume Screening and Candidate Shortlisting System** designed to automate repetitive HR tasks.  
The system parses resumes, extracts structured information, evaluates candidates against job descriptions using **semantic AI matching**, and ranks applicants based on multiple criteria.

This project demonstrates an end-to-end **AI + Automation + Full Stack Development** workflow.

---

## Features

### Resume Processing
- Upload resumes in **PDF/DOCX**
- Automatically extracts:
  - Name
  - Email
  - Skills
  - Experience
  - Education
  - CGPA
  - Projects
  - Hackathons
  - Achievements
  - Coding Profiles
  - Certifications

---

### AI Matching
- Semantic similarity using **Sentence Transformers**
- Context-aware comparison between resume content and job description

---

### Candidate Evaluation
Hybrid scoring based on:
- AI Similarity
- Skill Match
- Experience Match
- Achievements
- CGPA
- Projects

---

### Candidate Ranking
- Evaluates multiple resumes
- Returns ranked candidate list
- Provides explainable scoring breakdown

---

### Data Persistence
- MongoDB Atlas used for storing resume data
- Resumes remain available after server restart

---

### Export Functionality
- Export ranked candidates as CSV
- Download HR-ready report

---

### Dashboard
Simple React dashboard to:
- Upload resumes
- Enter job description
- View ranked candidates
- Export results

---

## Tech Stack

### Backend
- FastAPI
- Python
- PyMuPDF
- python-docx
- Sentence-Transformers
- Scikit-Learn
- MongoDB (PyMongo)

---

### Frontend
- React (Vite)
- CSS

---

## System Architecture

Upload Resume → Parse → Store (MongoDB)  
Job Description → AI Matching → Score Calculation → Ranking → Export

---

## API Endpoints

### Upload Resume
```
POST /resume/upload
```

Uploads and parses resume.

---

### Match Single Resume
```
POST /resume/match
```

Returns detailed evaluation.

---

### Rank All Candidates
```
POST /resume/rank
```

Returns sorted candidate list.

---

### Export Ranked Candidates
```
POST /resume/export
```

Downloads CSV file.

---

## Installation

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

### Frontend Setup

```bash
cd resume-ai-dashboard
npm install
npm run dev
```

---

## Environment Configuration

Create file:

```
app/database.py
```

Add MongoDB connection string:

```python
MONGO_URI = "YOUR_MONGODB_URI"
```

---

## Future Improvements

- Advanced NLP entity extraction
- Bias reduction filtering
- Authentication system
- Batch resume upload (ZIP)
- Analytics dashboard
- Deployment using Docker

---

## Project Motivation

Recruiters spend significant time manually screening resumes.  
This system automates candidate shortlisting while maintaining transparency and explainable scoring.

---

## Author

**Mayank Raj**

---

## License

MIT License
