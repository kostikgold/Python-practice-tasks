from github import Github

g = Github()


# Authors:
#   * A. Balyanova <bal0102@yandex.ru>
#   * E. Shibalkin <shibalkin@rambler.ru>
#   * D. Sandalov  <dmitry@sandalov.org>

def get_commits_number(user):
    commits_number = 0
    for repo in g.get_user(user).get_repos():
        if repo.size != 0:
            for i in repo.get_commits():
                commits_number +=1
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


user = "alsmirn"
print user, "wrote (sloc):", repos_sum_volume(user)
print user, "comitted times:", get_commits_number(user)
print_total_people(get_folder_login_list(user))

