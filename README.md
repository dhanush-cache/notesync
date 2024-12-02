
# Notesync

The API for a simple note-sharing application.

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.7+
- [Pipenv](https://pipenv.pypa.io/en/latest/)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/dhanush-cache/notesync.git
   cd notesync
   ```

2. Install dependencies:
   ```bash
   pipenv install
   ```

3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the seed script:
   ```bash
   python -m scripts.seed
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

### You're all set! 🎉

Navigate to `http://127.0.0.1:8000/content` in your browser to view the project.
