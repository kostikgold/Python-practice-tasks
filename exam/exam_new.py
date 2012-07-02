#!/usr/bin/env python

from github import Github
from github import GithubException

# Authors:
#   * A. Balyanova <bal0102@yandex.ru>
#   * D. Sandalov  <dmitry@sandalov.org>

def get_commits_number(user):
    commits_number = 0
    for repo in user.get_repos():
        if repo.size != 0:
            commits_number += len(list(repo.get_commits()))

    return commits_number
    
    # OR
    #get_repo_len = lambda repo: len(list(repo.get_commits()))

    #return sum(get_repo_len(repo) for repo in user.get_repos() if repo.size != 0)


# Authors:
#   * K. Sokolov   <kostikgold@gmail.com>
#   * D. Sandalov  <dmitry@sandalov.org>

def repos_sum_volume(user):
    return sum(repo.size for repo in user.get_repos())


# Author:
#   * A. Korenev <korenev.alexander@gmail.com>

def get_folder_login_list(user):
    
    commiters = []

    for repo in user.get_repos():
        
        if not repo.size:
            print "Repo %s is empty." % repo.name 
            continue

        commiters_tmp = {}
        
        for commits in repo.get_commits():
            if commits.committer is not None:
                commiters_tmp[commits.committer.login] = repo.name

        commiters.append(commiters_tmp)

    return commiters

def print_total_people(commiters):
    for x in commiters:
        print "-" * 20
        print "folder: %s:" % x.values()[0]

        for login in x.keys():
            print "login: ", login

        print "total: %d" % len(x)

#g = Github()
#user = "alsmirn"
#print user, "wrote (sloc):", repos_sum_volume(user)
#print user, "comitted times:", get_commits_number(user)
#print_total_people(get_folder_login_list(user))



# Author:
#   * E. Shibalkin <shibalkin@rambler.ru>

class MyGithub(Github):
    def get_user(self, login=""):
        login = raw_input("Enter Github username: ")

        if login in ("exit", "quit"):
            print "Thanks for using this application. Bye!"
            exit(0)

        try:
            return Github.get_user(self, login)
        except GithubException:
            print("User not found. Try again?")
            self.get_user()


g = MyGithub()
user = g.get_user()
print user._login, "wrote (sloc):", repos_sum_volume(user)
print user._login, "comitted times:", get_commits_number(user)
print_total_people(get_folder_login_list(user))
