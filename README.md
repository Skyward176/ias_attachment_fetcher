# Installation
`brew install tesseract`
`git clone https://github.com/Skyward176/ias_attachment_fetcher.git`
`cd ./ias_attachment_fetcher`
`python3 -m venv ./env`
`pip install -r REQUIREMENTS.txt`

# Usage
From the root directory of the script:
`touch ./.env`
Open .env in your preferred text editor.

Populate the following values:

```
ATTACHMENT_FETCHER_SERVER=""
ATTACHMENT_FETCHER_USER=""
ATTACHMENT_FETCHER_PASSWORD=""
ATTACHMENT_FETCHER_OUTPUT=""
ATTACHMENT_FETCHER_USE_INPUT=""
ATTACHMENT_FETCHER_SUBJECT=""
ATTACHMENT_FETCHER_SENDER=""
ATTACHMENT_FETCHER_FIELD=""
```
Env variable definitions:
- Server- the mail server being connected to
- User- the username of the mailbox being connected to
- Password- mailbox password
- Output- The directory of the output PDF's
- USE_INPUT - 'True' or 'False'. Determines if program will prompt for Subject, Sender, Field or use values from .env
- The term to search for in the subject line
- The sender to filter by
- UNIMPLEMENTED: The field value to extract from each PDF. As of now, it ONLY can retreive PO numbers based on the formats used at IAS.

Run the script with:
`python main.py`
Clean up the output directory with:
`python clean.py`
