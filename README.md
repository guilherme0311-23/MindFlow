# MindFlow

> A production-ready backend for an ADHD-first productivity platform, built with FastAPI, PostgreSQL, JWT authentication, Docker, and deployed on Railway.

![Tests](https://github.com/guilherme0311-23/MindFlow/actions/workflows/tests.yml/badge.svg)

## Live Demo

🌐 **Production API**  
https://mindflow-production-5b68.up.railway.app

📖 **Swagger Documentation**  
https://mindflow-production-5b68.up.railway.app/docs

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | FastAPI |
| ORM | SQLAlchemy |
| Database | PostgreSQL (Supabase) |
| Authentication | JWT + bcrypt |
| Containerization | Docker |
| Deployment | Railway |

---

## Features

- JWT authentication
- Secure password hashing with bcrypt
- User registration and login
- Per-user task ownership
- Full task CRUD (create, read, update, delete)
- PostgreSQL persistence
- Dockerized development
- Production deployment on Railway

---

## Architecture
Client
│
▼
JWT Authentication
│
▼
FastAPI
│
▼
SQLAlchemy
│
▼
PostgreSQL (Supabase)

---

## API Endpoints

### Authentication

| Method | Endpoint |
|---------|----------|
| POST | `/register` |
| POST | `/login` |

### Tasks

| Method | Endpoint | Description | Auth |
|--------|----------|--------------|------|
| POST | `/tasks` | Create a new task | ✅ |
| GET | `/tasks` | List the authenticated user's tasks | ✅ |
| GET | `/tasks/{task_id}` | Retrieve a specific task | ✅ |
| PATCH | `/tasks/{task_id}` | Partially update a task | ✅ |
| DELETE | `/tasks/{task_id}` | Delete a task | ✅ |

---

## Running Locally

Requirements:

- Docker
- Docker Compose

Clone the repository:

```bash
git clone https://github.com/guilherme0311-23/MindFlow.git
cd MindFlow
```

Create a `.env` file:

```env
DATABASE_URL=your_postgres_connection_string
SECRET_KEY=your_jwt_secret_key
```

Run:

```bash
docker compose up --build
```

API available at:
http://localhost:8000

Swagger:
http://localhost:8000/docs

---

# About

MindFlow is both a real product and a backend engineering portfolio project.

It is built by someone with ADHD, for people with ADHD. Every product decision reflects that perspective: low-friction onboarding, one task visible at a time, and AI-assisted decision making instead of superficial gamification.

This repository contains the backend responsible for authentication, task management, authorization, and persistent storage.

---

# Security Case Study

One of the most valuable lessons in this project happened after deployment.

While testing the production API with two real user accounts, I discovered a critical security issue.

The endpoint responsible for listing tasks returned resources belonging to any authenticated user.

Authentication correctly answered:

> "Who is the user?"

But the application never answered:

> "Does this resource belong to this user?"

This is a classic **IDOR (Insecure Direct Object Reference)** vulnerability.

## Root Cause

The `Task` model had no relationship with its owner.

## Solution

- Added `owner_id` as a foreign key referencing `users.id`
- Ownership is always derived from `current_user.id`
- The client never controls `owner_id`
- Every task query is filtered by the authenticated owner

---

## Security Audit

After fixing the issue, every endpoint accessing resources by ID was audited.

Results:

✅ `GET /tasks`

✅ `GET /tasks/{task_id}`

✅ `POST /tasks`

✅ `PATCH /tasks/{task_id}`

✅ `DELETE /tasks/{task_id}`

✅ Authentication routes (not applicable)

The same ownership pattern — filtering by `owner_id == current_user.id` and returning 404 (never 403) when a resource doesn't belong to the requester — was validated across the full CRUD, including the update and delete operations added after the initial audit. Each route was manually tested with two real user accounts to confirm that one user can never read, modify, or delete another user's tasks.

No remaining ownership vulnerabilities were found.

Finding, fixing, and auditing this vulnerability is part of the engineering process—not something to hide. This repository intentionally documents both the mistake and the solution.

---

# Roadmap

| Stage | Status |
|--------|--------|
| Backend Foundation | ✅ |
| JWT Authentication | ✅ |
| Docker | ✅ |
| Railway Deployment | ✅ |
| Security Audit | ✅ |
| Full CRUD | ✅ |
| Automated Testing (pytest) | ✅ |
| CI/CD (GitHub Actions) | ✅ |
| Landing Page | ⏳ |

---

# Author

**Guilherme Dias Lemos**

Information Systems student passionate about backend engineering, software architecture, and building real-world applications while documenting the learning process.