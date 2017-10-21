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

local_subs = open("montana.dat", "r")
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
            terms = ['gianforte', 'ganforte', 'Kier, a Democrats', 'Montana Republican\'s mugshot']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://sos.mt.gov/elections/vote/index) by May 7, 2018 \n\n"
           "[Sign up to vote by mail](https://sos.mt.gov/elections/absentee) \n\n\n"

           "[**John Heenan**](http://www.heenanforcongress.com/issues/) is running against Greg Gianforte. \n\n"
            "[Volunteer](http://www.heenanforcongress.com/page/volunteer/) | "
            "[Donate](https://secure.actblue.com/entity/fundraisers/52906) | "
            "[Facebook](https://www.facebook.com/HeenanForCongress/) | "
            "[Twitter](https://twitter.com/JohnForMontana) \n\n"
            "Heenan supports Medicare for all, renewable energy, campaign finance reform, and protecting Social Security. \n\n\n"

            "[**Grant Kier**](https://kierforcongress.com/) is running against Greg Gianforte. \n\n"
            "[Volunteer](https://docs.google.com/forms/d/e/1FAIpQLSdYS_RIcn4QekQpZT1n4vY-oQ347RL5XYSSY_7r8oAZt5QC8w/viewform) | "
            "[Donate](https://secure.actblue.com/donate/kier4mt) | "
            "[Facebook](https://www.facebook.com/kierforcongress/) | "
            "[Twitter](https://twitter.com/kierforcongress) \n\n"
            "Kier supports universal health care. \n\n\n"

            "Primary Election: June 5, 2018 | General Election: November 6, 2018 \n\n"

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