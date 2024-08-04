# iOS ChatGPT Version Checker

This script checks for updates to a specified app on the Apple App Store and sends a notification if a new version is available. The notification is sent using Pushover.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Setup


1. Download and install the Pushover app on your phone:
   - [Pushover for iOS](https://apps.apple.com/app/id506088175)
   - [Pushover for Android](https://play.google.com/store/apps/details?id=net.superblock.pushover)
   - A computer (local or cloud) that is always powered on or scheduled to run the script
   - GitHub account (optional, for version control and hosting)

2. Clone this repository.
3. Install the required libraries:

```bash
pip install requests beautifulsoup4
```
## Troubleshooting
You will need to have this running in a tmux session with an always powered on computer running this, either in the cloud or on a physical machine. If you choose to use the cloud, just put a crontab entry to run this weatherchecker at any specified time you pick.
