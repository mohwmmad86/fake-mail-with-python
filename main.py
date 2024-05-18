import requests
import time
# mohwmmad86
def get_temp_email():
    response = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
    if response.status_code == 200:
        email_address = response.json()[0]
        print(f"Temporary Email: {email_address}")
        return email_address
    else:
        print("Failed to get temporary email.")
        return None

def check_emails(email_id, domain):
    response = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={email_id}&domain={domain}")
    if response.status_code == 200:
        messages = response.json()
        return messages
    else:
        print("Failed to fetch messages.")
        return []

def read_email(email_id, domain, mail_id):
    response = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={email_id}&domain={domain}&id={mail_id}")
    if response.status_code == 200:
        mail_content = response.json()
        return mail_content
    else:
        print(f"Failed to read email with id {mail_id}.")
        return None

def main():
    email_address = get_temp_email()
    if email_address:
        email_id, domain = email_address.split('@')
        seen_emails = set()
        
        while True:
            messages = check_emails(email_id, domain)
            for message in messages:
                mail_id = message['id']
                if mail_id not in seen_emails:
                    mail_content = read_email(email_id, domain, mail_id)
                    if mail_content:
                        print(f"\nFrom: {mail_content['from']}")
                        print(f"Subject: {mail_content['subject']}")
                        print(f"Body:\n{mail_content['textBody']}")
                        print("-" * 50)
                        seen_emails.add(mail_id)
            time.sleep(10)

if __name__ == "__main__":
    main()
# mohwmmad86