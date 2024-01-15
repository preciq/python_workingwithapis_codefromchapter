from operator import itemgetter
import requests

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
# retrieves the top stories from hacker-news, in JSON format as keys, values and lists
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
# converts the top stories json string into a json object for processing below

submission_dicts = []
for submission_id in submission_ids[:5]:
    # loops through the top 5 stories returned from top stories get request above
    
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    # makes a get request for each of the top 5 stories and saves the response in 'r'
    
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    # prints the id and status of the request for each of the above articles
    
    response_dict = r.json()
    # Build a dictionary (json object) for each article.
    
    submission_dict = {
        'title': response_dict['title'],
        # extracts title of the current article
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        # extracts link of the current article (actually just generates it with an f string and predeterminied template, into which the submission_id is inserted)
        'comments': response_dict['descendants'],
        # extracts comments of the current article
    }
    # takes the above specified elements and make a dictionary out of them, for use later (basically a condensed grouping of elements from each article that we deem important (title, link and comments))
    
    submission_dicts.append(submission_dict)
    # appends the extracted information dictionary to submission_dicts, for usage below

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
# sorts the extracted information dictionaries by number of comments; the submission_dict with the highest number of comments is first in line
# this is because reverse=True

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
# prints the desired data from each submission_dict (the list containing these has been sorted)