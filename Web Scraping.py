import requests
from bs4 import BeautifulSoup
# Terminal: pip install beautifulsoup4
# TODO: download the page using requests
so_page = requests.get('https://stackoverflow.com/questions/tagged/python?tab=Unanswered')
soup = BeautifulSoup(so_page.content, 'html.parser')
# StackOverflow website, top 45 unanswered questions with python tags
# HTML Content:
''' <div class='s-post-summary--content">
        <h3 <a> [Question title text] </a> </h3>
        <div> [Question text excerpt] </div>
        <div class="s-user-card--info">
            <div> <a> [User account] </a> </div>
        </div>
    </div> '''
# TODO: using BeautifulSoup, extract the following from the list of questions: title, user, text excerpt
post_list = soup.find_all('div', 's-post-summary--content')
count = 1 
# A variable 'count' is 1, then within this loop, count increases every time it performs... stopping at 45 
for post in post_list:
    title = post.h3.a.text.strip()
    excerpt = post.div.text.strip()
    user_card = post.find('div', 's-user-card--info')
    try:
        user = user_card.div.a.text.strip()
    except AttributeError:
        user = user_card.div.text.strip()
    print('Title: {} \nUser: ({})\nExcerpt: {}'.format(title, user, excerpt)) 
    if count == 45:
        break
    count += 1 
# NOTE: you might need to get page 2 and page 3, to get to 45 (do lots of testing)

# TODO: print all 45 questions in the format "{title} ({user}):\n{excerpt}"
