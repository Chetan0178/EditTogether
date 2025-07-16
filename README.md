# 📘 EditTogether (Real-Time Collaborative Text Editor)
Project Description : A modern web application enabling real-time collaborative editing of text documents with minimal AI-powered suggestions. Built with WebSockets for live interaction, secure authentication using JWT, and a responsive front-end. The backend is modular and cloud deployment-ready.


## 🚀 Features

### ✅ 1. Real-Time Collaboration
- WebSocket-powered live editing.
- Multiple users can edit a document simultaneously and see updates in real time.

### ✅ 2. User Authentication
- Secure JWT-based user authentication.
- Login/register with email/password.
- OAuth (Google) support (optional/extendable).

### 🛠 3. Basic AI Suggestions *(Work in Progress)*
- Integrating AI grammar correction and writing suggestions.
- Planned integration with lightweight third-party NLP/AI APIs.

### ✅ 4. Responsive User Interface
- Clean, modern, and intuitive front-end.
- Fully responsive design for mobile, tablet, and desktop.

### 🛠 5. Cloud Deployment *(Work in Progress)*
- Preparing deployment steps for platforms like Heroku, GCP, Vercel, or AWS.
- Live collaboration demo will be hosted once deployment is complete.

---

## 💻 Tech Stack

### Backend:
- Python
- Django / Django Channels (for WebSockets)
- Django REST Framework (JWT authentication)
- Redis (optional, for WebSocket channels layer)

### AI/NLP Integration (Planned):
- OpenAI / Grammarly / LanguageTool API (for suggestions)

### Deployment Targets:
- Heroku / Render / Vercel / GCP / AWS

## 📂 Project Structure
EditTogether
│
├── editor/ # Django project folder
├── users/ # JWT-based auth
├── EditTogether/ # Settings.py etc.
├── manage.py
├── requirements.txt/ # all requirement packages
├── README.md
└── .env



## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/Chetan0178/EditTogether.git
cd EditTogether


### 2.Setup Virtual Environment

python -m venv venv
source venv/bin/activate 

### 3.Install Requirements
pip install -r requirements.txt


### 4.Run Migrations
python manage.py migrate

### 5.Start the Server
python manage.py runserver





✨ Coming Soon
✏️ AI writing suggestions via OpenAI or LanguageTool
☁️ Cloud deployment (Heroku / Vercel)
📜 Document versioning


