import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from data_loader import load_all_wage_data, get_industries
import io
import streamlit_analytics
import json
import os
from datetime import datetime
from collections import Counter

# Configure page
st.set_page_config(
    page_title="Singapore Wage Insights - Salary Trends & Analysis (2021-2024)",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="auto",  # Changed to auto for better mobile experience
    menu_items={
        'Get Help': 'https://singaporewage.com/help',
        'Report a bug': "https://singaporewage.com/contact",
        'About': "Singapore's premier wage analysis platform. Data sourced from official government statistics."
    }
)


# SEO Meta Tags and Structured Data
st.markdown("""
<!-- SEO Meta Tags -->
<meta name="description" content="Explore Singapore wage trends across occupations with interactive charts and data insights. Based on official government data (2021-2024).">
<meta name="keywords" content="Singapore wages, salary trends, jobs, occupations, wage analysis, Singapore salary, income data, employment statistics, pay scale Singapore">
<meta name="author" content="Singapore Wage Insights">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://singaporewage.com/">

<!-- Open Graph / Facebook -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://singaporewage.com/">
<meta property="og:title" content="Singapore Wage Insights - Salary Trends & Analysis (2021-2024)">
<meta property="og:description" content="Explore Singapore wage trends across occupations with interactive charts and data insights. Based on official government data.">
<meta property="og:image" content="https://singaporewage.com/assets/singapore-wage-preview.png">
<meta property="og:site_name" content="Singapore Wage Insights">

<!-- Twitter -->
<meta property="twitter:card" content="summary_large_image">
<meta property="twitter:url" content="https://singaporewage.com/">
<meta property="twitter:title" content="Singapore Wage Insights - Salary Trends & Analysis">
<meta property="twitter:description" content="Explore Singapore wage trends across occupations with interactive charts and data insights.">
<meta property="twitter:image" content="https://singaporewage.com/assets/singapore-wage-preview.png">

<!-- Structured Data - JSON-LD -->
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Singapore Wage Insights",
    "alternateName": "SG Wage Analysis",
    "url": "https://singaporewage.com/",
    "description": "Singapore's premier platform for wage analysis and salary trends across all occupations",
    "potentialAction": {
        "@type": "SearchAction",
        "target": "https://singaporewage.com/?search={search_term_string}",
        "query-input": "required name=search_term_string"
    }
}
</script>

<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Singapore Wage Insights",
    "url": "https://singaporewage.com/",
    "logo": "https://singaporewage.com/assets/logo.png",
    "description": "Comprehensive wage and salary analysis platform for Singapore",
    "sameAs": [
        "https://twitter.com/sgwageinsights",
        "https://www.linkedin.com/company/singapore-wage-insights"
    ]
}
</script>

<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "DataCatalog",
    "name": "Singapore Wage Database",
    "description": "Comprehensive database of Singapore wages and salaries from 2021-2024",
    "url": "https://singaporewage.com/",
    "keywords": "wages, salaries, Singapore, employment, statistics",
    "creator": {
        "@type": "Organization",
        "name": "Singapore Wage Insights"
    },
    "temporalCoverage": "2021/2024"
}
</script>
""", unsafe_allow_html=True)

# Custom CSS for responsive design
st.markdown("""
<style>
    /* Base styles */
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        margin: 5px;
    }
    
    .main > div {
        padding-top: 2rem;
    }
    
    /* Responsive header styles */
    .main-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .main-header h1 {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    
    .main-header p {
        font-size: 1.1rem;
        color: #666;
        margin-bottom: 1rem;
    }
    
    /* Mobile responsiveness - 320px to 768px */
    @media (max-width: 768px) {
        .main > div {
            padding-top: 1rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
        
        .main-header h1 {
            font-size: 1.8rem;
        }
        
        .main-header p {
            font-size: 1rem;
        }
        
        .stMetric {
            padding: 10px;
            margin: 3px;
        }
        
        /* Force sidebar to collapse on mobile */
        .css-1d391kg {
            width: 100%;
        }
        
        /* Make selectboxes full width */
        .stSelectbox > div > div {
            width: 100% !important;
        }
        
        /* Stack columns on mobile */
        .row-widget.stHorizontal {
            flex-direction: column;
        }
        
        .row-widget.stHorizontal > div {
            width: 100% !important;
            margin-bottom: 1rem;
        }
        
        /* Responsive table container */
        .dataframe {
            overflow-x: auto;
            white-space: nowrap;
        }
        
        /* Chart responsiveness */
        .js-plotly-plot {
            width: 100% !important;
            height: auto !important;
        }
        
        /* Mobile-specific spacing */
        .element-container {
            margin-bottom: 1rem;
        }
    }
    
    /* Tablet responsiveness - 768px to 1024px */
    @media (min-width: 768px) and (max-width: 1024px) {
        .main > div {
            padding-left: 1.5rem;
            padding-right: 1.5rem;
        }
        
        .main-header h1 {
            font-size: 2.2rem;
        }
        
        .stMetric {
            padding: 12px;
        }
    }
    
    /* Desktop styles - 1024px and up */
    @media (min-width: 1024px) {
        .main-header h1 {
            font-size: 2.5rem;
        }
    }
    
    /* Ensure tables don't overflow */
    .stDataFrame {
        width: 100%;
        overflow-x: auto;
    }
    
    .stDataFrame table {
        min-width: 100%;
        width: max-content;
    }
    
    /* Button responsiveness */
    .stButton > button {
        width: 100% !important;
        padding: 0.5rem 1rem;
        font-size: 0.9rem;
    }
    
    /* Download section responsiveness */
    @media (max-width: 768px) {
        .stButton > button {
            margin-bottom: 0.5rem;
            font-size: 0.8rem;
        }
    }
    
    /* Plotly chart container fix */
    .user-select-none {
        width: 100% !important;
    }
    
    /* Mobile-specific adjustments */
    @media (max-width: 480px) {
        .main-header h1 {
            font-size: 1.5rem;
        }
        
        .main-header p {
            font-size: 0.9rem;
        }
        
        .stTabs [data-baseweb="tab"] {
            font-size: 0.8rem;
            padding: 0.3rem 0.6rem;
        }
    }
    
    /* Support Section Styles */
    .support-section {
        background: linear-gradient(135deg, #2c3e50, #34495e);
        padding: 3rem 2rem;
        margin: 2rem 0;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .support-section h2 {
        font-size: 2.2rem;
        margin-bottom: 1rem;
        color: white;
        font-weight: 600;
    }
    
    .support-section p {
        font-size: 1.2rem;
        margin-bottom: 2rem;
        color: #ecf0f1;
        line-height: 1.6;
    }
    
    .coffee-button {
        display: inline-block;
        background: linear-gradient(45deg, #f39c12, #e67e22);
        color: #2c3e50 !important;
        padding: 15px 30px;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: bold;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(243, 156, 18, 0.4);
        border: none;
        cursor: pointer;
    }
    
    .coffee-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(243, 156, 18, 0.6);
        background: linear-gradient(45deg, #e67e22, #d35400);
        color: #2c3e50 !important;
        text-decoration: none !important;
    }
    
    .coffee-button:active {
        transform: translateY(0);
    }
    
    /* Responsive support section */
    @media (max-width: 768px) {
        .support-section {
            padding: 2rem 1.5rem;
            margin: 1.5rem 0;
        }
        
        .support-section h2 {
            font-size: 1.8rem;
        }
        
        .support-section p {
            font-size: 1rem;
            margin-bottom: 1.5rem;
        }
        
        .coffee-button {
            padding: 12px 25px;
            font-size: 1rem;
        }
    }
    
    @media (max-width: 480px) {
        .support-section {
            padding: 2rem 1rem;
        }
        
        .support-section h2 {
            font-size: 1.6rem;
        }
        
        .support-section p {
            font-size: 0.9rem;
        }
        
        .coffee-button {
            padding: 10px 20px;
            font-size: 0.9rem;
        }
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and prepare wage data with caching."""
    df = load_all_wage_data()
    
    # Rename columns to match requirements
    df = df.rename(columns={
        'Basic_P25': 'P25_Basic',
        'Basic_Median': 'Median_Basic',
        'Basic_P75': 'P75_Basic',
        'Gross_P25': 'P25_Gross',
        'Gross_Median': 'Median_Gross',
        'Gross_P75': 'P75_Gross'
    })
    
    return df

@st.cache_data
def get_unique_occupations(df):
    """Get sorted list of unique occupations."""
    return sorted(df['Occupation'].unique())

def filter_occupations(df, search_term):
    """Filter occupations based on search term."""
    if not search_term:
        return get_unique_occupations(df)
    
    occupations = get_unique_occupations(df)
    search_lower = search_term.lower()
    
    # Filter occupations that contain the search term
    filtered = [occ for occ in occupations if search_lower in occ.lower()]
    
    # Sort by relevance (starts with search term first)
    starts_with = [occ for occ in filtered if occ.lower().startswith(search_lower)]
    contains = [occ for occ in filtered if not occ.lower().startswith(search_lower)]
    
    return starts_with + contains

def calculate_yoy_growth(df):
    """Calculate year-over-year growth rates."""
    if len(df) < 2:
        return None
    
    df = df.sort_values('Year')
    growth_data = []
    
    for i in range(1, len(df)):
        prev_year = df.iloc[i-1]
        curr_year = df.iloc[i]
        
        median_basic_growth = None
        median_gross_growth = None
        
        if pd.notna(prev_year['Median_Basic']) and pd.notna(curr_year['Median_Basic']) and prev_year['Median_Basic'] > 0:
            median_basic_growth = ((curr_year['Median_Basic'] - prev_year['Median_Basic']) / prev_year['Median_Basic']) * 100
        
        if pd.notna(prev_year['Median_Gross']) and pd.notna(curr_year['Median_Gross']) and prev_year['Median_Gross'] > 0:
            median_gross_growth = ((curr_year['Median_Gross'] - prev_year['Median_Gross']) / prev_year['Median_Gross']) * 100
        
        growth_data.append({
            'Period': f"{prev_year['Year']}-{curr_year['Year']}",
            'Basic Wage Growth (%)': median_basic_growth,
            'Gross Wage Growth (%)': median_gross_growth
        })
    
    return pd.DataFrame(growth_data)

def create_wage_chart(data_list, wage_type, comparison_mode=False):
    """Create interactive line chart for wage trends."""
    
    fig = go.Figure()
    
    # Color palette for multiple occupations
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
    
    for idx, (occupation, df) in enumerate(data_list):
        color = colors[idx % len(colors)] if comparison_mode else '#1f77b4'
        
        # Prepare data
        df_sorted = df.sort_values('Year')
        years = df_sorted['Year'].values
        
        # Add traces based on wage type
        wage_suffix = '_Basic' if wage_type == 'Basic' else '_Gross'
        
        # Median line
        median_values = df_sorted[f'Median{wage_suffix}'].values
        fig.add_trace(go.Scatter(
            x=years,
            y=median_values,
            mode='lines+markers',
            name=f'{occupation} - Median' if comparison_mode else 'Median',
            line=dict(color=color, width=3),
            marker=dict(size=8)
        ))
        
        # P25 line
        p25_values = df_sorted[f'P25{wage_suffix}'].values
        fig.add_trace(go.Scatter(
            x=years,
            y=p25_values,
            mode='lines+markers',
            name=f'{occupation} - P25' if comparison_mode else '25th Percentile',
            line=dict(color=color, width=2, dash='dash'),
            marker=dict(size=6)
        ))
        
        # P75 line
        p75_values = df_sorted[f'P75{wage_suffix}'].values
        fig.add_trace(go.Scatter(
            x=years,
            y=p75_values,
            mode='lines+markers',
            name=f'{occupation} - P75' if comparison_mode else '75th Percentile',
            line=dict(color=color, width=2, dash='dot'),
            marker=dict(size=6)
        ))
        
        # Add wage range fill (only if not in comparison mode)
        if not comparison_mode:
            fig.add_trace(go.Scatter(
                x=np.concatenate([years, years[::-1]]),
                y=np.concatenate([p25_values, p75_values[::-1]]),
                fill='toself',
                fillcolor=f'rgba(31, 119, 180, 0.2)',
                line=dict(color='rgba(255,255,255,0)'),
                hoverinfo='skip',
                showlegend=False
            ))
    
    # Update layout
    title = f"{wage_type} Wage Trends"
    if comparison_mode and len(data_list) > 1:
        title += " - Comparison"
    
    fig.update_layout(
        title=title,
        xaxis_title='Year',
        yaxis_title=f'{wage_type} Wage (SGD)',
        hovermode='x unified',
        height=500,
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),
        # Format y-axis as currency
        yaxis=dict(tickformat='$,.0f'),
        # Set x-axis to show only integer years
        xaxis=dict(
            tickmode='array',
            tickvals=sorted(data_list[0][1]['Year'].unique())
        )
    )
    
    return fig

def show_analytics_dashboard():
    """Display custom analytics dashboard for admin users."""
    st.title("📊 Singapore Wage App Analytics Dashboard")
    st.markdown("---")
    
    # Check for analytics data file
    if not os.path.exists("analytics_data.json"):
        st.warning("No analytics data available yet. Start using the app to generate data.")
        return
    
    # Load analytics data
    try:
        with open("analytics_data.json", "r") as f:
            analytics_data = json.load(f)
    except Exception as e:
        st.error(f"Error loading analytics data: {e}")
        return
    
    # Overview metrics
    col1, col2, col3, col4 = st.columns(4)
    
    # Calculate total interactions
    total_interactions = sum(analytics_data.get("counts", {}).values())
    
    with col1:
        st.metric("Total Page Views", analytics_data.get("total_pageviews", 0))
    with col2:
        st.metric("Total Interactions", total_interactions)
    with col3:
        st.metric("Unique Widgets Used", len(analytics_data.get("counts", {})))
    with col4:
        # Calculate average interactions per session
        avg_interactions = total_interactions / max(analytics_data.get("total_pageviews", 1), 1)
        st.metric("Avg Interactions/Session", f"{avg_interactions:.1f}")
    
    st.markdown("---")
    
    # Create two columns for charts
    col_left, col_right = st.columns(2)
    
    with col_left:
        # Widget usage statistics
        st.subheader("📈 Widget Usage Statistics")
        counts = analytics_data.get("counts", {})
        if counts:
            # Process widget data
            widget_df = pd.DataFrame(list(counts.items()), columns=['Widget', 'Count'])
            widget_df = widget_df.sort_values('Count', ascending=True).tail(15)
            
            # Create horizontal bar chart
            fig_widgets = px.bar(
                widget_df, 
                x='Count', 
                y='Widget', 
                orientation='h',
                title="Top 15 Most Used Features",
                color='Count',
                color_continuous_scale='Blues'
            )
            fig_widgets.update_layout(height=600, showlegend=False)
            st.plotly_chart(fig_widgets, use_container_width=True)
        else:
            st.info("No widget interaction data available yet.")
    
    with col_right:
        # Occupation selection analysis
        st.subheader("🔍 Popular Occupations")
        
        # Extract occupation selections from widget data
        occupation_data = {}
        for widget, count in counts.items():
            if "Choose an occupation" in widget or "Choose up to 3 occupations" in widget:
                # Try to extract occupation name from widget string
                if " - " in widget:
                    parts = widget.split(" - ")
                    if len(parts) > 1:
                        occupation = parts[1].strip()
                        if occupation and occupation != "-- Select an occupation --":
                            occupation_data[occupation] = occupation_data.get(occupation, 0) + count
        
        if occupation_data:
            # Get top 10 occupations
            top_occupations = dict(sorted(occupation_data.items(), key=lambda x: x[1], reverse=True)[:10])
            occ_df = pd.DataFrame(list(top_occupations.items()), columns=['Occupation', 'Selections'])
            
            # Create pie chart
            fig_occ = px.pie(
                occ_df, 
                values='Selections', 
                names='Occupation',
                title="Top 10 Selected Occupations"
            )
            fig_occ.update_traces(textposition='inside', textinfo='percent+label')
            fig_occ.update_layout(height=600)
            st.plotly_chart(fig_occ, use_container_width=True)
        else:
            st.info("No occupation selection data available yet.")
    
    st.markdown("---")
    
    # Additional insights
    col_insights1, col_insights2 = st.columns(2)
    
    with col_insights1:
        st.subheader("💡 Feature Usage Insights")
        
        # Analyze feature usage
        comparison_mode_count = 0
        basic_wage_count = 0
        gross_wage_count = 0
        csv_downloads = 0
        png_downloads = 0
        
        for widget, count in counts.items():
            if "Enable Comparison Mode" in widget:
                comparison_mode_count += count
            elif "Select Wage Type - Basic" in widget:
                basic_wage_count += count
            elif "Select Wage Type - Gross" in widget:
                gross_wage_count += count
            elif "Download Data as CSV" in widget:
                csv_downloads += count
            elif "Download Chart as PNG" in widget:
                png_downloads += count
        
        # Display insights
        st.metric("Comparison Mode Used", comparison_mode_count)
        
        wage_type_data = {
            'Wage Type': ['Basic', 'Gross'],
            'Selections': [basic_wage_count, gross_wage_count]
        }
        if basic_wage_count > 0 or gross_wage_count > 0:
            wage_df = pd.DataFrame(wage_type_data)
            fig_wage = px.bar(
                wage_df, 
                x='Wage Type', 
                y='Selections',
                title="Wage Type Preferences",
                color='Wage Type',
                color_discrete_map={'Basic': '#3498db', 'Gross': '#e74c3c'}
            )
            st.plotly_chart(fig_wage, use_container_width=True)
    
    with col_insights2:
        st.subheader("📥 Download Statistics")
        
        download_data = {
            'Download Type': ['CSV Data', 'PNG Chart'],
            'Count': [csv_downloads, png_downloads]
        }
        
        if csv_downloads > 0 or png_downloads > 0:
            download_df = pd.DataFrame(download_data)
            fig_download = px.pie(
                download_df,
                values='Count',
                names='Download Type',
                title="Download Preferences"
            )
            fig_download.update_traces(textposition='inside', textinfo='percent+value')
            st.plotly_chart(fig_download, use_container_width=True)
        else:
            st.info("No downloads recorded yet.")
        
        # Industry selection analysis
        st.subheader("🏢 Popular Industries")
        industry_data = {}
        for widget, count in counts.items():
            if "Select Industry" in widget and " - " in widget:
                parts = widget.split(" - ")
                if len(parts) > 1:
                    industry = parts[1].strip()
                    if industry:
                        industry_data[industry] = industry_data.get(industry, 0) + count
        
        if industry_data:
            top_industries = dict(sorted(industry_data.items(), key=lambda x: x[1], reverse=True)[:5])
            ind_df = pd.DataFrame(list(top_industries.items()), columns=['Industry', 'Selections'])
            
            fig_ind = px.bar(
                ind_df,
                x='Industry',
                y='Selections',
                title="Top 5 Selected Industries",
                color='Selections',
                color_continuous_scale='Viridis'
            )
            fig_ind.update_layout(showlegend=False)
            st.plotly_chart(fig_ind, use_container_width=True)
    
    st.markdown("---")
    
    # Raw data view
    with st.expander("📋 View Raw Analytics Data"):
        st.json(analytics_data)
        
        # Download analytics data
        analytics_json = json.dumps(analytics_data, indent=2)
        st.download_button(
            label="Download Analytics Data (JSON)",
            data=analytics_json,
            file_name=f"wage_app_analytics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )

def main():
    # Check for admin parameter
    query_params = st.query_params
    if query_params.get("admin") == "true":
        # Show analytics dashboard with password protection
        password = st.text_input("Enter Admin Password", type="password")
        if password == "wage_admin_2024":
            show_analytics_dashboard()
            return
        elif password:
            st.error("Invalid password!")
            return
        else:
            st.info("Please enter the admin password to view analytics.")
            return
    
    # Track analytics for the entire app with JSON storage
    with streamlit_analytics.track(save_to_json="analytics_data.json", unsafe_password="wage_admin_2024"):
        # SEO-optimized header with proper heading hierarchy
        st.markdown("""
        <div class="main-header">
            <h1>💰 Singapore Wage Insights - Comprehensive Salary Analysis</h1>
            <p class="lead">Explore wage trends across occupations and industries from 2021 to 2024. 
            Data sourced from official Singapore government statistics.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Load data
        with st.spinner("Loading wage data..."):
            df = load_data()
        
        # Sidebar filters
        st.sidebar.header("🔍 Filters")
        
        # Comparison mode toggle
        comparison_mode = st.sidebar.checkbox("Enable Comparison Mode", value=False)
        
        # Occupation selection
        st.sidebar.subheader("Select Occupation(s)")
        
        if comparison_mode:
            # Multi-select for comparison
            search_term = st.sidebar.text_input("Search occupations", "")
            filtered_occupations = filter_occupations(df, search_term)
            
            selected_occupations = st.sidebar.multiselect(
                "Choose up to 3 occupations",
                options=filtered_occupations,
                max_selections=3,
                help="Select occupations to compare"
            )
            
            if not selected_occupations:
                st.warning("Please select at least one occupation to view data.")
                return
        else:
            # Single select with search
            occupations = ["-- Select an occupation --"] + get_unique_occupations(df)
            selected_occupation = st.sidebar.selectbox(
                "Choose an occupation",
                options=occupations,
                index=0,  # Start with placeholder selected
                help="Type to search for occupations"
            )
            # Only proceed if actual occupation selected (not placeholder)
            selected_occupations = [selected_occupation] if selected_occupation and selected_occupation != "-- Select an occupation --" else []
        
        # Industry selection
        industries = get_industries()
        selected_industry = st.sidebar.selectbox(
        "Select Industry",
        options=industries,
        index=0
    )
    
        # Wage type toggle
        wage_type = st.sidebar.radio(
        "Select Wage Type",
        options=['Basic', 'Gross'],
        index=0
    )
    
        # Filter data for selected occupation(s) and industry
        data_list = []
        for occupation in selected_occupations:
            filtered_df = df[(df['Occupation'] == occupation) & (df['Industry'] == selected_industry)]
            if not filtered_df.empty:
                data_list.append((occupation, filtered_df))
    
        if not data_list:
            if not selected_occupations:
                st.info("👆 Please select an occupation from the dropdown above to view wage data.")
            else:
                st.error("No data available for the selected combination(s).")
            return
    
        # Responsive main content area
        # Use container to control responsive behavior
        chart_container = st.container()
        insights_container = st.container()
        
        # On desktop: side-by-side, on mobile: stacked
        # Create responsive columns based on screen size via CSS
        col1, col2 = st.columns([3, 1])
        
        with col1:
            # Display chart
            fig = create_wage_chart(data_list, wage_type, comparison_mode)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Key insights
            st.subheader("📊 Key Insights")
        
            # Latest year data
            latest_year = df['Year'].max()
        
            for occupation, occ_df in data_list:
                if comparison_mode and len(data_list) > 1:
                    st.markdown(f"**{occupation}**")
            
                latest_data = occ_df[occ_df['Year'] == latest_year]
            
                if not latest_data.empty:
                    wage_suffix = '_Basic' if wage_type == 'Basic' else '_Gross'
                
                    # Wage gap indicator
                    p75 = latest_data[f'P75{wage_suffix}'].iloc[0]
                    p25 = latest_data[f'P25{wage_suffix}'].iloc[0]
                    median = latest_data[f'Median{wage_suffix}'].iloc[0]
                
                    if pd.notna(p75) and pd.notna(p25):
                        wage_gap = p75 - p25
                        st.metric(
                            f"Wage Gap ({latest_year})",
                            f"${wage_gap:,.0f}",
                            help="Difference between 75th and 25th percentile"
                        )
                
                    if pd.notna(median):
                        st.metric(
                            f"Median ({latest_year})",
                            f"${median:,.0f}"
                        )
            
                if comparison_mode and len(data_list) > 1:
                    st.markdown("---")
    
        # Year-over-year growth section
        st.markdown("## 📈 Year-over-Year Salary Growth Rates")
    
        growth_tabs = st.tabs([occ for occ, _ in data_list])
    
        for idx, (occupation, occ_df) in enumerate(data_list):
            with growth_tabs[idx]:
                growth_df = calculate_yoy_growth(occ_df)
            
                if growth_df is not None and not growth_df.empty:
                    # Format the dataframe for display
                    display_df = growth_df.copy()
                    for col in ['Basic Wage Growth (%)', 'Gross Wage Growth (%)']:
                        display_df[col] = display_df[col].apply(
                            lambda x: f"{x:.1f}%" if pd.notna(x) else "N/A"
                        )
                
                    st.dataframe(display_df, use_container_width=True, hide_index=True)
                else:
                    st.info("Insufficient data for growth calculation")
    
        # Data table section
        st.markdown("## 📋 Detailed Wage Data Table")
    
        data_tabs = st.tabs([occ for occ, _ in data_list])
    
        for idx, (occupation, occ_df) in enumerate(data_list):
            with data_tabs[idx]:
                # Prepare display dataframe
                display_cols = ['Year', 'P25_Basic', 'Median_Basic', 'P75_Basic', 
                              'P25_Gross', 'Median_Gross', 'P75_Gross']
                display_df = occ_df[display_cols].copy()
            
                # Format wage columns
                wage_cols = display_cols[1:]
                for col in wage_cols:
                    display_df[col] = display_df[col].apply(
                        lambda x: f"${x:,.0f}" if pd.notna(x) else "N/A"
                    )
            
                st.dataframe(display_df, use_container_width=True, hide_index=True)
    
        # Download section
        st.markdown("## 💾 Download Salary Data")
    
        # Responsive download columns - will stack on mobile via CSS
        col1, col2 = st.columns(2)
    
        with col1:
            # CSV download
            if st.button("📥 Download Data as CSV", use_container_width=True):
                csv_data = []
                for occupation, occ_df in data_list:
                    temp_df = occ_df.copy()
                    temp_df['Occupation'] = occupation
                    csv_data.append(temp_df)
            
                combined_csv = pd.concat(csv_data)
                csv_buffer = io.StringIO()
                combined_csv.to_csv(csv_buffer, index=False)
            
                st.download_button(
                    label="Click to Download CSV",
                    data=csv_buffer.getvalue(),
                    file_name=f"wage_data_{selected_industry.replace(' ', '_')}_{wage_type}.csv",
                    mime="text/csv"
                )
    
        with col2:
            # Chart download
            if st.button("📸 Download Chart as PNG", use_container_width=True):
                # Convert plotly figure to PNG
                img_bytes = fig.to_image(format="png", width=1200, height=600, scale=2)
            
                st.download_button(
                    label="Click to Download PNG",
                    data=img_bytes,
                    file_name=f"wage_chart_{selected_industry.replace(' ', '_')}_{wage_type}.png",
                    mime="image/png"
                )
    
        # Support Section
        st.markdown("""
        <div class="support-section">
            <h2>☕ Support This Project</h2>
            <p>If you find these tools helpful, consider buying me a coffee!</p>
            <a href="https://buymeacoffee.com/adrian_goh" target="_blank" class="coffee-button">
                ☕ Buy Me a Coffee
            </a>
        </div>
        """, unsafe_allow_html=True)
    
        # SEO Footer with navigation links for AdSense compliance
        st.markdown("---")
        st.markdown("""
        <footer style="text-align: center; padding: 2rem 0; color: #666;">
            <nav style="margin-bottom: 1rem;">
                <a href="https://singaporewage.com" style="margin: 0 1rem;">Home</a>
                <a href="https://singaporewage.com/privacy" style="margin: 0 1rem;">Privacy Policy</a>
                <a href="https://singaporewage.com/terms" style="margin: 0 1rem;">Terms of Service</a>
                <a href="https://singaporewage.com/about" style="margin: 0 1rem;">About Us</a>
                <a href="https://singaporewage.com/contact" style="margin: 0 1rem;">Contact</a>
            </nav>
            <p style="margin: 0.5rem 0;">
                Data Source: Official Singapore Government Statistics (2021-2024)
            </p>
            <p style="margin: 0.5rem 0;">
                © 2024 Singapore Wage Insights. All rights reserved.
            </p>
            <p style="margin: 0.5rem 0; font-size: 0.8rem;">
                Singapore Wage Insights is an independent platform and is not affiliated with any government agency.
            </p>
            <p style="margin: 0.5rem 0; font-size: 0.7rem;">
                <a href="?admin=true" style="color: #999; text-decoration: none;">📊</a>
            </p>
        </footer>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()