from datetime import datetime
from ghub import Github
import schedule
import time


def make_request():
    gh = Github()

    month = datetime.now().month
    day = datetime.now().day
    year = datetime.now().year
    date = f"0{month}/{day}/{year}"

    content = f"""
## {date}
### Hello, I'm Adam(aerovize) 👋 

- :wrench: My skills: HTML, CSS, Javascript, Nodejs, Python, & Web Security.
- :bulb: Tech Interests: Security, Automation, and Backend Development.
- 🔭 I’m currently working on: Obtaining my first developer role and becoming a better one.
- 🌱 I’m currently learning: Rust
- ⚡ Fun fact: I've previously worked as an underground coal miner and commercial truck driver.
- :computer: [My Linkedin](https://www.linkedin.com/in/aweisend)"""

    resp = gh.update_file("aerovize", "updated README",
                          content, "sha", "README.md")
    if resp:
        print(resp)


def main():
    schedule.every().day.at("24:00").do(make_request)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
