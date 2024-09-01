import streamlit as st
import datetime
import random

def dummy_water_zone(duration_minutes):
    # Simulate watering
    progress_bar = st.progress(0)
    for i in range(100):
        # Simulate progress
        progress_bar.progress(i + 1)
        st.experimental_rerun()

def get_next_watering_time():
    # Dummy function to return a random future time
    now = datetime.datetime.now()
    random_hours = random.randint(1, 24)
    next_time = now + datetime.timedelta(hours=random_hours)
    return next_time.strftime("%H:%M")

def dummy_toggle_scheduling():
    # Dummy function to toggle scheduling
    st.session_state.scheduling = not st.session_state.scheduling

# Initialize session state
if 'valve_state' not in st.session_state:
    st.session_state.valve_state = False
if 'scheduling' not in st.session_state:
    st.session_state.scheduling = True

st.title('Irrigation Control System (Dummy)')

if st.button('Water Now'):
    duration = st.slider('Watering duration (minutes)', 1, 30, 5)
    st.write(f"Watering for {duration} minutes...")
    dummy_water_zone(duration)
    st.write("Watering complete!")

st.write(f"Next scheduled watering: {get_next_watering_time()}")

if st.button('Toggle Scheduling'):
    dummy_toggle_scheduling()
    if st.session_state.scheduling:
        st.write("Scheduling enabled")
    else:
        st.write("Scheduling disabled")

st.write("System Status:")
st.write(f"Valve state: {'Open' if st.session_state.valve_state else 'Closed'}")

st.write("Recent Log Entries:")
dummy_log = [
    "2023-09-01 06:00:00 - Watering started",
    "2023-09-01 06:05:00 - Watering completed",
    "2023-09-02 06:00:00 - Watering started",
    "2023-09-02 06:05:00 - Watering completed",
    "2023-09-03 06:00:00 - Watering skipped (rain detected)"
]
st.code("\n".join(dummy_log))

if st.button('Toggle Valve'):
    st.session_state.valve_state = not st.session_state.valve_state
    st.write(f"Valve {'opened' if st.session_state.valve_state else 'closed'}")

if st.button('Shutdown System'):
    st.write("System shut down. You can close this window.")
    st.stop()
