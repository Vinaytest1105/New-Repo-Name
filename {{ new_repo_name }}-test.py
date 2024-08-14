import requests

# Replace these with your actual values
GITHUB_TOKEN = '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'
REPO_OWNER = 'Vinaytest1105'
REPO_NAME = 'GitHubApp14'

def get_repo_details(owner, repo_name, token):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github+json'
    }
    url = f'https://api.github.com/repos/{owner}/{repo_name}'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def main():
    repo_details = get_repo_details(REPO_OWNER, REPO_NAME, GITHUB_TOKEN)
    owner_info = repo_details['owner']
    owner_type = owner_info['type']
    owner_name = owner_info['login']
    
    print(f"The repository '{REPO_NAME}' is owned by a {owner_type}: {owner_name}.")

if __name__ == '__main__':
    main()