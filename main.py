from datetime import datetime
from ghub import Github
from logger import *
import schedule
import time


def getDate():
    dt = datetime.now()
    datestamp = dt.strftime("%Y-%m-%d")
    return datestamp


def make_request():
    gh = Github()
    # Fetch the sha value for the file, to use as part of the update request.
    data = gh.get_repo_content("aerovize", "README.md")
    sha = data["sha"]

    date = getDate()
    # Add the current date to the content of the file.
    content = f"""
## {date}
### Hello, I'm Adam(aerovize) 👋 

- :wrench: My skills: HTML, CSS, Javascript, Nodejs, Python, & Web Security.
- :bulb: Tech Interests: Security, Automation, and Backend Development.
- 🔭 I’m currently working on: Obtaining my first developer role and becoming a better one.
- 🌱 I’m currently learning: Rust
- ⚡ Fun fact: I've previously worked as an underground coal miner and commercial truck driver.
- :computer: [My Linkedin](https://www.linkedin.com/in/aweisend)"""

    # Make the update request
    update_resp = gh.update_file("aerovize", "updated README",
                                 content, sha, "README.md")
    if update_resp:
        # Log respone to log file.
        log_string = log_response(update_resp)
        log_file(log_string)


def scheduler():
    # Runs the script at 12:01 AM to update the date.
    schedule.every().day.at("00:01").do(make_request)

    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    scheduler()


if __name__ == '__main__':
    main()
