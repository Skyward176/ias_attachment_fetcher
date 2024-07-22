import imaplib
from imap_tools import MailBox, AND
import pypdf
import os
from dotenv import load_dotenv

PDF_DIR = "./attachments"
load_dotenv()

# uses creds in env vars to grab all email containing attachments
def get_email_list():
    user = os.environ.get('ATTACHMENT_FETCHER_USER')
    pwd = os.environ.get('ATTACHMENT_FETCHER_PASSWORD')
    mailList = []
    try:
        with MailBox('mail.ias.edu').login(user, pwd) as mailbox:
            for msg in mailbox.fetch():
                for att in msg.attachments:
                    if att.filename.endswith(".pdf"):
                        mailList.append((msg.subject, att))
        print(mailList)
        return mailList
    except:
        exit(f"Could not login as {user}")
# def get_email_list():
    # mail = imaplib.IMAP4_SSL('mail.ias.edu')
    # user = os.environ.get('ATTACHMENT_FETCHER_USER')
    # if user == None:
        # exit("Did not find a username")
    # password = os.environ.get('ATTACHMENT_FETCHER_PASSWORD')
    # if password == None:
        # exit("Did not find a password")
    # try:
        # print(f"Attempting to login as {user} with password {password}")
        # mail.login(user, password)
    # except:
        # exit(f"Could not login as {user}")
    # mail.select('inbox')
    # result, data = mail.uid('search', 'ALL')
    # uids=data[0].split()
    # for message in uids:
        # result, data = mail.uid('fetch', message, 'BODYSTRUCTURE')
        # print(data)
    # return
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
    mailList = get_email_list() # This has a list of all subject lines of emails containing PDF attachments and the containe PDF
    for mail in mailList:
        print(f"{mail[0]}:  {mail[1].filename}")
    #download_attachments(get_email_list())
    #for file in PDF_DIR:
    #    rename_pdf(file, "PO" + parse_pdf(file))
    return
if __name__ == "__main__":
    main()