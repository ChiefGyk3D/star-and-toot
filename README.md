# Star and Toot
## GitHub Starred Repo Notifier for Mastodon

This is a simple bot that monitors starred repositories on GitHub and posts a status update on Mastodon whenever a new repository is starred.

Note: This bot is currently under testing. If you encounter any bugs or issues, please report them through the issue tracker.

## Setup 

1. Clone this repository.
2. Install the necessary dependencies using pip:

```
pip install -r requirements.txt
```

3. Obtain your GitHub Personal Access Token and Mastodon API Access Token.
4. Create a config.ini file in the project directory based on config_template.ini and add your GitHub and Mastodon API credentials:

```
[GitHub]
access_token = your_github_token

[Mastodon]
access_token = your_access_token_here
api_base_url = https://your.mastodon.instance
client_id = your_client_id_here
client_secret = your_client_secret_here
```

5. Run the bot:

```
    python star-and-toot.py
```

## Configuration

All configuration is done through the config.ini file. You'll need to provide your GitHub and Mastodon API credentials:

- GitHub.access_token: Your GitHub Personal Access Token.
- Mastodon.access_token: Your Mastodon API Access Token.
- Mastodon.api_base_url: Your Mastodon instance URL.

Remember to replace 'your_github_token', 'your_mastodon_token', and 'your_mastodon_instance_url' with your actual tokens and URLs in the config.ini file.
Contributing

We welcome contributions of all kinds. If you have a feature request, bug report, or code contribution, please use the issue tracker or open a pull request.