# Star and Toot

## GitHub Starred Repo Notifier for Mastodon

"Star and Toot" is a bot that monitors when you star new repositories on GitHub and posts a status update ("Toot") on your Mastodon account. As a secondary feature, it can also post to Twitter. However, we emphasize a Mastodon-first approach to microblogging in this project.

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

[Twitter]
enable_twitter = false
consumer_key = your_consumer_key
consumer_secret = your_consumer_secret
access_token = your_access_token
access_token_secret = your_access_token_secret
```

5. Run the bot:

```
    python star-and-toot.py
```

## Running as a systemd Service

If you are running this bot on a system with systemd, you can configure it as a service so it starts automatically on system boot. Follow these steps:

1. Create a systemd service file, e.g., star-and-toot.service. Service files are typically stored in /etc/systemd/system/:

```
sudo nano /etc/systemd/system/star-and-toot.service
```

2. In the service file, add the following content (replace user and /path/to/script with your actual username and the absolute path to your Python script):

```
[Unit]
Description=Star and Toot GitHub-Mastodon integration

[Service]
ExecStart=/usr/bin/python3 /path/to/star-and-toot.py
User=user
Restart=always

[Install]
WantedBy=multi-user.target
```

3. Reload the systemd manager configuration:

```
sudo systemctl daemon-reload
```

4. Start the service:

```
sudo systemctl start star-and-toot.service
```

5. Enable the service to start on boot:

```
sudo systemctl enable star-and-toot.service
```

## Configuration

All configuration is done through the config.ini file. You'll need to provide your GitHub and Mastodon API credentials:

- GitHub.access_token: Your GitHub Personal Access Token.
- Mastodon.access_token: Your Mastodon API Access Token.
- Mastodon.api_base_url: Your Mastodon instance URL.

Remember to replace 'your_github_token', 'your_mastodon_token', and 'your_mastodon_instance_url' with your actual tokens and URLs in the config.ini file.
Contributing

## Support

You can also tip the author with the following cryptocurrency addresses:

    Bitcoin: bc1q5grpa7ramcct4kjmwexfrh74dvjuw9wczn4w2f
    Monero: 85YxVz8Xd7sW1xSiyzUC5PNqSjYLYk4W8FMERVkvznR38jGTBEViWQSLCnzRYZjmxgUkUKGhxTt2JSFNpJuAqghQLhHgPS5
    PIVX: DS1CuBQkiidwwPhkfVfQAGUw4RTWPnBXVM
    Ethereum: 0x2a460d48ab404f191b14e9e0df05ee829cbf3733

## Connect
- [ChiefGyk3D's Mastodon Account](https://social.chiefgyk3d.com/@chiefgyk3d)
