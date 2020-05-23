import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
msg = EmailMessage()
msg['From'] = 'rats at your hostel'
msg['To'] = 'anyaogupeter601@gmail.com'
msg['Subject'] = 'you won a million dollars'

msg.set_content(html.substitute(name='peter'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('anyaogupeter602@gmail.com', '21102001hc')
    smtp.send_message(msg)
    print('message sent')

