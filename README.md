CampusConnect

A Django web app with user sign-up, login, a personal dashboard, and an editable profile page, styled with Bootstrap 5.

- **Name:** Lance Angelo Reusora
- **Section:** G5
- **Course:** CSIT327

Features

- Sign-up with a success message (Django messages framework, shown as a Bootstrap alert)
- Login and logout
- Dashboard showing role, course, and member count
- Profile page built with `UpdateView`. It requires login, and users can only edit their own profile
- Role-protected admin panel (students get a 403 page)
- Bootstrap 5 loaded from the CDN, with a shared `base.html` and navbar

How to Run

Requires Python 3.12 or newer.

1. Clone the repository and open the folder:
   ```powershell
   git clone https://github.com/LanceAngeloReusora/CSIT327-G5-Reusora-LanceAngelo-FirstDjango.git
   cd CSIT327-G5-Reusora-LanceAngelo-FirstDjango
   ```
2. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```
   On macOS/Linux, use `source .venv/bin/activate` instead.
3. Install the dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Create the database tables:
   ```powershell
   python manage.py migrate
   ```
5. (Optional) Create an admin account:
   ```powershell
   python manage.py createsuperuser
   ```
   Then open `/admin/` and set the user's Role to Administrator to access the admin panel.
6. Start the server and open http://127.0.0.1:8000/:
   ```powershell
   python manage.py runserver
   ```

Pages

| URL | Page |
| --- | --- |
| `/accounts/signup/` | Sign up |
| `/accounts/login/` | Log in |
| `/` | Dashboard (login required) |
| `/accounts/profile/` | Edit profile (login required) |
| `/admin-panel/` | Admin panel (administrators only) |
