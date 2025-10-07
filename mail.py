from email.message import EmailMessage
import smtplib

def send_notification_email(new_courses, SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL):
    subject = "New University Courses Available!"
    
    body = "The following new course(s) have opened up:\n\n"
    body += "\n".join([f"- Class Code: {code}" for code in new_courses])
    body += "\n\nPlease check the portal."

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() 
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("✅ Successfully sent email notification.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")