# 📝 Django Blog

<img src=https://user-images.githubusercontent.com/50201165/109299508-d5f40300-77fa-11eb-95ed-646879615fb4.jpg width=500>

A feature-rich blog application built with Django, offering full user authentication, commenting capabilities, and editable user profiles.

## 🌟 Features

- **User Authentication:** Secure registration, login, and logout functionalities.
- **User Profiles:** Editable profiles with avatars and personal information.
- **Blog Posts:** Create, read, update, and delete posts with rich text support.
- **Commenting System:** Engage in discussions through threaded comments on posts.
- **Responsive Design:** Optimized for various devices to ensure a seamless user experience.

## 🛠️ Tech Stack

- **Backend:** Django, Python
- **Frontend:** HTML, CSS (Consider mentioning any frameworks like Bootstrap if used)
- **Database:** SQLite (for development)

## 🔧 Setup Instructions

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/blakebrandon-hub/Django-Blog.git
    cd Django-Blog
    ```

2. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser (for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the Application:**

    Open your browser and navigate to `http://127.0.0.1:8000/`

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for details.

