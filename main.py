from imap_tools import MailBox, AND
from pypdf import PdfReader
import os
from dotenv import load_dotenv
import pytesseract
import fitz
from PIL import Image

load_dotenv()

def pdf_to_text(file): # convert to image using resolution 600 dpi 
    #pdf to image
    doc = fitz.open(file)
    for page in doc:
        mat = fitz.Matrix(2, 2)
        pixmap = page.get_pixmap(matrix=mat)
        output = f"./images/{page.number}.jpg"
        pixmap.save(output)
        img = pixmap.tobytes()

        # extract text
        text_data = ''
        text = pytesseract.image_to_string(Image.open(output))
        text_data += text + '\n'
        return text_data

# uses creds in env vars to grab all email containing attachments
def get_email_list(subject, sender):
    imap_server = os.environ.get('ATTACHMENT_FETCHER_SERVER')
    user = os.environ.get('ATTACHMENT_FETCHER_USER')
    pwd = os.environ.get('ATTACHMENT_FETCHER_PASSWORD')
    mailList = []
    try:
        with MailBox(imap_server).login(user, pwd) as mailbox:
            for msg in mailbox.fetch(AND(from_=f"{sender}", subject=f"{subject}")):
                for att in msg.attachments:
                    if att.filename.endswith(".pdf"):
                        mailList.append((msg.subject, att))
        return mailList
    except:
        exit(f"Failed to get mail for {user}")
# returns a list of email with attachments

# Copy the PDF attachment into output directory
def copy_att(att, output_dir):
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    with open(f"{output_dir}/{att.filename}", 'wb') as f:
        f.write(att.payload)
    return

# takes the name of a pdf, what we're filtering for, and returns what we wanted
# currenty this is going to be locked to PO until i can get generic
def parse_pdf(file, field):
    data = pdf_to_text(file)
    
    return data
# rename the pdf
def get_filter_input(): # Could be skipped by env vars
    sender = input("Please input the sender to filter by: ")
    subject = input("Please input the subject keyword(s) to filter by: ")
    field = "PO #"
    field = input("Please input the target field for naming(leave blank for PO): ")
    return(subject, sender,field)
# runs the steps 
def main():
    #subject = os.environ.get("ATTACHMENT_FETCHER_SUBJECT")
    #sender = os.environ.get("ATTACHMENT_FETCHER_SENDER")

    if(os.environ.get("ATTACHMENT_FILTER_USE_INPUT") == True ):
        (subject, sender, field) = get_filter_input()
    else:
        subject = os.environ.get("ATTACHMENT_FETCHER_SUBJECT")
        sender = os.environ.get("ATTACHMENT_FETCHER_SENDER")
        field = os.environ.get("ATTACHMENT_FETCHER_FIELD")
    
    mailList = get_email_list(subject, sender) # This has a list of all subject lines of emails containing PDF attachments and the containe PDF
    output_dir = os.environ.get("ATTACHMENT_FETCHER_OUTPUT")
    for mail in mailList:
        copy_att(mail[1], output_dir)
        print(f"{mail[0]}:  {mail[1].filename}")
    for file in os.listdir(output_dir):
        cur_name = f"{output_dir}/{file}"
        print(cur_name)
        tokens = parse_pdf(cur_name, "#").split()
        for index, token in enumerate(tokens):
            if token == "#" or token == "#-" or token == "Po#" or token == "PO#":
                os.rename(f"{output_dir}/{file}", f"{output_dir}/po{tokens[index+1]}.pdf")
                continue
    #     # rename_pdf(cur_name, parse_pdf(cur_name, field)) # rename the pdf with the value of the field we filter by
    return
if __name__ == "__main__":
    main()