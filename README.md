# get Reddit comments for Talk to the City

This script allows you to scrape comments from a specific Reddit post and save them to a CSV file for Talk to the City, using the Reddit API through the praw library and saving the results to the reddit-comments.csv file The results are saved in the reddit-comments.csv file.

## Features
- Scrapes all comments (including nested ones) from a specified Reddit post.
- Saves the comments in a CSV file with two columns: `comment-id` (unique identifier) and `comment-body` (content of the comment).
- Uses environment variables for Reddit API credentials via a `.env` file for security.

## Prerequisites

Before using the script, make sure you have the following installed:

- Python 3.6 or higher
- `praw` library for accessing Reddit API
- `pandas` library for handling CSV file creation
- `python-dotenv` for loading environment variables

You can install the required Python libraries using the following command:

```bash
pip install praw pandas python-dotenv
```

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/reddit-comment-scraper.git
   cd reddit-comment-scraper
   ```

2. **Create a Reddit Application**:
   - Go to https://www.reddit.com/prefs/apps.
   - Scroll down to the "Developed Applications" section and click "Create App" or "Create Another App."
   - Set the app type to "script" and fill in the necessary fields.
   - Once created, you'll receive a `client_id` and `client_secret`.

3. **Create a `.env` file**:
   In the root of the project, create a `.env` file and add your Reddit API credentials:

   ```bash
   CLIENT_ID=your_client_id
   CLIENT_SECRET=your_client_secret
   USER_AGENT=your_user_agent
   ```

   Example `.env` file:

   ```.env
   CLIENT_ID=abcd1234
   CLIENT_SECRET=efgh5678
   USER_AGENT=script:reddit_comment_scraper.0 (by u/your_reddit_username)
   ```

## Usage

1. **Edit the script**:
Open the Python script and update the `post_url` variable with the URL of the Reddit post you want to scrape comments from.

Example:
```python
post_url = "https://www.reddit.com/r/AskReddit/comments/108ijlw/whats_your_first_thought_when_thinking_about_japan/"
```

2. **Run the script**:
Once the environment variables are set and the post URL is updated, run the script:

```bash
python main.py
```

This will create a file called `reddit-comments.csv` in the current directory with all the comments from the specified Reddit post.

## Output

The CSV file will have the following structure:

| comment-id | comment-body        |
|------------|---------------------|
| 1          | First comment text   |
| 2          | Second comment text  |
| ...        | ...                  |

## supplementary information
This README was created by ChatGPT.