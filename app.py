import streamlit as strl
import streamlit.components.v1 as component_components

strl.set_page_config(
    page_title="Quantum Interferometer",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Read the HTML application data directly from disk space
with open("index.html", "r", encoding="utf-8") as html_reader:
    raw_source_code = html_reader.read()

strl.title("Advanced QED Research Portal")
strl.caption("Production Build Engine Integrated Matrix Framework Tools")

# Embed the raw simulation canvas securely inside Streamlit's iframe canvas wrapper
component_components.html(
    raw_source_code,
    height=2800,       # Sets total height clearance to ensure all components render without clipping
    scrolling=True    # Enables scrolling inside the component container if needed
)