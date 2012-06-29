from github import Github
from github import GithubException

# Authors:
#   * A. Balyanova <bal0102@yandex.ru>
#   * D. Sandalov  <dmitry@sandalov.org>

def get_commits_number(user):
    commits_number = 0
    for repo in user.get_repos():
        if repo.size != 0:
            commits_number += sum(1 for e in repo.get_commits())
    return commits_number


# Authors:
#   * K. Sokolov   <kostikgold@gmail.com>
#   * D. Sandalov  <dmitry@sandalov.org>

def repos_sum_volume(user):
    sum_repository = 0
    for repo in user.get_repos():
        sum_repository += repo.size
    return sum_repository


# Author:
#   * A. Korenev <korenev.alexander@gmail.com>

def get_folder_login_list(user):
    list = []
    for repo in user.get_repos():
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
    def get_user(self, login=raw_input("Enter Github username: ")):
        while 1:
            try:
                return Github.get_user(self, login)
            except (GithubException):
                print ("User not found")
                if ask_ok("Try again") == 1:
                    login = raw_input("Enter Github username: ")
                else:
                    print ("Thanks for using this application. Bye!")
                    exit(0)

def ask_ok(prompt, retries=3, complaint='[Y/n]? '):
# example from lecture 1, modified by E. Shibalkin <shibalkin@rambler.ru>
    for i in xrange(retries):
        ok = raw_input(prompt + " " + complaint)
        if ok in ("Y", "Yes", "y"): return 1
        if ok in ("N", "No", "Not", "n"): return 0
        if i == retries-1:
            raise IOError("User doesn't respond!")

g = My_Github()
user = g.get_user()
print user._login, "wrote (sloc):", repos_sum_volume(user)
print user._login, "comitted times:", get_commits_number(user)
print_total_people(get_folder_login_list(user))