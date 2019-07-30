import logging
import youtube_dl
import smtplib, ssl
import environ

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


env = environ.Env()
environ.Env.read_env()


subject = "Thanks for using our service!"
body = "Here is your link to download mp3 file generated from youtube link."
sender_email = env('sender_email')
receiver_email = env('receiver_email')
password = env('password')

# Create a multipart message and set headers
email_message = MIMEMultipart()
email_message['From'] = sender_email
email_message['To'] = receiver_email
email_message['Subject'] = subject


def send_link_mail(email, link):
    options = {
        'format': 'bestaudio',
        'outtmpl': 'media/%(uploader)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        result = ydl.extract_info(link)
        print(result)
        filename = result['uploader']

    url = '127.0.0.1:8000'
    download_link = 'http://' + url + '/media/' + filename.replace(" ", "%20") + '.mp3'
    filename = filename + '.mp3'

    message = MIMEText(body + ' ' + download_link, 'plain')
    email_message.attach(message)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, email_message.as_string())

