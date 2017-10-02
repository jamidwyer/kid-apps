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

local_subs = open("southcarolina.dat", "r")
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
            terms = ['henderson myers', 'michael fowler', 'harold mitchell']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; VOTE September 26, 2017 &#9733;&#9733;&#9733;](https://www.scvotes.org/south-carolina-voting-information-page) \n\n"
            "[**Rosalyn Henderson Myers**](http://www.karilernerfornewhampshire.com/) is running to represent District Rockingham 4 in the New Hampshire House of Representatives. \n\n"
            "[Facebook](https://www.facebook.com/HendersonMyersforSCHouse31/) | "
            "[Volunteer](http://www.karilernerfornewhampshire.com/GetInvolved.aspx) | "
            "[Donate](https://secure.actblue.com/donate/FriendsOfKariLerner) \n\n"

            "[Map of New Hampshire State House District Rockingham County No. 4](https://statisticalatlas.com/state-lower-legislative-district/New-Hampshire/Rockingham-County-No-4-District/Overview) \n\n"

        "^(I'm a bot and I'm learning. Let me know how I can do better.)")
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