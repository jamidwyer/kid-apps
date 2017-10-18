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

local_subs = open("missouri.dat", "r")
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
            terms = ['mccaskill', 'Vulnerable Dem senators', 'recruit huddles with Koch network in New York', 'top 10 Senate races of 2018']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register to Vote &#9733;&#9733;&#9733;](https://www.sos.mo.gov/elections/goVoteMissouri/register) by July 11, 2018 \n\n"
            "[**Claire McCaskill**](http://clairemccaskill.com/) is running to represent Missouri in the United States Senate. \n\n"
            "[Facebook](https://www.facebook.com/clairemccaskill) | "
            "[Twitter](https://twitter.com/clairecmc) | "
            "[Volunteer](http://action.clairemccaskill.com/p/dia/action3/common/public/?action_KEY=10440) | "
            "[Donate](https://secure.actblue.com/contribute/page/mccaskill-web) \n\n "

            "McCaskill supports renewable energy, public schools, affordable college, protecting Social Security and Medicare, equal pay for equal work, campaign finance reform, LGBTQ equality, and the DREAM Act. \n\n\n"

            "Primary Election: August 7, 2018 | General Election: November 6, 2018 \n\n"

            "^(I'm a bot and I'm learning. Let me know how I can do better.)")
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