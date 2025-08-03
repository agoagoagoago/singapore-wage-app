import streamlit as st

st.set_page_config(
    page_title="Terms of Service - Singapore Wage Insights",
    page_icon="📋",
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
    
    .warning-box {
        background: #fff3cd;
        padding: 1rem;
        border-radius: 6px;
        margin: 1rem 0;
        border: 1px solid #ffeaa7;
    }
    
    .info-box {
        background: #e8f4fd;
        padding: 1rem;
        border-radius: 6px;
        margin: 1rem 0;
        border: 1px solid #bee5eb;
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
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 📋 Terms of Service")
st.markdown("**Last Updated:** August 3, 2024")

# Contact information
st.markdown("""
<div class="contact-box">
    <strong>📧 Contact:</strong> For questions about these terms or legal matters, email us at 
    <a href="mailto:admin@singaporewage.com" style="color: #0066cc;">admin@singaporewage.com</a>
</div>
""", unsafe_allow_html=True)

# Introduction and Acceptance
st.markdown("""
## 1. Acceptance of Terms

### 1.1 Agreement to Terms
By accessing or using Singapore Wage Insights ("the Service"), you agree to be bound by these Terms of Service ("Terms"). If you do not agree to these Terms, please do not use the Service.

### 1.2 Legal Capacity
You must be at least 16 years old and have the legal capacity to enter into this agreement. If you are using the Service on behalf of an organization, you represent that you have the authority to bind that organization to these Terms.

### 1.3 Modifications
We reserve the right to modify these Terms at any time. Changes will be effective immediately upon posting. Your continued use of the Service constitutes acceptance of any modifications.
""")

# Service Description
st.markdown("""
## 2. Service Description

### 2.1 Platform Purpose
Singapore Wage Insights provides:
- Analysis and visualization of Singapore wage data (2021-2024)
- Interactive tools for exploring salary trends across occupations and industries
- Data export capabilities for research and analysis
- Educational resources about Singapore's employment landscape

### 2.2 Data Sources
Our platform uses publicly available wage data from:
- Singapore government statistical agencies
- Official employment surveys and reports
- Publicly released occupational wage studies

### 2.3 Service Limitations
Please note that:
- Data is for informational purposes only
- Individual experiences may vary significantly
- Platform availability may be subject to maintenance or technical issues
- Features may be updated or modified without prior notice
""")

# Data Accuracy and Disclaimers
st.markdown("""
## 3. Data Accuracy and Disclaimers

### 3.1 Information Accuracy
""")

# Warning box for data accuracy
st.markdown("""
<div class="warning-box">
    <strong>⚠️ Important Disclaimer:</strong> While we strive for accuracy, all wage data is provided "as is" based on available government statistics. We make no guarantees about the completeness, accuracy, or timeliness of the information.
</div>
""", unsafe_allow_html=True)

st.markdown("""
### 3.2 No Financial or Career Advice
The Service does not provide:
- Personal financial advice
- Career counseling or guidance
- Employment recommendations
- Salary negotiation advice

### 3.3 Individual Results May Vary
Wage data represents statistical averages and ranges. Individual salaries may differ significantly based on:
- Education and qualifications
- Years of experience
- Company size and industry sector
- Performance and negotiation skills
- Market conditions and economic factors

### 3.4 Data Verification Responsibility
For critical decisions, we strongly recommend:
- Verifying information with multiple sources
- Consulting with professional advisors
- Conducting your own market research
- Seeking advice from industry professionals
""")

# Permitted Uses
st.markdown("""
## 4. Permitted Uses

### 4.1 Authorized Activities
You may use our platform for:

- **Personal Research:** Salary research for career planning and job searching
- **Academic Purposes:** Educational research and analysis projects
- **Professional Analysis:** Business research and market analysis
- **Data Export:** Downloading data for permitted personal or professional use
- **Sharing Insights:** Sharing general trends and insights (with attribution)

### 4.2 Commercial Use Guidelines
Limited commercial use is permitted for:
- Internal business research and analysis
- Academic publications with proper attribution
- Professional consulting (with data verification)

Commercial redistribution of our compiled datasets requires prior written permission.
""")

# Prohibited Activities
st.markdown("""
## 5. Prohibited Activities

### 5.1 Technical Restrictions
You may not:

- **Excessive Scraping:** Use automated tools to scrape data beyond reasonable use
- **System Overload:** Make requests that could overwhelm our servers
- **Reverse Engineering:** Attempt to reverse engineer our algorithms or systems
- **Circumvention:** Bypass any security measures or access controls
- **Malicious Activity:** Upload viruses, malware, or engage in harmful activities

### 5.2 Content and Usage Restrictions
You may not:

- **Misrepresentation:** Present our data as your own original research
- **Redistribution:** Commercially redistribute our compiled datasets without permission
- **Misleading Use:** Use data in ways that could mislead or deceive others
- **Illegal Purposes:** Use the Service for any illegal or unauthorized purposes
- **Harassment:** Use the platform to harass, threaten, or harm others

### 5.3 Consequences of Violations
Violations may result in:
- Immediate termination of access
- Legal action if necessary
- Reporting to relevant authorities
- Claims for damages and costs
""")

# Intellectual Property
st.markdown("""
## 6. Intellectual Property Rights

### 6.1 Our Intellectual Property
Singapore Wage Insights owns:
- Platform design, code, and algorithms
- Data compilation and analysis methodologies
- User interface and visualization tools
- Brand names, logos, and trademarks

### 6.2 Government Data
Raw wage data belongs to the Singapore government and is publicly available. Our intellectual property lies in:
- Data compilation and processing methods
- Visualization and analysis tools
- Platform functionality and features

### 6.3 User-Generated Content
If you provide feedback or suggestions:
- You grant us a non-exclusive license to use your feedback
- We may implement suggestions without compensation
- You retain ownership of any original content you create
""")

# Service Availability
st.markdown("""
## 7. Service Availability and Modifications

### 7.1 Service Availability
We strive to maintain high availability but do not guarantee:
- Uninterrupted access to the Service
- Error-free operation at all times
- Availability during maintenance periods
- Compatibility with all devices or browsers

### 7.2 Maintenance and Updates
We may perform:
- Scheduled maintenance with advance notice when possible
- Emergency updates or fixes without notice
- Feature updates and improvements
- Data refreshes and accuracy improvements

### 7.3 Service Modifications
We reserve the right to:
- Modify, suspend, or discontinue features
- Update terms and policies
- Change pricing (if applicable)
- Enhance or reduce functionality
""")

# Limitation of Liability
st.markdown("""
## 8. Limitation of Liability

### 8.1 Disclaimer of Warranties
""")

# Warning box for warranty disclaimer
st.markdown("""
<div class="warning-box">
    <strong>⚠️ Important:</strong> THE SERVICE IS PROVIDED "AS IS" WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR NON-INFRINGEMENT.
</div>
""", unsafe_allow_html=True)

st.markdown("""
### 8.2 Limitation of Damages
To the fullest extent permitted by law, Singapore Wage Insights shall not be liable for:

- **Indirect Damages:** Lost profits, business interruption, or consequential damages
- **Career Decisions:** Outcomes of employment or salary decisions based on our data
- **Data Inaccuracies:** Losses resulting from inaccurate or outdated information
- **Service Interruptions:** Damages from temporary unavailability of the Service
- **Third-Party Actions:** Actions of other users or third-party service providers

### 8.3 Maximum Liability
Our total liability for any claims shall not exceed the amount you paid to use the Service (currently $0 for free services).

### 8.4 Essential Purpose
These limitations are fundamental to our ability to provide the Service at no cost to users.
""")

# User Responsibilities
st.markdown("""
## 9. User Responsibilities

### 9.1 Appropriate Use
You are responsible for:
- Using the Service appropriately and legally
- Verifying information for important decisions
- Maintaining the security of your access
- Respecting other users and our platform

### 9.2 Data Verification
You acknowledge that:
- You will verify important information independently
- You understand the limitations of statistical data
- You will not rely solely on our data for major decisions
- You will seek professional advice when appropriate

### 9.3 Compliance
You agree to comply with:
- All applicable laws and regulations
- These Terms of Service
- Our Privacy Policy
- Any additional guidelines we may provide
""")

# Dispute Resolution
st.markdown("""
## 10. Dispute Resolution and Legal Terms

### 10.1 Governing Law
These Terms are governed by the laws of Singapore. Any disputes will be subject to the jurisdiction of Singapore courts.

### 10.2 Dispute Resolution Process
For disputes:
1. **Direct Communication:** Contact us first at admin@singaporewage.com
2. **Good Faith Resolution:** We'll attempt to resolve issues amicably
3. **Mediation:** Consider mediation before formal legal proceedings
4. **Legal Action:** As a last resort, disputes may be resolved in Singapore courts

### 10.3 Severability
If any provision of these Terms is found unenforceable, the remaining provisions will continue in full force and effect.

### 10.4 Entire Agreement
These Terms, along with our Privacy Policy, constitute the entire agreement between you and Singapore Wage Insights.
""")

# Contact and Support
st.markdown("""
## 11. Contact Information and Support

### 11.1 General Inquiries
**Email:** admin@singaporewage.com  
**Response Time:** Within 5 business days  
**Website:** https://singaporewage.com

### 11.2 Legal Matters
For legal notices or formal disputes:
- Send written notice to admin@singaporewage.com
- Include detailed description of the issue
- Provide your contact information for response

### 11.3 Technical Support
For technical issues:
- Check our website for known issues
- Contact admin@singaporewage.com with details
- Include browser and device information when relevant
""")

# Final Notes
st.markdown("""
<div class="info-box">
    <h3>📝 Important Reminders</h3>
    <ul>
        <li><strong>Free Service:</strong> Singapore Wage Insights is currently provided free of charge</li>
        <li><strong>Educational Purpose:</strong> Our platform is designed for informational and educational use</li>
        <li><strong>Data Verification:</strong> Always verify important information with multiple sources</li>
        <li><strong>Professional Advice:</strong> Consult professionals for significant career or financial decisions</li>
    </ul>
</div>
""", unsafe_allow_html=True)

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
    <p>These terms are effective as of August 3, 2024</p>
    <p>By using our service, you acknowledge that you have read, understood, and agree to these Terms of Service.</p>
</footer>
""", unsafe_allow_html=True)