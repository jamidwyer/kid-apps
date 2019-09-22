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

local_subs = open("washington.dat", "r")
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
            terms = ['referendum 88', 'one way to reduce reports of cars hitting things', 'agent provocannot', 'safeguard against homelessness, disability payments', 'who governs seattle', 'seattle now most expensive city', 'moms for seattle', 'praxis in the emerald city', 'brendan kolding', 'Take away the last this homeless person has with our new app', 'poisoning puget sound', 'toxins in the Salish Sea', 'toxics into Puget Sound', 'Progressive Boomers Are Making It Impossible For Cities To Fix The Housing Crisis', 'prime day strike', 'seattle transpride', 'trans pride seattle', '9-an-hour engineers', 'seattle minimum wage', 'the head tax', 's up bootlickers', 'Seattle-area prosecutor', 'Seattle Democratic Socialists of America']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Washington 2019 Election \n\n"
            "[General Registration Deadline](https://weiapplets.sos.wa.gov/MyVote/#/login): October 28, 2019 \n\n"
            "[General Election](https://weiapplets.sos.wa.gov/MyVote/#/login): November 5, 2019 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write our updated list back to the file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()