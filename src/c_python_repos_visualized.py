import requests
import plotly.express as px

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process overall results.
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Process repository information.
repo_dicts = response_dict['items']
# gets the individual repos that the query returned

repo_links, stars, hover_texts = [], [], []
# for storing the links and number of stars each repo has, as well as hover text for each generated bar

for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    # gets the name and the github link for the repository
    
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    # using html to display the repo name and also make it a clickable link (with the anchor, <a tag)
    
    repo_links.append(repo_link)
    # puts this html styled name/link combo into the repo_links list, to be displayed in the graph 
    stars.append(repo_dict['stargazers_count'])
    
    # above appends the names (with links attached) and star values to the arrays above, for visualization below
    
    # Build hover texts.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)
    # will use description and the owner of the repo as the hover text for each bar
    
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)
# plots a bar graph; x axis is name of repo, y axis is number of stars for that repo
# adding title and labels (for x and y axis) as well
# adds hover text as well with "hover_name" field

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
# font sizes for titles and labels

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
# makes the bars in the graph slightly more transparent (via marker_opacity) and makes the marker_color "SteelBlue"

fig.show()
# displays the graph

fig.write_html('bar_graph_stars_per_repo.html')
# saves generated html file