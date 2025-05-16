Project Overview
Huluflix Prime is a Flask-based web application that allows users to browse, search, and view detailed information about movies and shows available. Built using Python, SQLite, Flask, SQLAlchemy, and Bootstrap, the application supports pagination, and poster integration.

Design
1.	Backend: Flask web framework with SQLAlchemy ORM for database modeling and management.
2.	Database Models:
•	Title: Represents a show or movie, with fields like title, type, release year, etc.
•	Genre: Many-to-many relationship with titles.
3.	Frontend: HTML templates using Jinja2 and Bootstrap for clean, responsive layout.
4.	Poster Images: External URLs added via a supplemental CSV (poster_links.csv).
Development
1.	Designed modular Python files for models, routes, and data loading.
2.	Implemented pagination and filtering on the homepage.
3.	Integrated full-text search using SQLAlchemy.
4.	Ensured full HTML accessibility and styling
Implementation
1.	Data was loaded from hulu_titles.csv using Pandas.
2.	Poster images were merged by mapping title names to URLs from poster_links.csv.
3.	Custom Flask routes render templates using Jinja2 to dynamically display content.
4.	Error handling (404 pages) and template inheritance were implemented for maintainability.
Installation
Steps to install and run:
1.	Clone the repository:
   ```bash
git clone https://github.com/jst-uyi/flask_project.git
```
3.	Install dependencies:
```bash
pip install -r requirements.txt
```
3.	Run the data loader:
   ```bash
python load_data.py
```
5.	Start the Flask server:
   ```bash
python app.py
```
if running on codio, copy codio box url (e.g https://tennissigma-mondaytaxi-5000.codio-box.uk)

Usage
•	Navigate to the home page to browse content.
•	Use the search bar to find specific titles.
•	Click a title to view detailed information, including description, rating, genres, and poster.
•	Use pagination to move through the list of results.

Testing
•	Manually tested routes, error pages, pagination, and search.
•	Verified correct linking of posters and genre associations.
