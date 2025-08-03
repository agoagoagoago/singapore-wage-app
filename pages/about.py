import streamlit as st

st.set_page_config(
    page_title="About Us - Singapore Wage Insights",
    page_icon="ℹ️",
    layout="wide"
)

# Custom CSS for consistent styling
st.markdown("""
<style>
    .main > div {
        max-width: 800px;
        margin: 0 auto;
        padding-top: 2rem;
    }
    
    .contact-box {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1.5rem 0;
        border-left: 4px solid #0066cc;
    }
    
    .mission-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 12px;
        margin: 2rem 0;
        text-align: center;
    }
    
    .feature-box {
        background: #e8f4fd;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        border: 1px solid #bee5eb;
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        margin: 2rem 0;
    }
    
    .stat-item {
        text-align: center;
        padding: 1rem;
        background: white;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem;
        flex: 1;
        min-width: 150px;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: #0066cc;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #666;
        margin-top: 0.5rem;
    }
    
    h1 {
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    
    h2 {
        color: #34495e;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    
    .back-link {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
    }
    
    @media (max-width: 768px) {
        .main > div {
            padding: 1rem;
        }
        
        .mission-box {
            padding: 1.5rem;
        }
        
        .stats-container {
            flex-direction: column;
        }
        
        .stat-item {
            margin: 0.5rem 0;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("# ℹ️ About Singapore Wage Insights")

# Mission Statement
st.markdown("""
<div class="mission-box">
    <h2 style="color: white; margin-top: 0;">🎯 Our Mission</h2>
    <p style="font-size: 1.2rem; line-height: 1.6; margin-bottom: 0;">
        To democratize access to wage information in Singapore, empowering individuals with transparent, accurate, and comprehensive salary data for informed career decisions.
    </p>
</div>
""", unsafe_allow_html=True)

# Platform Overview
st.markdown("""
## 🏢 About Our Platform

Singapore Wage Insights is an independent, data-driven platform dedicated to providing comprehensive wage analysis and salary transparency across Singapore's diverse employment landscape. We believe that access to accurate wage information is fundamental to career planning, salary negotiations, and economic empowerment.

### 🌟 What Makes Us Different

- **Government-Sourced Data:** All wage information comes directly from official Singapore government statistics
- **Comprehensive Coverage:** Data spans 2021-2024 across all major industries and occupations
- **User-Friendly Interface:** Complex wage data made accessible through intuitive visualizations
- **Complete Transparency:** Open about our data sources, methodology, and limitations
- **No Hidden Agendas:** Independent platform not affiliated with any employer or recruitment agency
""")

# Platform Statistics
st.markdown("""
<div class="stats-container">
    <div class="stat-item">
        <div class="stat-number">4</div>
        <div class="stat-label">Years of Data<br>(2021-2024)</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">14</div>
        <div class="stat-label">Industry<br>Categories</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">500+</div>
        <div class="stat-label">Occupation<br>Types</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">100%</div>
        <div class="stat-label">Free<br>Access</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Our Purpose
st.markdown("""
## 🎯 Our Purpose

### Empowering Job Seekers
We provide the wage insights you need to:
- Research salary ranges for career transitions
- Prepare for salary negotiations with confidence
- Understand compensation trends in your industry
- Make informed decisions about career advancement

### Supporting Employers
Our data helps organizations:
- Benchmark compensation packages
- Understand market salary standards
- Develop competitive hiring strategies
- Ensure fair and equitable pay practices

### Advancing Economic Transparency
We contribute to Singapore's economic ecosystem by:
- Promoting wage transparency and fairness
- Supporting evidence-based career planning
- Facilitating informed employment decisions
- Encouraging salary equity across industries
""")

# Data Source and Methodology
st.markdown("""
## 📊 Data Sources and Methodology

### Primary Data Sources
Our wage data comes exclusively from:
- **Ministry of Manpower (MOM):** Official employment statistics and wage surveys
- **Department of Statistics Singapore (SingStat):** National employment data
- **Government Employment Reports:** Annual and quarterly wage publications

### Data Processing Approach
""")

# Feature box for methodology
st.markdown("""
<div class="feature-box">
    <h4>🔍 Our Methodology</h4>
    <ul>
        <li><strong>Data Verification:</strong> All data cross-referenced with official government sources</li>
        <li><strong>Quality Control:</strong> Systematic validation and cleaning of wage information</li>
        <li><strong>Standardization:</strong> Consistent formatting across years and industries</li>
        <li><strong>Transparency:</strong> Clear indication of data limitations and suppressed values</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
### What We Provide
- **Percentile Data:** 25th, 50th (median), and 75th percentile wages
- **Basic vs. Gross Wages:** Distinction between basic salary and total compensation
- **Industry Breakdown:** Wages segmented by major industry categories
- **Temporal Analysis:** Year-over-year trends and growth rates
""")

# Platform Features
st.markdown("""
## 🛠️ Platform Features

### Interactive Analysis Tools
- **Occupation Search:** Find specific roles with intelligent search functionality
- **Industry Filtering:** Focus on specific sectors or compare across industries
- **Trend Visualization:** Interactive charts showing wage progression over time
- **Growth Calculations:** Year-over-year percentage changes in compensation

### Data Export Capabilities
- **CSV Downloads:** Raw data for further analysis in spreadsheet applications
- **Chart Exports:** High-quality visualizations for presentations and reports
- **Custom Filtering:** Export only the data relevant to your research needs

### Mobile-Responsive Design
- **Optimized Experience:** Full functionality across desktop, tablet, and mobile devices
- **Fast Loading:** Optimized performance for quick access to wage information
- **Intuitive Navigation:** User-friendly interface designed for efficiency
""")

# Team and Contact
st.markdown("""
## 👥 Our Team and Values

### Our Commitment
Singapore Wage Insights is built and maintained by professionals who believe in:
- **Data Accuracy:** Rigorous verification of all information
- **User Privacy:** Minimal data collection with full transparency
- **Continuous Improvement:** Regular updates and feature enhancements
- **Community Service:** Providing valuable resources at no cost to users

### Platform Independence
We want to be clear about our independence:
- **No Corporate Sponsorship:** Not funded by employers, recruitment agencies, or government entities
- **No Bias:** Objective presentation of wage data without manipulation
- **No Commercial Interests:** Our goal is public service, not profit
- **No Data Manipulation:** Raw government data presented accurately and transparently
""")

# Contact Information
st.markdown("""
<div class="contact-box">
    <h3>📧 Get in Touch</h3>
    <p><strong>General Inquiries:</strong> <a href="mailto:admin@singaporewage.com" style="color: #0066cc;">admin@singaporewage.com</a></p>
    <p><strong>Data Questions:</strong> Questions about specific wage data or methodology</p>
    <p><strong>Technical Support:</strong> Website issues, bugs, or feature requests</p>
    <p><strong>Partnerships:</strong> Collaboration opportunities or data sharing inquiries</p>
    <p><strong>Response Time:</strong> We aim to respond within 2-3 business days</p>
</div>
""", unsafe_allow_html=True)

# Future Plans
st.markdown("""
## 🚀 Future Development

### Planned Enhancements
We're continuously working to improve Singapore Wage Insights:

- **Extended Data Coverage:** Adding more years as government data becomes available
- **Enhanced Analytics:** More sophisticated trend analysis and forecasting tools
- **Industry Deep-Dives:** Detailed analysis of specific sectors and specializations
- **Mobile App:** Native mobile application for on-the-go wage research
- **API Access:** Programmatic access to wage data for researchers and developers

### Community Feedback
Your input shapes our development priorities:
- **Feature Requests:** Tell us what tools would be most valuable
- **User Experience:** Help us improve the platform's usability
- **Data Requests:** Suggest additional data sources or analysis approaches
- **Bug Reports:** Help us maintain a reliable, error-free platform
""")

# Legal and Disclaimer
st.markdown("""
## ⚖️ Important Disclaimers

### Data Limitations
Please understand that:
- **Statistical Nature:** Wage data represents averages and ranges, not guarantees
- **Individual Variation:** Personal circumstances significantly impact actual salaries
- **Market Dynamics:** Economic conditions and industry changes affect compensation
- **Verification Recommended:** Always verify critical information with multiple sources

### Platform Scope
Singapore Wage Insights:
- **Provides Information Only:** We do not offer career advice or employment services
- **Independent Platform:** Not affiliated with government agencies or employers
- **Educational Purpose:** Designed for research and informational use
- **No Guarantees:** Cannot guarantee accuracy of outcomes based on our data

### Professional Advice
For important career and financial decisions, we recommend:
- Consulting with career counselors or financial advisors
- Speaking directly with industry professionals
- Researching multiple information sources
- Considering your unique circumstances and goals
""")

# Support Section
st.markdown("""
## ☕ Support Our Mission

If you find Singapore Wage Insights valuable, consider supporting our work:
""")

# Buy Me a Coffee button
st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
    <a href="https://buymeacoffee.com/adrian_goh" target="_blank" style="display: inline-block; background: linear-gradient(45deg, #f39c12, #e67e22); color: white; padding: 15px 30px; border-radius: 50px; text-decoration: none; font-weight: bold;">
        ☕ Buy Me a Coffee
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
Your support helps us:
- Maintain and improve the platform
- Add new features and data sources
- Keep the service free for all users
- Invest in better infrastructure and tools
""")

# Back navigation
st.markdown("""
<div class="back-link">
    <strong><a href="/" style="color: #0066cc; text-decoration: none;">← Back to Singapore Wage Insights</a></strong>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<footer style="text-align: center; padding: 1rem 0; color: #666; font-size: 0.9rem;">
    <p>© 2024 Singapore Wage Insights. All rights reserved.</p>
    <p><strong>Contact:</strong> <a href="mailto:admin@singaporewage.com" style="color: #0066cc;">admin@singaporewage.com</a></p>
    <p>Singapore Wage Insights is an independent platform and is not affiliated with any government agency.</p>
</footer>
""", unsafe_allow_html=True)