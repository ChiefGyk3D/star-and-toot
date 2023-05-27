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

# Create Mastodon API instance
mastodon = Mastodon(
    access_token=mastodon_token,
    api_base_url=mastodon_api_base_url
)

# Get your user
user = g.get_user()

# Get list of currently starred repos
starred = [repo for repo in user.get_starred()]
print("You have starred", len(starred), "repositories.")

# Periodically check for new starred repos
while True:
    time.sleep(60)  # wait for 60 seconds

    # Get updated list of starred repos
    updated_starred = [repo for repo in user.get_starred()]

    # Compare lists to find new stars
    new_stars = set(updated_starred) - set(starred)

    for repo in new_stars:
        # Create new status update
        mastodon.status_post("I just starred a new repository: " + repo.html_url)

    # Update list of starred repos
    starred = updated_starred
