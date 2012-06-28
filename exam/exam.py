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


# Authors:
#   * A. Korenev <korenev.alexander@gmail.com>

def get_folder_login_list(user):
    list = []
    for repo in g.get_user(user).get_repos():
        temp = {}        
        try:
            for commit in repo.get_commits():
                if commit.committer != None:
                    temp[commit.committer.login] = repo.name
#                    print repo.name + " " + commit.committer.login
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

#import operator
#x = { 1: 2, 3: 4, 4:3, 2:1, 7:1, 8:2 }
#sorted_x = sorted( x.iteritems(), key=operator.itemgetter(0) )
#print sorted_x


user1 = "dmitrysandalov"
user2 = "kostikgold"
user3 = "alsmirn"
user4 = "akorenev"

print user1, "wrote (sloc):", repos_sum_volume(user1)
print user1, "comitted times:", get_commits_number(user1)
print_total_people(get_folder_login_list(user3))

