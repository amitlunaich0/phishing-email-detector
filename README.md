🛡️ Phishing Email Detection System
A simple web app built using Python and Streamlit that helps detect whether an email is real or a phishing attempt based on the subject, content, and sender’s email address.

📌 Features
✅ Checks if the email address is from a legit or temporary domain

⚠️ Detects phishing keywords (like "click here", "verify", "urgent")

📊 Displays detection results instantly

🌐 Deployed publicly using Streamlit Cloud

📄 Supports manual input for email fields

🎯 What is Phishing?
Phishing is a cyber-attack where attackers trick users into sharing sensitive information (like passwords, OTPs, or card details) by sending fake emails that look real.

Example phishing message:

“Your account has been suspended. Click here to verify your login.”

🚀 How It Works
User enters:

📨 Email address (e.g., support@tempmail.com)

📝 Subject line

✉️ Body/content of the email

App checks for:

Suspicious keywords

Temporary/fake email domains

It returns:

✅ If safe

⚠️ Warning if phishing signs are detected

💡 Tech Stack
Tool	Purpose
Python	Backend logic
Streamlit	Interactive web UI
fpdf / pptx	Export reports and slides
GitHub	Version control & collaboration
Streamlit Cloud	For public deployment
🖼️ Screenshot
(Add your screenshot here)
📸 A preview of the phishing detection interface.

📌 Future Scope
Add Machine Learning model for better accuracy

Integrate real email file support (.eml format)

Use email reputation APIs

Add user login + log history

🙏 Credits
Built by Amit Lunaich

Inspired by common phishing detection needs in cybersecurity awareness

📬 License
This project is open-source under the MIT License.

