from dotenv import load_dotenv
import os

# this just nukes a directory, I'll have to be careful with it. Should get fool-proofed at some point
load_dotenv()
output_dir = os.environ.get("ATTACHMENT_FETCHER_OUTPUT")
def erase_all(dir):
    for file in os.listdir(dir):
        if os.path.isdir(file):
            erase_all(f"{dir}/{file}")
            continue
        else:
            os.remove(f"{dir}/{file}")
if os.path.isdir(output_dir):
    erase_all(output_dir)