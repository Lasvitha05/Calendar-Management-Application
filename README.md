

# Calendar & Appointment Manager

A user-friendly **Streamlit web application** to create, view, and manage daily events and appointments. Built using Python, this tool allows users to store events in an Excel file, view available time slots, and manage their schedule — all from a clean, interactive interface.

---

##  Features

- Create new events with title, date, start time, and end time
- View:
  - Today's events
  - Remaining events for the day
  - Events for a specific date
- Delete selected events
- Find all available time slots on a selected day for a specific duration
- Simple and clean UI with real-time feedback

---

## Tools & Technologies

- **Python 3**
- **Streamlit** – For building the interactive web UI
- **openpyxl** – For reading and writing Excel files
- **datetime** – For time-based operations and validations

---

## Project Structure

```bash
calendar-appointment-manager/
├── streamlit_app.py           # Main Streamlit frontend application
├── calendar_logic.py          # Backend logic for managing events
├── calendar.xlsx              # Excel file where events are stored
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation

```
## How to Run This App Locally
1. Clone the Repository
   
- git clone (https://github.com/Lasvitha05/Calendar-Management-Application)
- cd Calendar-Management-Application

2. Install Dependencies
   - pip install -r requirements.txt
3. Run the Streamlit App
   - streamlit run streamlit_app.py 
