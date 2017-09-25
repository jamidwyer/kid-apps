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
            terms = ['sara walsh', 'historically red 50th', 'Missouri State House District 50', 'missouri special election', 'august 8 special election', 'august 8th special election']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; VOTE &#9733;&#9733;&#9733;](https://s1.sos.mo.gov/elections/goVoteMissouri/howtovote) \n\n"
            "[**Michela Skelton**](http://www.michelaskelton.com/) is running to represent Missouri State House District 50. \n\n"
            "[Donate](https://secure.actblue.com/contribute/page/michelaskelton) | "
            "[Facebook](https://www.facebook.com/skeltonfor50/) | "
            "[Twitter](https://twitter.com/SkeltonFor50) \n\n"

            "Skelton supports living wages and paid family leave. \n\n\n"

            "Map of [Missouri State House District 50](https://ballotpedia.org/File:MO_HD_050.JPG) \n\n"

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