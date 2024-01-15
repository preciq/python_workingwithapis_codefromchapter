import requests

"""Making an API Call, checking response of the call"""

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
# url is divided up into 2 lines for simplicity
# first line is the "base url", against which all requests will be made
# second line contains the part of the url with queries (after the '?')
    # three queries exist -->
    # language, which is python (looking for repos containing the python programming language)
    # sort, which is stars (filters the repos based on stars)
    # and stars, which is greater than 10k (returns repos that have more than 10k stars)
    # these queries will be passed along the request to give us a specific response

headers = {"Accept": "application/vnd.github.v3+json"}
# headers are another type of parameter that is accepted by the request
# here we are specifying that we want to accept the response from the third version of the github API (v3) and as a json
# note that "headers" takes the form of a dictionary
    # the key being the name of the header
    # the value being...well the value we want to pass for that header

r = requests.get(url, headers=headers)
# here we specify that we want to do a get request (.get(), from get, post, push, delete) with the url (with queries embedded in the url) and the headers to pass for this request
print(f"Status code: {r.status_code}")
# APIs return a status code (200s, 400s or 500s). We print that here

# Convert the response object to a dictionary.
response_dict = r.json()
# this converts the response we got into a processable json object (a dictionary)

# Process results.
print(response_dict.keys())
# print all the keys in the response dictionary


"""Processing the content of the response"""

print(f"Total repos found - {response_dict['total_count']}")
print(f"Are the results of this query complete? (meaning was this query able to return its results completely, or are some of them cutoff?) - {not response_dict['incomplete_results']}")
# github has a timeout on their backend for how long an API can run
# for APIs that return a lot of results, like this one, that timeout comes into effect
# under the "incomplete_results" key is stored a boolean value, which states whether the query was successful in returning all expected results completely (were any results cut off?)
# the NOT of basically asks "Are the results complete? True/False"

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned from request - {len(repo_dicts)}")
# a note that github also by default returns a fixed number of repositories for a given query (probably to save bandwidth and computing resources)
# Repositories returned from request - 30 <-- when above print statement is run, this is the result
# If we want more, need to specify in the query


# Examine the first repository.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
# gets the keys stored in the first repository returned and lists them
# in the query params (far above) we instructed github to sort the results based on stars
# meaning this repository is the most starred python repo in github!
for key in sorted(repo_dict.keys()):
    # sorts the list of keys in the first repository
    print(key)
    # prints each key one by one


"""Examining information (keys) provided in a single repository"""

print("\nSelected information about first repository:")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}") # number of stars on this repo
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")
# uses the keys provided by github to extract various information from the first repository
# keys appear to be fairly self explanatory...


"""Print out a brief summary with a few important keys for each of the returned repositories"""

for indiv_repo in repo_dicts:
    print(f"\nName: {indiv_repo['name']}")
    print(f"Owner: {indiv_repo['owner']['login']}")
    print(f"Stars: {indiv_repo['stargazers_count']}")
    print(f"Repository: {indiv_repo['html_url']}")
    print(f"Description: {indiv_repo['description']}")