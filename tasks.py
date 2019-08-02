from pytube import YouTube
import subprocess
import os
import smtplib, ssl


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from celery import Celery


app = Celery('tasks', broker='redis://localhost')
app.conf.broker_url = 'redis://localhost:6379/0'




subject = "Thanks for using our service!"
body = "Here is your link to download mp3 file generated from youtube link."
sender_email = 'vdconvertermp3@gmail.com'

password = 'videoconverter123'

# Create a multipart message and set headers
email_message = MIMEMultipart('alternative')
email_message['From'] = sender_email

email_message['Subject'] = subject


@app.task
def send_link_mail(email, link):
    link_vid = link
    yt = YouTube(link_vid)
    stream = yt.streams.first()
    directory = '/home/kadyrov02/DjangoProjects/custom_fw/media'
    stream.download(directory)
    default_filename = (stream.default_filename)
    filename = 'converted_audio.mp3'
    subprocess.call(['ffmpeg', '-i',
                     os.path.join(directory, default_filename),
                     os.path.join(directory, filename)
                     ])

    url = '127.0.0.1:9090'
    download_link = 'http://' + url + '/media/' + filename.replace(" ", "%20")


    receiver_email = email
    email_message['To'] = receiver_email
    message = MIMEText(body + ' ' + download_link, 'plain')
    email_message.attach(message)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, email_message.as_string())

