import sys
import os
from github import Github

path = "/Users/Benjo/Sublime/"

username = "onibenjo"
# password = "benjamin232"
password = sys.argv[1]

def create():
    folderName = str(sys.argv[2])
    os.makedirs(path + folderName)
    user = Github(username, password).get_user()
    user.create_repo(sys.argv[2])
    print("Succesfully created repository {}".format(sys.argv[2]))
    

if __name__ == "__main__":
    create()