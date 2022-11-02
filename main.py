# from job_korea import get_pages, extract_job_korea
# from file import save_to_file

# user_input = input("Which job are you looking for?")

# get_pages(user_input)
# job_korea = extract_job_korea(user_input)

# save_to_file(user_input, job_korea)

from flask import Flask

app = Flask("JobScapper")

@app.route("/")
def home():
    return 'Hey there!(TEST)'

app.run("127.0.0.1")




