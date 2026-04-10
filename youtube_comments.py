from googleapiclient.discovery import build
import pandas as pd

api_key = "AIzaSyDtlodnXUi-8rUMfKdKH6uyI03g59yPqCY"

youtube = build('youtube', 'v3', developerKey=api_key)

video_id = "dQw4w9WgXcQ"  # change this

comments = []

request = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    maxResults=50
)

response = request.execute()

for item in response['items']:
    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
    comments.append(comment)

df = pd.DataFrame(comments, columns=["Comment"])
df.to_csv("comments.csv", index=False)

print("Comments saved successfully!")