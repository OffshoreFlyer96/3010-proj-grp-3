# CS Department Dashboard - Phase 2

## Project Overview

Welcome to the CS Department Dashboard Phase 2! This project is an extension of our ongoing efforts to create a comprehensive dashboard for managing and displaying information about the faculty in the Computer Science Department at ECU. In this phase, we've introduced a web application to dynamically showcase faculty details from a PostgreSQL database.

## Table of Contents

- [Requirements](#requirements)
- [Installation Guide](#installation-guide)
- [Functionality Overview](#functionality-overview)
- [Project Structure](#project-structure)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Requirements

Before running the application, please ensure you have the following tools and dependencies installed:

- [Python](https://www.python.org/downloads/) (version 3.6 or higher)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)

You can install Python dependencies using:

```bash
Installation Guide
To set up the CS Department Dashboard Phase 2, follow these steps:

Install the required Python dependencies:
pip install -r requirements.txt

Clone the repository:
git clone https://github.com/OffshoreFlyer96/3010-proj-grp-3.git

Configure the PostgreSQL database:
Create a PostgreSQL database named csdashboard.
Import the provided SQL dump into the database:
psql -U your-username -d csdashboard < csdashboard_dump.sql

Functionality Overview
The CS Department Dashboard Phase 2 introduces the following key features:

Dynamic Web Application: A Flask-powered web application that dynamically displays faculty information.
Pagination: Faculty data is presented in paginated form for a user-friendly experience.
Responsive Design: HTML and CSS files have been meticulously crafted to ensure a seamless experience across various devices.
Project Structure
app.py: The main Flask application file.
templates/: Folder containing HTML templates.
static/: Folder containing static assets such as CSS stylesheets.
Database Setup
Make sure the PostgreSQL database is set up as described in the installation steps. The provided SQL dump (csdashboard_dump.sql) contains sample data for testing.

Usage
Run the application:

python app.py

Access the dashboard at:

http://localhost:5000/
http://192.168.56.10:5000/
Contributing
We welcome contributions to enhance and expand the functionality of the CS Department Dashboard. Feel free to fork the repository, create a new branch, and submit pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.
