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
        print "-"*40
        print "folder:", x.values()[0], ":"
        for login in x.keys():
            print "login: ", login
        print "total:", len(x)

#g = Github()
#user = "alsmirn"
#print user, "wrote (sloc):", repos_sum_volume(user)
#print user, "comitted times:", get_commits_number(user)
#print_total_people(get_folder_login_list(user))

# Authors:
#   * K. Sokolov   <kostikgold@gmail.com>
#   * A. Smirnov <alsmirnn@gmail.com>


def ask_ok(prompt, retries=4, complaint='Yes' or 'No'):
    while 1:
        ok = raw_input(prompt)
        if ok in ('Y', 'Yes'): return 1
        if ok in ('N', 'No', 'Not'): return 0
        retries = retries - 1
        if retries < 0:
            raise IOError('User don\'t answer!')
        print complaint

# Author:
#   * E. Shibalkin <shibalkin@rambler.ru>
#   * K. Sokolov   <kostikgold@gmail.com>

class My_Github(Github):
    def get_user(self, login=None):
        if login is None:
            login = raw_input("Enter Github username: ")
        while 1:
            try:
                return Github.get_user(self, login)
            except (GithubException):
                if ask_ok("User unknown. Do you want to continue?"):
                    login = raw_input("Enter Github username: ")
                else:
                    exit(0)

g = My_Github()
user = g.get_user()
print user._login, "wrote (sloc):", repos_sum_volume(user._login)
print user._login, "comitted times:", get_commits_number(user._login)
print_total_people(get_folder_login_list(user._login))