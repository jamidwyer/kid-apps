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

local_subs = open("texas.dat", "r")
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
            terms = ['brian babin', 'rep. babin', 'rep babin', 'representative babin', 'congressman babin', 'Climate Change Denying GOP Congressman Trapped In His Texas Home By Flood Waters']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://www.votetexas.gov/register-to-vote/) \n\n"
        "[**Dayna Steele**](https://daynasteele36.com/) is running against Brian Babin. \n\n"
        "[Donate](https://daynasteele36.givingfuel.com/dayna-steele-campaign) | "
        "[Facebook](https://www.facebook.com/daynasteele) | "
        "[Twitter](https://twitter.com/daynasteele) \n\n"

        "Steele supports single-payer health care.  \n\n"

        "[**Jon Powell**](http://jonpowellforcongress.us/) is running against Brian Babin. \n\n"
        "[Donate](https://secure.actblue.com/contribute/page/jptx36) | "
        "[Facebook](https://www.facebook.com/JonPowellTX36/) | "
        "[Twitter](https://twitter.com/JonPowellTX36) \n\n"

        "Powell supports affordable health care for everyone.  \n\n"

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