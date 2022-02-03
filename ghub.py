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
        # Fetches a single repository
        try:
            response = requests.get(
                f"{self.url}/repos/{self.USERNAME}/{repo_name}", auth=(self.USERNAME, self.TOKEN), headers=self.header)
            return response.json()
        except requests.ConnectionError as err:
            return f"A error has occured trying to connect to the repository: {repo_name}, Error: {repr(err)}"

    def get_repo_content(self, repo_name, path):
        # Fetches file content from a single repository
        repos = f"/repos/{self.USERNAME}/{repo_name}/contents/{path}"
        try:
            response = requests.get(
                f"{self.url}{repos}", auth=(self.USERNAME, self.TOKEN), headers=self.header)
            return response.json()
        except requests.ConnectionError as err:
            return f"A error has occured trying to connect to: {repo_name}/{path}, Error: {repr(err)}"

    def create_file(self, repo_name, commit_message, content, path):

        # Creates a new file in a repository

        content = content.encode("utf-8")
        content = base64.b64encode(content).decode("utf-8")

        body = {
            "message": commit_message,
            "content": content,
        }
        try:
            response = requests.put(
                f"{self.url}/repos/{self.USERNAME}/{repo_name}/contents/{path}", auth=(self.USERNAME, self.TOKEN), headers=self.header, json=body)
            return response.json()
        except requests.ConnectionError as err:
            return f"A error has occured trying to add the file: {path} to the repository: {repo_name}, Error: {err}"

    def create_repository(self, repo_name):
        # Creates a new repository
        body = {
            "name": repo_name,
            "private": True,
        }
        try:
            resp = requests.post(f"{self.url}/user/repos",
                                 auth=(self.USERNAME, self.TOKEN), headers=self.header, json=body)
            return resp.json()
        except requests.ConnectionError as err:
            return f"A error has occured trying to create: {repo_name}, Error: {err}"

    def update_file(self, repo_name, commit_message, content, sha, path):
        # Updates a file in a repository
        # requires from the API, the sha value for the file
        content = content.encode("utf-8")
        content = base64.b64encode(content).decode("utf-8")

        body = {
            "message": commit_message,
            "content": content,
            "sha": sha
        }
        try:
            resp = requests.put(
                f"{self.url}/repos/{self.USERNAME}/{repo_name}/contents/{path}", auth=(self.USERNAME, self.TOKEN), headers=self.header, json=body)
            return resp.json()
        except requests.ConnectionError as err:
            return f"A error has occured trying to update: {path} in the repo {repo_name}, Error: {err}"
