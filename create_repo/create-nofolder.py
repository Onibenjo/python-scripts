import os
import sys
from github import Github

# path = "/Users/Benjo/Sublime/"

username = "onibenjo"
# password = "benjamin232"
password = sys.argv[1]
print("python <filename> <password> <reponame>")
def create():
    # folderName = str(sys.argv[2])
    # os.makedirs(path + folderName)
    user = Github(username, password).get_user()
    user.create_repo(sys.argv[2])
    print("------No folder created-----")
    print("Succesfully created repository {}".format(sys.argv[2]))
    print("-- git remote add origin git@github.com:{}/{}.git".format(username, sys.argv[2]))
    print("URL: https://github.com/{}/{}".format(username, sys.argv[2]))

if __name__ == "__main__":
    create()