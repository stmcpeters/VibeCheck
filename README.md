# [VibeCheck](https://vibe-check-final.netlify.app/)
### Table of Contents
- [Overview](#overview)
- [Demo](#demo)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation Instructions](#installation-instructions)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
### Overview
Many people struggle to track their moods consistently, which prevents them from recognizing emotional patterns and improving mental well-being. VibeCheck simplifies this process with an intuitive emoji-based system, AI-driven insights, and web scraped articles with self-care suggestions.
### Demo


https://github.com/user-attachments/assets/abed83d4-befe-487c-b850-9ce10aa8deea


### Features
- User authentication (login and registration).
- Mood logging with AI-driven sentiment analysis.
- Interactive chart to visualize mood trends over time.
- Articles section with curated content for mental health.
- User authentication (email/password)
- Client-side validation
- Error handling and logging

### Technologies Used
- **Frontend**:
  - React
  - DaisyUI (Tailwind CSS)
  - Chart.js for data visualization
- **Backend**:
  - Flask
  - PostgreSQL
  - OpenAI API (for sentiment analysis)
- **Other Tools**:
  - Vite (for development and build)
  - BeautifulSoup (for web scraping)
  - dotenv (for environment variable management)

### Installation Instructions
Prerequisite: Python 3.13.1
1. Clone the repository <br>
`git clone https://github.com/stmcpeters/VibeCheck.git` <br>
`cd vibecheck`
2. Set up the Flask backend
    - Create and activate a virtual environment <br>
`python3 -m venv venv` <br>
`source venv/bin/activate` # On Windows: venv\Scripts\activate
    - Navigate to the server <br>
`cd server`
    - Install dependencies <br>
`pip install -r requirements.txt`
    - Register for an API key from [OpenAI](https://openai.com/)
    - Add environment variables for application <br>
    Copy the `.env.example` file and rename it to `.env` <br>
    Fill in the required values in the `.env` file
    - Set up the database:<br>
   Connect to your PostgreSQL database: <br>
     `psql -U <your_username> -d <your_database>`<br>
   Run the `db.sql` file to create the schema: <br>
     `\i path/to/db.sql`<br>
    - Run the Flask server <br>
`python3 app.py`
3. Set up the React Frontend <br>
`cd client` <br>
`npm install` <br>
`npm run dev`

### Running Tests

This project uses `pytest` for testing.

1. Run all tests: <br>
   `pytest`

2. View the test results in the terminal.

Optional:
- To check test coverage, install `pytest-cov`:<br>
  `pip install pytest-cov`

- Run tests with coverage:<br>
  `pytest --cov=vibecheck`

### Contributing
Contributions are welcomed to this project! If you have an idea for a new feature or a bug fix, please open an issue or a pull request.
