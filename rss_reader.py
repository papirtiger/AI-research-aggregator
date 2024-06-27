import feedparser
import time
from datetime import datetime

def fetch_rss(url):
    feed = feedparser.parse(url)
    results = []
    for entry in feed.entries:
        headline = entry.title
        description = entry.summary[:200] + '...' if len(entry.summary) > 200 else entry.summary
        link = entry.link
        results.append(f"Headline: {headline}\nDescription: {description}\nLink: {link}\n")
    return "\n".join(results)

# List of RSS feed URLs
feeds = [
    "http://export.arxiv.org/rss/cs.AI",
    "http://export.arxiv.org/rss/cs.CL",
    # Add more feed URLs here
]

output = f"AI Research Updates - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

for feed in feeds:
    output += f"From feed: {feed}\n"
    output += fetch_rss(feed)
    output += "\n---\n\n"

with open('ai_research_updates.txt', 'w', encoding='utf-8') as f:
    f.write(output)

print("AI research updates have been written to ai_research_updates.txt")
