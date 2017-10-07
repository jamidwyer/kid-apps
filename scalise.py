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

local_subs = open("georgia.dat", "r")
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
            terms = ['buddy carter', 'Republican congressman from the state wants to withhold federal dollars to test these kits', 'withhold federal funding to test rape kits', '@repbuddycarter', 'Senate opponents of Trumpcare should be beaten', 'another round of anger over health care', 'fantasizes about beating up a female Republican Senator', 'snatch a knot']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://www.mvp.sos.ga.gov/MVP/mvp.do) \n\n"
            "[**Lisa Ring**](http://www.lisaringforcongress.com/) is running against Buddy Carter. \n\n"
            "[Donate](https://secure.actblue.com/donate/lisaringforcongress) | "
            "[Facebook](https://www.facebook.com/LisaRingGA/) | "
            "[Twitter](https://twitter.com/lisaringga) \n\n"
            "Ring supports Medicare for all and living wages. \n\n\n"

            "[**Steve Jarvis**](http://www.electstevejarvis.com/) is running against Buddy Carter. \n\n"
            "[Donate](http://www.electstevejarvis.com/make-a-donation/) | "
            "[Facebook](https://www.facebook.com/WinIn2018/) | "
            "[Twitter](https://twitter.com/ElectSteve2018) \n\n"
            "Jarvis supports campaign finance reform, protecting Social Security and Medicare, and equal pay for equal work. \n\n\n"

            "Map of Georgia District 1: https://www.govtrack.us/congress/members/GA/1 \n\n"

            "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people instead of billionaire political donors.)")

        print("Bot replying to : ", submission.title)
        submission.reply(text)

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