import requests
from dotenv import load_dotenv
from pathlib import Path
import os
import base64

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)


class Github:

    def __init__(self):
        self.url = "https://api.github.com"
        self.TOKEN = os.getenv("TOKEN")
        self.USERNAME = os.getenv("USERNAME")
        self.header = {"accept": "application/vnd.github.v3+json"}

    def get_repo(self, repo_name):
        response = requests.get(
            f"{self.url}/repos/{self.USERNAME}/{repo_name}", auth=(self.USERNAME, self.TOKEN), headers=self.header)
        return response.json()

    def get_repo_content(self, repo_name, path):
        repos = f"/repos/{self.USERNAME}/{repo_name}/contents/{path}"

        response = requests.get(
            f"{self.url}{repos}", auth=(self.USERNAME, self.TOKEN), headers=self.header)
        return response.json()

    def create_file(self, repo_name, commit_message, content, path):
        content = content.encode("utf-8")
        content = base64.b64encode(content).decode("utf-8")

        body = {
            "message": commit_message,
            "content": content,
        }

        resp = requests.put(
            f"{self.url}/repos/{self.USERNAME}/{repo_name}/contents/{path}", auth=(self.USERNAME, self.TOKEN), headers=self.header, json=body)
        return resp.json()

    def create_repository(self, repo_name):
        body = {
            "name": repo_name,
            "private": True,
        }

        resp = requests.post(f"{self.url}/user/repos",
                             auth=(self.USERNAME, self.TOKEN), headers=self.header, json=body)
        return resp.json()

    def update_file(self, repo_name, commit_message, content, sha, path):
        content = content.encode("utf-8")
        content = base64.b64encode(content).decode("utf-8")

        body = {
            "message": commit_message,
            "content": content,
            "sha": sha
        }

        resp = requests.put(
            f"{self.url}/repos/{self.USERNAME}/{repo_name}/contents/{path}", auth=(self.USERNAME, self.TOKEN), headers=self.header, json=body)
        return resp.json()
