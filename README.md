# MydockerProject - Phase 4

## Project Overview
This project is part of the advanced coursework for implementing a web-based dashboard using Flask and PostgreSQL within a Docker environment. This phase involves migrating the PostgreSQL database into a Docker container and ensuring all functionalities from previous phases remain intact.

## Structure
The project is structured as follows:

- `Docker/`: Contains Dockerfile and requirements for Python Flask application.
- `DB/`: Contains database backup and initialization scripts.
- `webpages/`: Contains Flask application files and HTML templates.
- `static/`: Contains static files like CSS and JavaScript.
- `templates/`: Contains HTML templates for the Flask application.

## Getting Started

### Prerequisites
- Docker
- Git
- Access to a command-line interface

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/OffshoreFlyer96/3010-proj-grp-3.git
   cd 3010-proj-grp-3
   git checkout phase4

## Project Structure
MydockerProject/
│
├── Docker/
│   ├── Dockerfile             # Dockerfile to build the container image
│   └── requirements.txt       # Python libraries requirements
│
├── DB/
│   ├── backup.sql             # pg_dumpall or pg_dump backup of your database
│   └── init-db.sh             # Script to initialize the PostgreSQL database
│
├── webpages/                  # Folder to contain all web development files
│   ├── static/                # CSS, JS, and image files
│   │   └── style.css
│   ├── templates/             # HTML (Jinja2) templates
│   │   ├── index.html
│   │   ├── courses.html
│   │   └── fte.html
│   └── app.py                 # Flask application
│
├── .gitignore                 # Specifies intentionally untracked files to ignore
└── README.md                  # Project description and instructions


2. **Build the Docker Container**
    Navigate to the Docker directory and build the container:

    bash

cd Docker
docker build -t my-flask-app .
docker build -t my-flsk-app .
docker run -d -p 5000:5000 --name my-flsk-app my-flsk-app
docker logs my-flsk-app
# To stop Docker Container and remove it:
docker stop my-flsk-app
docker rm my-flsk-app

# Navigate Webproject using this links:

3. **Run the Docker Container**

bash

docker run -d -p 80:5000 --name my-flask-app my-flask-app

4. **Initialize the Database**
Ensure the PostgreSQL service is up and then execute the init script:

bash

docker exec -it my-flask-app /bin/bash
./DB/init-db.sh

5. **Restore the Database**

bash

    cat DB/backup.sql | docker exec -i my-flask-app psql -U webuser1 -d cscdashboard

### Usage
Access the web application via `http://localhost:5000` or `(http://0.0.0.0:5000)` or `(http://127.0.0.1:5000)`.
Features

    User-friendly web interface to interact with the database.
    Automatic calculation of FTE (Full-Time Equivalent) for faculty based on their course load.
    Search functionality to filter faculty records by name, year, or semester.

### Contributions

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

    Fork the Project
    Create your Feature Branch (git checkout -b feature/AmazingFeature)
    Commit your Changes (git commit -m 'Add some AmazingFeature')
    Push to the Branch (git push origin feature/AmazingFeature)
    Open a Pull Request

### License

Distributed under the MIT License. See LICENSE for more information.
Contact

### Contact: Group 3

Project Link: https://github.com/OffshoreFlyer96/3010-proj-grp-3


