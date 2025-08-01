import streamlit as st

st.set_page_config(
    page_title="Privacy Policy - Singapore Wage Insights",
    page_icon="🔒",
    layout="wide"
)

st.markdown("""
# Privacy Policy

**Last Updated: August 1, 2024**

## Introduction

Singapore Wage Insights ("we," "our," or "us") is committed to protecting your privacy. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit our website singaporewage.com.

## Information We Collect

### 1. Automatically Collected Information

When you visit our website, we automatically collect certain information about your device, including:
- IP address
- Browser type and version
- Operating system
- Referring website
- Pages viewed
- Time spent on pages
- Date and time of visit

### 2. Analytics Data

We use Google Analytics to understand how visitors interact with our website. This includes:
- Page views and user behavior
- Geographic location (country/city level)
- Device and browser information
- Traffic sources

### 3. Cookies

We use cookies and similar tracking technologies to:
- Analyze website traffic
- Remember user preferences
- Improve website performance
- Serve relevant advertisements through Google AdSense

## How We Use Your Information

We use the collected information to:
- Provide and maintain our wage analysis service
- Improve user experience
- Analyze website usage patterns
- Display relevant advertisements
- Comply with legal obligations

## Google AdSense

Our website uses Google AdSense to display advertisements. Google uses cookies to serve ads based on your prior visits to our website or other websites. You can opt out of personalized advertising by visiting [Google's Ads Settings](https://www.google.com/settings/ads).

## Data Security

We implement appropriate technical and organizational measures to protect your information against unauthorized access, alteration, disclosure, or destruction.

## Third-Party Services

We use the following third-party services:
- **Google Analytics**: For website analytics
- **Google AdSense**: For advertising
- **Render**: For website hosting

These services have their own privacy policies governing the use of your information.

## Your Rights

You have the right to:
- Access your personal information
- Request correction of inaccurate data
- Request deletion of your data
- Opt out of certain data collection practices

## Children's Privacy

Our service is not directed to individuals under the age of 13. We do not knowingly collect personal information from children under 13.

## Changes to This Privacy Policy

We may update this Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page and updating the "Last Updated" date.

## Contact Us

If you have questions about this Privacy Policy, please contact us at:
- Email: privacy@singaporewage.com
- Website: https://singaporewage.com/contact

## Consent

By using our website, you consent to our Privacy Policy and agree to its terms.
""")

# Add footer
st.markdown("---")
st.markdown("""
<footer style="text-align: center; padding: 1rem 0; color: #666;">
    <p><a href="https://singaporewage.com">← Back to Home</a></p>
    <p>© 2024 Singapore Wage Insights. All rights reserved.</p>
</footer>
""", unsafe_allow_html=True)