import streamlit as st
import re
    
    # Suspicious keywords often found in phishing emails
phishing_keywords = [
    "urgent", "verify", "click here", "login", "password",
    "bank", "account", "security alert", "update", "reset",
    "confirm", "limited time", "suspended", "billing"
    ]
    
    # Common fake or throwaway domains
fake_domains = [
    "mailinator.com", "tempmail.com", "10minutemail.com", "fakeinbox.com",
    "sharklasers.com", "guerrillamail.com", "dispostable.com"
    ]
    
    # Function to check if the email is suspicious
def check_email_validity(email):
    pattern = r"[^@]+@[^@]+\.[^@]+"  # Basic email regex
    if not re.match(pattern, email):
        return False, "❌ Invalid email format"
    
    domain = email.split('@')[-1].lower()
    if domain in fake_domains:
        return False, f"⚠ Domain `{domain}` is known for temporary/fake emails"
    
    return True, "✅ Email format and domain look okay"
    
    # Function to detect phishing content
def detect_phishing(subject, body):
             full_text = (subject + " " + body).lower()
    detected = [word for word in phishing_keywords if word in full_text]
    return len(detected) >= 2, detected
    
    # Streamlit UI
    st.set_page_config(page_title="Phishing Email Detector")
    st.title("📧 Phishing Email Detection System")
    
    st.markdown("Enter email details below to check for phishing.")
    
    email = st.text_input("Sender Email Address")
    subject = st.text_input("Email Subject")
    body = st.text_area("Email Body")
    
    if st.button("Scan Email"):
    is_valid_email, email_msg = check_email_validity(email)
    is_phish, matched_keywords = detect_phishing(subject, body)
    
    st.subheader("🔍 Scan Results")
    # Email check
    st.markdown("**Email Address Check:**")
    if is_valid_email:
        st.info(email_msg)
    else:
        st.warning(email_msg)
    
    
    # Phishing content check
    st.markdown("**Content Analysis:**")
    if is_phish:
        st.error(f"⚠ This email may be phishing! ({len(matched_keywords)} suspicious keywords found)")
        st.write(f"Suspicious keywords: `{', '.join(matched_keywords)}`")
    else:
        st.success("✅ Email content appears safe.")
    
    st.sidebar.title("👨💻 Amit Lunaich")
    
    
