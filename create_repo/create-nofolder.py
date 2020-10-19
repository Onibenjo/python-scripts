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
    # folderName = str(sys.argv[2])
    # os.makedirs(path + folderName)
    g = Github(username, password)
    # g = Github(access_token)
    user = g.get_user()
    user.create_repo(reponame)
    print("------No folder created-----")
    print("Succesfully created repository {}".format(sys.argv[2]))
    print("-- git remote add origin git@github.com:{}/{}.git".format(username, sys.argv[2]))
    print("URL: https://github.com/{}/{}".format(username, sys.argv[2]))

if __name__ == "__main__":
    create()