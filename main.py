import imaplib
import pypdf
import os
from dotenv import load_dotenv

PDF_DIR = "./attachments"
load_dotenv()

# uses creds in env vars to grab all email containing attachments
def get_email_list():
    mail = imaplib.IMAP4_SSL('mail.ias.edu')
    mail.login('emailaddr@gmail.com', 'password')
    mail.select('inbox')
    result, data = mail.uid('search', None, 'ALL')
    uids=data[0].split()
    result, data = mail.uid('fetch', uids[-1], 'BODYSTRUCTURE')
    print(data)
    return
# returns a list of email with attachments
# takes a list of email with attachments and downloads all attachments
# the attachments are placed into the folder specified in env vars
def download_attachments():
    return
# the returned attachments are in the output directory

# takes the name of a pdf, what we're filtering for, and returns what we wanted
def parse_pdf():
    return

# rename the pdf
def rename_pdf():
    return

# runs the steps 
def main():
    download_attachments(get_email_list())
    for file in PDF_DIR:
        rename_pdf(file, "PO" + parse_pdf(file))
    return