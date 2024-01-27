from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64
from service import service  # Assuming this is your service import
import os


def create_message(to, subject, message_text):
    """
    Create a MIME message ready to be sent.
    """
    message = MIMEText(message_text, "html")
    message["to"] = to
    message["subject"] = subject
    return {"raw": base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def send_message(user_id, message_body):
    """
    Send the composed message.
    """
    try:
        message = (
            service.users().messages().send(userId=user_id, body=message_body).execute()
        )
        return message
    except Exception as e:
        print(f"An error occurred while sending the message: {str(e)}")
        return None


def load_template(template_filename):
    """
    Load the HTML template from the file.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(current_dir, template_filename)
    with open(template_path, "r") as file:
        template = file.read()
    return template


def main():
    # Get user inputs
    recipient_email = input("Enter recipient's email address: ")
    subject = input("Enter the email subject: ")
    user_name = input("Enter the user's name: ")

    # Load HTML template
    template_path = "template.html"
    template = load_template(template_path)

    # Replace placeholders in the template
    message_text = template.replace("{{ subject }}", subject)
    message_text = message_text.replace("{{ user }}", user_name)
    message_text = message_text.replace(
        "{{ content }}", "This is the content of the email."
    )

    # Create MIME message
    message_body = create_message(recipient_email, subject, message_text)

    # Send the message
    message = send_message("me", message_body)

    if message:
        print("Message sent successfully!")
    else:
        print("Failed to send the message.")


if __name__ == "__main__":
    main()
