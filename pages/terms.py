import streamlit as st

st.set_page_config(
    page_title="Terms of Service - Singapore Wage Insights",
    page_icon="📜",
    layout="wide"
)

st.markdown("""
# Terms of Service

**Last Updated: August 1, 2024**

## 1. Acceptance of Terms

By accessing and using Singapore Wage Insights ("the Service") at singaporewage.com, you accept and agree to be bound by these Terms of Service.

## 2. Description of Service

Singapore Wage Insights provides wage and salary analysis data for Singapore based on official government statistics from 2021-2024. The Service includes:
- Interactive wage trend charts
- Occupation and industry comparisons
- Data visualization tools
- Downloadable reports

## 3. Use of Service

### Permitted Use
- Personal, non-commercial research
- Educational purposes
- Professional salary research
- Market analysis

### Prohibited Use
- Scraping or automated data extraction
- Redistribution of data without attribution
- Misrepresentation of data
- Any illegal or unauthorized purpose

## 4. Data Disclaimer

While we strive for accuracy:
- Data is sourced from official government statistics
- We make no warranties about completeness or accuracy
- Data should not be the sole basis for employment decisions
- Historical data may not predict future trends

## 5. Intellectual Property

- The Service and its original content are protected by copyright
- Data source: Singapore Government (publicly available)
- Charts and visualizations created by the Service are our property
- You may share content with proper attribution

## 6. User Conduct

You agree not to:
- Violate any laws or regulations
- Interfere with the Service's operation
- Attempt unauthorized access
- Submit false or misleading information
- Use the Service to harm others

## 7. Advertising

The Service displays advertisements through Google AdSense. By using the Service, you consent to the display of these advertisements and the use of cookies for advertising purposes.

## 8. Privacy

Your use of the Service is subject to our Privacy Policy, which is incorporated into these Terms of Service.

## 9. Disclaimers

THE SERVICE IS PROVIDED "AS IS" WITHOUT WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT.

## 10. Limitation of Liability

Singapore Wage Insights shall not be liable for any indirect, incidental, special, consequential, or punitive damages resulting from your use or inability to use the Service.

## 11. Indemnification

You agree to indemnify and hold harmless Singapore Wage Insights from any claims, damages, or expenses arising from your use of the Service or violation of these Terms.

## 12. Modifications

We reserve the right to modify these Terms at any time. Continued use of the Service after changes constitutes acceptance of the modified Terms.

## 13. Termination

We may terminate or suspend access to the Service immediately, without prior notice, for any breach of these Terms.

## 14. Governing Law

These Terms are governed by the laws of Singapore, without regard to conflict of law principles.

## 15. Contact Information

For questions about these Terms of Service:
- Email: legal@singaporewage.com
- Website: https://singaporewage.com/contact

## 16. Severability

If any provision of these Terms is found to be unenforceable, the remaining provisions will continue in full force and effect.

## 17. Entire Agreement

These Terms constitute the entire agreement between you and Singapore Wage Insights regarding the use of the Service.
""")

# Add footer
st.markdown("---")
st.markdown("""
<footer style="text-align: center; padding: 1rem 0; color: #666;">
    <p><a href="https://singaporewage.com">← Back to Home</a></p>
    <p>© 2024 Singapore Wage Insights. All rights reserved.</p>
</footer>
""", unsafe_allow_html=True)