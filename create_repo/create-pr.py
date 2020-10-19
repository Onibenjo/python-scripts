import os
import sys
from github import Github

# path = "/Users/Benjo/Sublime/"

username = "onibenjo"
# password = sys.argv[1]
password = input('Enter your github password: ')
reponame = input('Enter the name of the repository: ')

# print("python <filename> <password> <reponame>")
def create():
    g = Github(username, password)

    user = g.get_user()

    repo = user.get_repo(reponame)
    title = input('Enter title: ')
    body = input('Enter body text: ')
    head = input('Enter head (main) branch: ')
    base = input('Enter base branch: ')

    repo.create_pull(title=title, body=body, head=head, base=base)
    
    print("PR created successfully")

if __name__ == "__main__":
    create()