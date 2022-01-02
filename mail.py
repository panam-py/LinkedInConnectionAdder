import os
import pickle
# Gmail utils
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# Encoding/decoding messages in base64
from base64 import urlsafe_b64decode, urlsafe_b64encode
# For dealing with attachment MIME types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from mimetypes import guess_type as guess_mime_type

# Request all access (permisssion to read/send/recieve emails, manage the inbox and more)
SCOPES = ["https://mail.google.com/"]
my_email = 'panampraisehebron@gmail.com'

