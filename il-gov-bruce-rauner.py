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
            terms = ['chris kennedy', 'rauner', 'IL gubernatorial', '@govrauner', '^(?!.*bissexual).*biss.*$', 'illinois governor', 'IL\'s next governor ', 'governor of illinois', 'il gov', 'jeanne ives', 'Billions in Illinois bills not sent for payment', 'Welcome to the dysfunction of Illinois government', 'Gubernatorial Forum Sunday', 'High school students to host gubernatorial primary debate', 'rage at Rauner', 'Rauner Vetoes Geolocation Privacy Protection Act', 'unpaid bill backlog hits a record', 'pritzker', 'il governor\'s']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://ova.elections.il.gov/Step0.aspx) by February 20, 2018 \n\n"
            "[Sign up to vote by mail](https://www.elections.il.gov/VotingInformation/VotingByMail.aspx) \n\n\n"

            "[**Daniel Biss**](https://www.danielbiss.com/the-issues) is running to be Governor of Illinois. \n\n"
            "[Facebook](https://www.facebook.com/DanielBiss/) | "
            "[Twitter](https://twitter.com/danielbiss) | "
            "[Volunteer](https://www.danielbiss.com/take-action/) | "
            "[Donate](https://secure.actblue.com/contribute/page/biss1) \n\n"
            "Biss supports universal health care, renewable energy, public schools, living wages, paid family leave, affordable college, equal pay for equal work, campaign finance reform, LGBTQ equality, DACA, the Paris Climate Agreement, and legalizing marijuana. \n\n\n"

            "[**Chris Kennedy**](https://kennedyforillinois.com/) is running to be Governor of Illinois. \n\n"
            "[Reddit](https://www.reddit.com/r/ChrisKennedy) | "
            "[Facebook](https://www.facebook.com/KennedyforIllinois/) | "
            "[Twitter](https://twitter.com/kennedyforIL) | "
            "[Volunteer](https://kennedyforillinois.com/get-involved/) | "
            "[Donate](https://secure.actblue.com/donate/kennedy-joy-launch) \n\n"
            "Kennedy supports Medicare for All, public schools, living wages, paid family and sick leave, equal pay for equal work, LGBTQ equality, and DACA. \n\n\n"

            "[**JB Pritzker**](https://www.jbpritzker.com/) is running to be Governor of Illinois. \n\n"
            "[Facebook](https://www.facebook.com/jbpritzker) | "
            "[Twitter](https://twitter.com/jbpritzker) | "
            "[Volunteer](https://www.jbpritzker.com/volunteer/) \n\n"
            "Pritzker supports renewable energy, public schools, universal pre-K, child care assistance, the Paris Climate Agreement, and legalizing marijuana. \n\n\n"

            "Primary Election: March 20, 2018 | General Election: November 6, 2018 \n\n"

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