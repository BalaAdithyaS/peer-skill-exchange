# SkillSwap Campus

SkillSwap Campus is a full-stack web application that enables students to exchange skills through a peer-to-peer platform. Users can offer skills they know, discover skills from others, and interact through a structured system.

## Overview

The project is designed to demonstrate full-stack development, backend architecture, and database integration. It follows a modular structure using Flask for the backend and React for the frontend.

## Features

* User authentication (JWT-based)
* Skill listing and management
* Skill discovery and search functionality
* RESTful API design
* Modular backend using Flask Blueprints
* Token-based authorization for protected routes

## Tech Stack

**Frontend**

* React.js
* JavaScript
* React Router

**Backend**

* Python (Flask)
* Flask Blueprints (modular architecture)
* Flask-JWT-Extended (authentication)

**Database**

* MongoDB


## Setup Instructions

### Backend

```
cd backend
pip install -r requirements.txt
python run.py
```

### Frontend

```
cd frontend
npm install
npm start
```

## API Endpoints (Sample)

* `POST /auth/register` — Register a user
* `POST /auth/login` — Login and receive JWT
* `GET /skills/all` — Fetch all skills
* `POST /skills/add` — Add a skill (requires token)

## Current Status

This project is under active development. Core backend structure and authentication system are implemented, with ongoing improvements in frontend integration and feature completeness.

## Future Improvements

* Skill recommendation system
* Real-time communication (chat)
* Session scheduling
* UI/UX enhancements
* Deployment to cloud platforms

## Purpose

This project was built to demonstrate:

* Full-stack application development
* Backend system design
* API development and integration
* Authentication and security concepts

## Author

Bala Adithya
B.Tech Information Technology, VIT Vellore
