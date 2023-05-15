#!/usr/bin/python3
""" Count it! """
import requests

def count_words(subreddit, word_list, after=None, counts={}):
    if not word_list:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        articles = data['data']['children']
        for article in articles:
            title = article['data']['title'].lower()
            for word in word_list:
                if word.lower() in title.split():
                    counts[word.lower()] = counts.get(word.lower(), 0) + 1

        after = data['data']['after']
        count_words(subreddit, word_list, after, counts)

# Example usage
count_words("python", ["Python", "Java", "javascript"])


