# streamlit_app.py

import streamlit as st
import datetime
from calendar_logic import Calendar


st.set_page_config(page_title="Calendar Manager", layout="centered")
st.title("Calendar & Appointment Manager")

# Initialize calendar object
calendar = Calendar()

if 'create_event_title' not in st.session_state:
    st.session_state.create_event_title = ""
if 'create_event_date' not in st.session_state:
    st.session_state.create_event_date = datetime.date.today()
if 'create_event_start_time' not in st.session_state:
    st.session_state.create_event_start_time = datetime.datetime.now().time()
if 'create_event_end_time' not in st.session_state:
    st.session_state.create_event_end_time = (datetime.datetime.now() + datetime.timedelta(hours=1)).time()


# Create Event
st.header("Create Event")
with st.form("create_event"):
    title = st.text_input("Event Title", value=st.session_state.create_event_title, key="title_input")
    event_date = st.date_input("Event Date", value=st.session_state.create_event_date, key="date_input")
    start_time = st.time_input("Start Time", value=st.session_state.create_event_start_time, key="start_time_input")
    end_time = st.time_input("End Time", value=st.session_state.create_event_end_time, key="end_time_input")
    submitted = st.form_submit_button("Create Event")

    if submitted:
        st.session_state.create_event_title = title
        st.session_state.create_event_date = event_date
        st.session_state.create_event_start_time = start_time
        st.session_state.create_event_end_time = end_time

        start = datetime.datetime.combine(event_date, start_time)
        end = datetime.datetime.combine(event_date, end_time)
        
        if not title:
            st.error("Event title cannot be empty.")
        elif start >= end:
            st.error("Start time must be before end time.")
        else:
            success, msg = calendar.create_event(
                title,
                start.strftime('%Y-%m-%d %H:%M'),
                end.strftime('%Y-%m-%d %H:%M')
            )
            if success:
                st.success(msg)
                st.session_state.create_event_title = ""
                st.session_state.create_event_start_time = datetime.datetime.now().time()
                st.session_state.create_event_end_time = (datetime.datetime.now() + datetime.timedelta(hours=1)).time()
                st.rerun() 
            else:
                st.error(msg)


# Events Today
st.header("Events Today")
calendar = Calendar() 
events_today = calendar.list_events_for_day(datetime.datetime.now().strftime('%Y-%m-%d'))
if events_today:
    for i, e in enumerate(events_today):
        st.write(f"{i+1}. {e}")
else:
    st.info("No events today.")

# Remaining Today
st.header("Remaining Today")
calendar = Calendar() 
remaining = calendar.list_remaining_events_for_today()
if remaining:
    for i, e in enumerate(remaining):
        st.write(f"{i+1}. {e}")
else:
    st.info("No remaining events.")

# Events for Specific Date
st.header("Events for Specific Date")
calendar = Calendar() 
date_input = st.date_input("Choose a date", datetime.date.today(), key="specific")
events = calendar.list_events_for_day(date_input.strftime('%Y-%m-%d'))
if events:
    for i, e in enumerate(events):
        st.write(f"{i+1}. {e}")
else:
    st.info("No events on selected date.")

#Delete Event
st.header("Delete Event")
calendar = Calendar() 
if calendar.events:

    options = [f"{i+1}. {e.title} ({e.start_time.strftime('%Y-%m-%d %H:%M')})" for i, e in enumerate(calendar.events)]
    selected_option = st.selectbox("Choose event to delete", options, index=0 if options else None, key="delete_select")
    

    if selected_option and st.button("Delete Event"):
        try:
            index_str = selected_option.split('.')[0]
            if calendar.delete_event(index_str):
                st.success("Event deleted.")
                st.rerun() 
            else:
                st.error("Could not delete event. Please try again.")
        except Exception as e:
            st.error(f"Error processing deletion: {e}")
else:
    st.info("No events to delete.")

# Find Available Slots
st.header("Find Available Slots")
calendar = Calendar() 
slot_date = st.date_input("Date for Slot Search", datetime.date.today(), key="slot")
duration = st.number_input("Duration in minutes", 15, 180, 30)
if st.button("Find Available Slots"):
    slots = calendar.find_all_available_slots(duration, slot_date)
    if slots:
        st.success(f"{len(slots)} slots found. Showing top 5:")
        for s, e in slots[:5]:
            st.write(f"→ {s.strftime('%H:%M')} - {e.strftime('%H:%M')}") 
            st.caption(f"Duration: {(e - s).total_seconds() / 60:.0f} mins")
    else:
        st.warning("No available slots found.")