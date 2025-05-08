# [VibeCheck](https://vibe-check-final.netlify.app/)
### Overview
Many people struggle to track their moods consistently, which prevents them from recognizing emotional patterns and improving mental well-being. VibeCheck simplifies this process with an intuitive emoji-based system, AI-driven insights, and web scraped articles with self-care suggestions.
### Project Wireframe
<img width="1392" alt="Screenshot of wireframe for VibeCheck" src="https://github.com/user-attachments/assets/8757f755-52bd-4eb9-b12e-54646a908a48" />

### Features
- User authentication (email/password, OAuth)
- Mood logging via emoji and optional journal entry
- CRUD ops for mood logs
- Sentiment analysis for journal entries
- AI journal prompt generation
- Self-care articles via webscraping
- Pagination and search (keyword, date, sentiment)
- Data visualization via Tableau
- Client-side validation
- Error handling and logging
- Google CAPTCHA anti-bot and rate limiting

### Technologies Used
- Frontend: React (mood input, data visualization)
- Backend: Flask (API, webscraping)
- Database: SQLite (user mood logs and self-care webscraped articles/tips)
- APIs/Libraries: BeautifulSoup, openAI and Tableau
- CSS Framework: Tailwind

### Installation Instructions
Prerequisite: Python 3.13.1
1. Clone the repository <br>
`git clone https://github.com/stmcpeters/VibeCheck.git` <br>
`cd vibecheck`
2. Set up the Flask backend
    - Create and activate a virtual environment <br>
`python3 -m venv venv` <br>
`source venv/bin/activate` # On Windows: venv\Scripts\activate
    - Install dependencies <br>
`pip install -r requirements.txt`
    - Add environment variables for database <br>
    Create a `.env` file inside the `server` folder with: <br>
`DB_USERNAME='<username>'` <br>
`DB_PASSWORD='<password>'`
    - Run the Flask server <br>
`python3 app.py`
3. Set up the React Frontend <br>
`cd client` <br>
`npm install` <br>
`npm run dev`

### Stretch Goals/Help Wanted
- Daily mood streak tracker
- Notification reminder to log mood
- AI chatbot
- Custom journal prompt creation
- Upload photos with mood logs

### Contributing
Contributions are welcomed to this project! If you have an idea for a new feature or a bug fix, please open an issue or a pull request.
