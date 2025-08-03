import streamlit as st

# Configure page
st.set_page_config(
    page_title="Singapore Wage Insights - Welcome",
    page_icon="💰", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Simple welcome page directing users to the home page
st.markdown("""
# Welcome to Singapore Wage Insights 💰

### Please navigate to the **Home** page from the sidebar to access the full wage analysis tool.

""")

st.info("👈 Click **Home** in the sidebar to get started with Singapore wage data analysis.")

# Add some basic information
st.markdown("""
---

## Quick Overview

Singapore Wage Insights provides comprehensive salary and wage analysis across:

- 📊 **Interactive Charts** - Visual wage trends from 2021-2024
- 🔍 **Occupation Search** - Find specific job roles and salaries  
- 🏢 **Industry Analysis** - Compare wages across different sectors
- 📈 **Growth Rates** - Year-over-year salary progression data
- 💾 **Data Downloads** - Export data for further analysis

**Data Source:** Official Singapore Government Statistics (2021-2024)

---

### Navigation
- **Home** - Main wage analysis tool
- **Privacy** - Privacy policy and data handling
- **Terms** - Terms of service and usage guidelines
""")