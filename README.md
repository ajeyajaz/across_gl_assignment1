# Django Multi-User Authentication System (Doctor & Patient)

This is a Django-based web application that supports **signup, login, and dashboard redirection** for two types of users:

*  Patient
*  Doctor

Each user is redirected to their respective dashboard after login, and the dashboard displays the details they submitted during signup.

---

## 🚀 Features

* User Registration with:

  * First Name, Last Name
  * Email & Username
  * Profile Picture
  * Password & Confirm Password
  * Full Address (Line1, City, State, Pincode)
  * User Type: Doctor or Patient
* Login System
* Redirect based on User Type
* Dashboards for both roles displaying user info
* Auth protection for dashboard views
* Clean, responsive form design with CSS



## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Database:** SQLite
* **Frontend:** HTML, CSS (custom)
* **Image Upload:** Pillow for profile pictures

---

## 📁 Project Structure

```
django-auth/
├── users/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── accounts/
├── static/
│   └── css/
│       └── styles.css
├── media/
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 🧰 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ajeyajaz/across_gl_assignment1.git
cd django-auth-task
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the server

```bash
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/` in your browser.

---

## 🧪 Testing the App

* Go to `/signup/` to register as a **Doctor** or **Patient**
* Then go to `/login/` to sign in
* You'll be redirected to:

  * `/doctor/dashboard/` if you're a doctor
  * `/patient/dashboard/` if you're a patient

---

## 📦 Requirements

You can generate a `requirements.txt` using:

```bash
pip freeze > requirements.txt
```

Basic requirements include:

```txt
Django>=4.0
Pillow
```

