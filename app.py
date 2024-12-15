from github import Github
import os
import requests

token = "Token da api do GitHub"

repo_url = "Link do repositorio"

folder_de_destino = "downloads"

g = Github(token)

repo_name = repo_url.split('/')[-2] + "/" + repo_url.split('/')[-1]

repo = g.get_repo(repo_name)

repo_clone_url = repo.clone_url.replace('https://', f'https://{token}@')
os.system(f'git clone {repo_clone_url} {folder_de_destino}')