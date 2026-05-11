import streamlit as st
import streamlit.components.v1 as components
import os

# 1. Page Configuration
st.set_page_config(
    page_title="ITrack Dashboard",
    page_icon="📊",
    layout="wide",  # Ensures the dashboard uses the full screen width
)

# 2. Function to load the HTML file
def load_html():
    # Get the path to the HTML file relative to this script
    path = os.path.join(os.path.dirname(__file__), "ITrack_Dashboard.html")
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# 3. Display the Dashboard
try:
    html_data = load_html()
    
    # Use components.html to render the content
    # height=1000 provides enough room to see the KPIs and top of the list
    # scrolling=True allows the internal HTML scrollbars to work
    components.html(html_data, height=1200, scrolling=True)

except FileNotFoundError:
    st.error("Error: 'ITrack_Dashboard.html' not found in the repository folder.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")

# 4. (Optional) Streamlit Sidebar for instructions
with st.sidebar:
    st.title("Navigation")
    st.info("This is a Streamlit wrapper for the ITrack Dashboard.")
    if st.button("Refresh Dashboard"):
        st.rerun()
