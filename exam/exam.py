from github import Github
from github import GithubException

# Authors:
#   * A. Balyanova <bal0102@yandex.ru>
#   * D. Sandalov  <dmitry@sandalov.org>

def get_commits_number(user):
    commits_number = 0
    for repo in g.get_user(user).get_repos():
        if repo.size != 0:
            commits_number += sum(1 for e in repo.get_commits())
    return commits_number


# Authors:
#   * K. Sokolov   <kostikgold@gmail.com>
#   * D. Sandalov  <dmitry@sandalov.org>

def repos_sum_volume(user):
    sum_repository = 0
    for repo in g.get_user(user).get_repos():
        sum_repository += repo.size
    return sum_repository


# Author:
#   * A. Korenev <korenev.alexander@gmail.com>

def get_folder_login_list(user):
    list = []
    for repo in g.get_user(user).get_repos():
        temp = {}        
        try:
            for commit in repo.get_commits():
                if commit.committer != None:
                    temp[commit.committer.login] = repo.name
            list.append(temp)
        except:
            print "creating empty folder"
    return list

def print_total_people(list):
    for x in list:
        print "--------------------------------"
        print "folder:", x.values()[0], ":"
        for login in x.keys():
            print "login: ", login
        print "total:", len(x)

#g = Github()
#user = "alsmirn"
#print user, "wrote (sloc):", repos_sum_volume(user)
#print user, "comitted times:", get_commits_number(user)
#print_total_people(get_folder_login_list(user))



# Author:
#   * E. Shibalkin <shibalkin@rambler.ru>

class My_Github(Github):
    def get_user(self, login=None):
        if login is None:
            login = raw_input("Enter Github username: ")
        while 0 == 0:
            try:
                return Github.get_user(self, login)
            except (GithubException):
                if raw_input ("User not found. Continue? (y|n): ") == "n":
                    exit(0)
                else:
                    login = raw_input("Enter Github username: ")

g = My_Github()
user = g.get_user()
print user._login, "wrote (sloc):", repos_sum_volume(user._login)
print user._login, "comitted times:", get_commits_number(user._login)
print_total_people(get_folder_login_list(user._login))