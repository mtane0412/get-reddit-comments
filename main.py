import praw
import pandas as pd
import os
from dotenv import load_dotenv

# .envファイルの内容を読み込む
load_dotenv()


# Reddit APIの認証情報を入力
reddit = praw.Reddit(
    client_id=os.environ['CLIENT_ID'],
    client_secret=os.environ['CLIENT_SECRET'],
    user_agent=os.environ['USER_AGENT']
)

# スレッドURLまたはIDを指定してコメントを取得
post_url = "https://www.reddit.com/r/AskReddit/comments/108ijlw/whats_your_first_thought_when_thinking_about_japan/"
submission = reddit.submission(url=post_url)

# コメントを抽出
comments_data = []
submission.comments.replace_more(limit=None)  # 省略されたコメントもすべて取得
for i, comment in enumerate(submission.comments.list()):
    comments_data.append({
        "comment-id": i + 1,  # ユニークな数字としてi+1を使用
        "comment-body": comment.body
    })

# データをCSVに保存
df = pd.DataFrame(comments_data)
df.to_csv("reddit-comments.csv", index=False)

print("コメントがCSVファイルに保存されました。")