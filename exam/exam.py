from Github import Github
g = Github()

# Authors:
#   * A. Balyanova <bal0102@yandex.ru>
#   * E. Shibalkin <shibalkin@rambler.ru>
#   * D. Sandalov  <dmitry@sandalov.org>

def get_commits_number(user):
    commits_number = 0
    for repo in g.get_user(user).get_repos():
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

# Authors:
#   * A. Korenev <korenev.alexander@gmail.com>

def f():
        list = []
        for x in g.get_user("alsmirn").get_repos():
                for y in x.get_commits():
                        for z in list:
                                if list[z] != y.committer or len(list) == 0:
                                        list.append( y.committer )
        return list


user = "dmitrysandalov"
#user = "alsmirn"
print user, "wrote (sloc):", repos_sum_volume(user)
print user, "comitted times:", get_commits_number(user)
f()

