import streamlit as st
import datetime
import random
import plotly.graph_objs as go

# Set page config
st.set_page_config(page_title="Smart Irrigation System", page_icon="💧", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        border-radius: 20px;
    }
    .stProgress .st-bo {
        background-color: #3498db;
    }
    .css-1v0mbdj.ebxwdo61 {
        width: 100%;
        border-radius: 20px;
    }
    .stats-box {
        background-color: #f0f2f6;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Dummy functions
def dummy_water_zone(duration_minutes):
    progress_bar = st.progress(0)
    for i in range(100):
        progress_bar.progress(i + 1)
        st.experimental_rerun()

def get_next_watering_time():
    now = datetime.datetime.now()
    random_hours = random.randint(1, 24)
    next_time = now + datetime.timedelta(hours=random_hours)
    return next_time.strftime("%H:%M")

def dummy_toggle_scheduling():
    st.session_state.scheduling = not st.session_state.scheduling

# Initialize session state
if 'valve_state' not in st.session_state:
    st.session_state.valve_state = False
if 'scheduling' not in st.session_state:
    st.session_state.scheduling = True
if 'water_usage' not in st.session_state:
    st.session_state.water_usage = [random.randint(50, 100) for _ in range(7)]

# Main app layout
st.title('🌿 Smart Irrigation Control System')

# Sidebar
with st.sidebar:
    st.header("System Controls")
    if st.button('💧 Water Now'):
        duration = st.slider('Duration (minutes)', 1, 30, 5)
        st.write(f"Watering for {duration} minutes...")
        dummy_water_zone(duration)
        st.success("Watering complete!")
    
    st.write("---")
    
    if st.button('🔄 Toggle Scheduling'):
        dummy_toggle_scheduling()
        if st.session_state.scheduling:
            st.success("Scheduling enabled")
        else:
            st.warning("Scheduling disabled")
    
    st.write("---")
    
    if st.button('🚰 Toggle Valve'):
        st.session_state.valve_state = not st.session_state.valve_state
        if st.session_state.valve_state:
            st.success("Valve opened")
        else:
            st.info("Valve closed")

# Main content
col1, col2 = st.columns(2)

with col1:
    st.subheader("System Status")
    st.markdown(f"""
    <div class="stats-box">
        <h3>Valve State</h3>
        <p style="font-size: 24px; color: {'green' if st.session_state.valve_state else 'red'};">
            {'Open' if st.session_state.valve_state else 'Closed'}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="stats-box">
        <h3>Next Scheduled Watering</h3>
        <p style="font-size: 24px;">{get_next_watering_time()}</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.subheader("Water Usage (Last 7 Days)")
    fig = go.Figure(data=[go.Bar(y=st.session_state.water_usage)])
    fig.update_layout(title="Daily Water Consumption", xaxis_title="Days Ago", yaxis_title="Liters")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Watering Schedule")
schedule_date = st.date_input("Select date for watering schedule")
schedule_time = st.time_input("Select time for watering")
st.write(f"Scheduled watering for: {schedule_date} at {schedule_time}")

st.subheader("System Log")
with st.expander("View Recent Log Entries"):
    dummy_log = [
        "2023-09-01 06:00:00 - Watering started",
        "2023-09-01 06:05:00 - Watering completed",
        "2023-09-02 06:00:00 - Watering started",
        "2023-09-02 06:05:00 - Watering completed",
        "2023-09-03 06:00:00 - Watering skipped (rain detected)"
    ]
    st.code("\n".join(dummy_log))

# Footer
st.markdown("---")
st.markdown("© 2023 Smart Irrigation Systems Inc. | [Documentation](https://example.com) | [Support](mailto:support@example.com)")
