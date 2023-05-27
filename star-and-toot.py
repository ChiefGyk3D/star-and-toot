import time
from github import Github
from mastodon import Mastodon
import configparser

# Parse the config file
config = configparser.ConfigParser()
config.read('config.ini')

# Get GitHub access token from config
gh_token = config.get('GitHub', 'access_token')

# Create GitHub API instance
g = Github(gh_token)

# Get Mastodon API credentials from config
mastodon_token = config.get('Mastodon', 'access_token')
mastodon_api_base_url = config.get('Mastodon', 'api_base_url')
mastodon_client_id = config.get('Mastodon', 'client_id')
mastodon_client_secret = config.get('Mastodon', 'client_secret')

# Append /api/v1 to the base URL if it is not already present
if not mastodon_api_base_url.endswith('/api/v1'):
    mastodon_api_base_url += '/api/v1'

# Create Mastodon API instance
mastodon = Mastodon(
    client_id=mastodon_client_id,
    client_secret=mastodon_client_secret,
    access_token=mastodon_token,
    api_base_url=mastodon_api_base_url
)

# Get your user
user = g.get_user()

# Get list of currently starred repos
starred = [repo for repo in user.get_starred()]
print("You have starred", len(starred), "repositories.")

# Function to check for new starred repos
def check_for_new_starred_repos():
    global starred
    new_starred = [repo for repo in user.get_starred() if repo not in starred]
    if new_starred:
        print("You have starred", len(new_starred), "new repositories.")
        for repo in new_starred:
            message = f"I just starred a new repository on GitHub: {repo.html_url}"
            mastodon.status_post(message)
        starred = user.get_starred()

# Periodically check for new starred repos
while True:
    check_for_new_starred_repos()
    time.sleep(60)  # wait for 60 seconds