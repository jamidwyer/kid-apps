#!/usr/bin/python
import praw
import pdb
import re
import os

# Create the Reddit instance
reddit = praw.Reddit('bot1')

# and login
#reddit.login(REDDIT_USERNAME, REDDIT_PASS)

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

local_subs = open("illinois.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['rauner', 'IL gubernatorial', '@govrauner', 'biss', 'illinois governor', 'IL\'s next governor ', 'governor of illinois', 'il gov', 'Illinois House passes school funding bill on second try', 'il governor\'s']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://ova.elections.il.gov/Step0.aspx) \n\n"
            "[**Ameya Pawar**](https://www.pawar2018.com/issues/) is running to be Governor of Illinois. \n\n"
            "[Donate](https://secure.actblue.com/donate/pawar2018-today) | "
            "[Reddit](https://www.reddit.com/r/Pawar2018) | "
            "[Facebook](https://www.facebook.com/AmeyaPawarIL/) | "
            "[Twitter](https://twitter.com/Ameya_Pawar_IL) \n\n"
            "Pawar supports universal health care, renewable energy, public schools, living wages, paid family leave, paid sick leave, affordable college, campaign finance reform, and LGBTQ equality. \n\n\n"

            "[**Daniel Biss**](https://www.danielbiss.com/the-issues) is running to be Governor of Illinois. \n\n"
            "[Donate](https://secure.actblue.com/contribute/page/biss1) | "
            "[Facebook](https://www.facebook.com/DanielBiss/) | "
            "[Twitter](https://twitter.com/danielbiss) \n\n"
            "Biss supports universal health care, renewable energy, public schools, living wages, paid family leave, affordable college, equal pay for equal work, campaign finance reform, and LGBTQ equality. \n\n\n"

            "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people instead of billionaire political donors.)")

        print("Bot replying to : ", submission.title)

        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Store the current id into our list
        posts_replied_to.append(submission.id)

for sub in subs:
     print(sub)
     searchAndPost(sub);

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

text_file.close()
local_subs.close()