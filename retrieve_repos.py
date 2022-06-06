import requests, json
from github import Github


def retrieve_repos(username):
    json_content = requests.get(f"https://api.github.com/users/{username}")
    conent_dict = json.loads(json_content.content)
    return int(conent_dict["public_repos"])


if __name__ == '__main__':
    print(retrieve_repos("talisainen"))
