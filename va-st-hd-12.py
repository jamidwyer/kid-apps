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

local_subs = open("virginia.dat", "r")
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
            terms = ['joseph yost', 'chris hurst', 'Virginia House of Delegates seats HD-72, HD-10, HD-12', 'Boyfriend of reporter killed', 'Our Revolution in the Blue Ridge endorses the following candidates', 'push to retake rural Virginia', 'This is a cry for help.']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://vote.elections.virginia.gov/Registration/Eligibility) by Monday, October 16, 2017. \n\n"
            "General Election: November 7, 2017 \n\n"
            "[Find your polling place](http://www.elections.virginia.gov/voter-outreach/where-to-vote.html) \n\n"

            "[**Chris Hurst**](https://www.hurst4delegate.com/the-issues/) is running to represent Virginia State House District 12. \n\n"
            "[Donate](https://secure.actblue.com/contribute/page/chris-hurst-for-delegate-1) | "
            "[Facebook](https://www.facebook.com/ChrisHurstForVirginia/) | "
            "[Twitter](https://twitter.com/ChrisHurstVA) \n\n"

            "Hurst supports renewable energy, public schools, and DACA.  \n\n"

            "[Map of Virginia State House District 12](http://redistricting.dls.virginia.gov/2010/Data%5C2011HouseMaps%5CHB5005%20-%20House%2012.pdf) \n\n"

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