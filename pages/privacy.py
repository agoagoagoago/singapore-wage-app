import streamlit as st

st.set_page_config(
    page_title="Privacy Policy - Singapore Wage Insights",
    page_icon="🔒",
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
    
    .highlight-box {
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
st.markdown("# 🔒 Privacy Policy")
st.markdown("**Last Updated:** August 3, 2024")

# Contact information
st.markdown("""
<div class="contact-box">
    <strong>📧 Contact:</strong> For questions about this privacy policy or to exercise your privacy rights, email us at 
    <a href="mailto:admin@singaporewage.com" style="color: #0066cc;">admin@singaporewage.com</a>
</div>
""", unsafe_allow_html=True)

# Introduction
st.markdown("""
## Introduction

Singapore Wage Insights ("we," "our," or "us") is committed to protecting your privacy and being transparent about how we collect, use, and protect your information. This Privacy Policy explains our practices when you visit our website at singaporewage.com and use our wage analysis tools.

**Key Principles:**
- We collect minimal data necessary to provide our service
- We do not sell or share your personal information
- You have control over your data and privacy settings
- We are transparent about our data practices
""")

# Information We Collect
st.markdown("""
## 1. Information We Collect

### 1.1 Automatically Collected Information
When you visit our website, we automatically collect:

- **Basic Analytics Data:** Page views, session duration, bounce rate
- **Technical Information:** Browser type, operating system, device type, screen resolution
- **Usage Patterns:** Features used, search queries within our platform, download activities
- **Network Information:** IP address (anonymized), referring website, general geographic location (country/city level)

### 1.2 User-Provided Information
- **Search Queries:** Occupations and industries you search for within our platform
- **Optional Feedback:** Any messages or feedback you choose to send us

### 1.3 Cookies and Tracking Technologies
We use the following types of cookies:

- **Essential Cookies:** Required for basic website functionality
- **Analytics Cookies:** Help us understand how you use our site (can be disabled)
- **Preference Cookies:** Remember your settings and preferences

You can control cookie settings through your browser preferences.
""")

# How We Use Information
st.markdown("""
## 2. How We Use Your Information

We use collected information for the following purposes:

### 2.1 Service Provision
- Provide wage analysis and visualization tools
- Display relevant data based on your searches
- Enable data export functionality (CSV, PNG)

### 2.2 Service Improvement
- Analyze usage patterns to improve user experience
- Identify popular occupations and industries for feature development
- Optimize website performance and loading times
- Debug technical issues and improve reliability

### 2.3 Analytics and Insights
- Generate aggregated, anonymized usage statistics
- Understand demographic trends in wage research
- Improve data presentation and visualization

**We do not use your information for:**
- Targeted advertising or marketing
- Selling or sharing with third parties
- Creating individual user profiles for commercial purposes
""")

# Data Sharing and Third Parties
st.markdown("""
## 3. Data Sharing and Third-Party Services

### 3.1 No Sale of Personal Information
We do not sell, rent, or trade your personal information to third parties.

### 3.2 Legal Requirements
We may disclose information if required by law or to:
- Comply with legal obligations
- Protect our rights and property
- Ensure user safety and security
- Respond to government requests or court orders
""")

# Data Security
st.markdown("""
## 4. Data Security

### 4.1 Security Measures
We implement appropriate technical and organizational security measures:

- **Data Encryption:** HTTPS encryption for all data transmission
- **Access Controls:** Limited access to systems and data
- **Regular Updates:** Security patches and updates applied promptly
- **Monitoring:** Continuous monitoring for security threats

### 4.2 Data Retention
- **Analytics Data:** Retained for up to 2 years for service improvement
- **Search History:** Limited to recent searches for user convenience
- **Technical Logs:** Automatically deleted after 90 days

### 4.3 Data Breaches
In the unlikely event of a data breach, we will:
- Notify affected users within 72 hours
- Provide details about the incident and our response
- Take immediate steps to secure the system
- Cooperate with relevant authorities
""")

# Your Privacy Rights
st.markdown("""
## 5. Your Privacy Rights

You have the following rights regarding your personal information:

### 5.1 Access and Transparency
- **Right to Know:** What personal information we collect and how we use it
- **Data Access:** Request a copy of your personal information
- **Processing Details:** Information about how and why we process your data

### 5.2 Control and Choice
- **Opt-Out:** Disable analytics tracking through browser settings
- **Data Deletion:** Request deletion of your personal information
- **Correction:** Request correction of inaccurate information
- **Data Portability:** Receive your data in a portable format

### 5.3 How to Exercise Your Rights
To exercise any of these rights, contact us at admin@singaporewage.com with:
- Clear description of your request
- Verification of your identity (if applicable)
- Specific information you're requesting

We will respond within 30 days of receiving your request.
""")

# International Data Transfers
st.markdown("""
## 6. International Data Transfers

Our services are primarily hosted in Singapore and the United States. If you access our website from other countries:

- Your data may be transferred to and processed in these countries
- We ensure appropriate safeguards are in place for international transfers
- Data protection standards equivalent to Singapore's PDPA are maintained
""")

# Children's Privacy
st.markdown("""
## 7. Children's Privacy

Our service is not directed to individuals under 16 years of age. We do not knowingly collect personal information from children under 16. If we become aware that we have collected such information, we will take steps to delete it promptly.

Parents or guardians who believe their child has provided personal information should contact us immediately.
""")

# Changes to Privacy Policy
st.markdown("""
## 8. Changes to This Privacy Policy

We may update this Privacy Policy from time to time to reflect:
- Changes in our practices or services
- Legal or regulatory requirements
- User feedback and suggestions

When we make changes:
- We will update the "Last Updated" date at the top of this policy
- For significant changes, we will provide prominent notice on our website
- Continued use of our service constitutes acceptance of the updated policy
""")

# Contact Information
st.markdown("""
## 9. Contact Information

### Privacy Questions and Requests
For questions about this Privacy Policy or to exercise your privacy rights:

**Email:** admin@singaporewage.com  
**Response Time:** Within 30 days  
**Website:** https://singaporewage.com

### Data Protection Officer
For complex privacy matters or complaints, you may also contact relevant authorities:
- **Singapore:** Personal Data Protection Commission (PDPC)
- **International:** Your local data protection authority
""")

# Consent and Acknowledgment
st.markdown("""
<div class="highlight-box">
    <h3>🤝 Your Consent</h3>
    <p>By using Singapore Wage Insights, you acknowledge that you have read and understood this Privacy Policy and agree to the collection, use, and disclosure of your information as described herein.</p>
    <p>You can withdraw your consent at any time by ceasing to use our service or contacting us at admin@singaporewage.com.</p>
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
    <p>This policy is effective as of August 3, 2024</p>
</footer>
""", unsafe_allow_html=True)