from dotenv import load_dotenv
import os

# this just nukes a directory, I'll have to be careful with it. Should get fool-proofed at some point
load_dotenv()
output_dir = os.environ.get("ATTACHMENT_FETCHER_OUTPUT")
if os.path.isdir(output_dir):
    for file in os.listdir(output_dir):
        os.remove(f"{output_dir}/{file}")