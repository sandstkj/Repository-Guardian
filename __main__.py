import requests

urls = {
    'bootstrap-sass': ('https://github.com/twbs/bootstrap-sass', 'https://rubygems.org/gems/bootstrap-sass')
}

def get_git_version(dependency_name):
    response = str(requests.get('https://rubygems.org/gems/' + dependency_name).content)
    response = response.split(' ')

    for line in response:
        if line.strip().find('page__subheading') > 0:
            return line.split('>')[1].split('<')[0]


def get_mine_version(dependency_name):
    response = str(requests.get('https://github.com/twbs/' + dependency_name + '/releases'))
    # response = response.split(' ')
    #
    # for line in response:
    #     if line.strip().find('page__subheading') > 0:
    #         return line.split('>')[1].split('<')[0]


def compare_repo_to_mine(dependency_name):
    git_version = get_git_version(dependency_name)
    mine_version = get_mine_version(dependency_name)

    # ruby_mine_version = requests.get()
    # if git_hub_version != ruby_mine_version:
    #     return False
    # else:
    #     return True


gem_file = open('gem_file.txt', 'r')

for line in gem_file:
    dependency_name = line.split(' ')[1].split('\'')[1]
    print(dependency_name, 'safe?: ', compare_repo_to_mine(dependency_name))

