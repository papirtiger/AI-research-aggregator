import feedparser
import time
from datetime import datetime

def fetch_rss(url):
    feed = feedparser.parse(url)
    results = []
    for entry in feed.entries:
        headline = entry.title
        description = entry.summary[:200] + '...' if len(entry.summary) > 200 else entry.summary
        link = entry.link
        results.append(f"Headline: {headline}\nDescription: {description}\nLink: {link}\n")
    return "\n".join(results)

# List of RSS feed URLs
feeds = [
    "http://export.arxiv.org/rss/cs.AI",
    "http://export.arxiv.org/rss/cs.CL",
    # Add more feed URLs here
]

output = f"AI Research Updates - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

for feed in feeds:
    output += f"From feed: {feed}\n"
    output += fetch_rss(feed)
    output += "\n---\n\n"

with open('ai_research_updates.txt', 'w', encoding='utf-8') as f:
    f.write(output)

print("AI research updates have been written to ai_research_updates.txt")
# ... (eksisterende kode) ...

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(filename, recipient_email):
    sender_email = os.environ.get('SENDER_EMAIL')
    password = os.environ.get('EMAIL_PASSWORD')

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "AI Research Updates"

    body = "Her er de seneste AI research opdateringer."
    message.attach(MIMEText(body, "plain"))

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(message)

# Efter at have genereret filen
if __name__ == "__main__":
    # ... (eksisterende kode til at generere filen) ...
    
    recipient_email = os.environ.get('RECIPIENT_EMAIL', 'esben@publico.dk')
    send_email("ai_research_updates.txt", recipient_email)
