# Instagram Automation Bot

This repository contains a Python script for automating interactions on Instagram, including logging in, liking posts, and commenting on posts. The bot uses Selenium WebDriver for browser automation. 

## Overview

The bot is designed to:
- Log in to Instagram.
- Find posts tagged with a specific hashtag.
- Like and comment on these posts.

**Note**: Due to Instagram's frequently changing restrictions on automation, the bot may require updates to keep functioning properly.

## Prerequisites

- Python 3.x
- Chrome WebDriver
- Selenium

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/MRJOHN5ON/igbot
    cd igbot
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

    **Note**: Create a `requirements.txt` file with the following content:

    ```
    selenium
    ```

## Usage

1. **Set Up Configuration**

    Create a file named `password.py` in the same directory as `bot.py` and add the following content:

    ```python
    pw = 'your_instagram_password'
    ```

    Replace `'your_instagram_password'` with your actual Instagram password.

2. **Run the Bot**

    ```bash
    python bot.py
    ```

    The bot will log in to Instagram and start interacting with posts tagged with 'travel photos'. It will repeat this process every 30 minutes.

## Code Explanation

- **`Bot` Class**: Contains methods for logging in, finding posts, liking posts, and commenting on posts.
- **`login` Method**: Handles the login process and dismisses prompts.
- **`like_comment_by_hashtag` Method**: Finds posts by hashtag, likes them, and comments on them.
- **`main` Function**: Instantiates the bot and sets it to run indefinitely with a 30-minute interval between runs.

## Notes

- The base URL for Instagram interactions is subject to change and may require updates.
- Instagram's automation restrictions may affect the bot's functionality over time.
- Ensure to comply with Instagram's terms of service regarding automation.

## Disclaimer

This repository is intended for educational purposes to demonstrate Python automation with Selenium. The base URL for Instagram interactions is private and subject to change. The purpose of this repository is to showcase my work and experience with Python automation. Use this bot responsibly and within Instagram's terms of service.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or enhancements.


