import feedparser
import time

def fetch_rss(url):
    feed = feedparser.parse(url)
    for entry in feed.entries:
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Published: {entry.published}")
        print(f"Summary: {entry.summary}\n")

# List of RSS feed URLs
feeds = [
    "http://export.arxiv.org/rss/cs.AI",
    "http://export.arxiv.org/rss/cs.CL",
    # Add more feed URLs here
]

while True:
    for feed in feeds:
        print(f"Fetching feed: {feed}")
        fetch_rss(feed)
    
    # Wait for an hour before checking again
    time.sleep(3600)
