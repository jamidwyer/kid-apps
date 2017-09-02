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
            terms = ['warren love', 'Missouri State House District 125', 'Missouri rep posts hope that vandal is hanged', 'hung from a tall tree', 'Missouri representative appears to call for lynching', 'Republican calls for vandals of Confederate monument to be lynched', 'advocating \'lynching\' of Confederate statue vandal', 'Threaten Lynching']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register to Vote &#9733;&#9733;&#9733;](https://www.sos.mo.gov/elections/goVoteMissouri/register) \n\n"
            "Warren Love is currently unopposed in 2018. Know someone who should [run](https://www.runforoffice.org/elected_offices/34558-state-representative-mo-125/interest_form)? \n\n"

            "Map of [Missouri State House District 125](https://statisticalatlas.com/state-lower-legislative-district/Missouri/District-125/Overview) \n\n"

            "^(I'm a bot and I'm learning. Let me know how I can do better.)")
        submission.reply(text)
        print("Bot replying to : ", submission.title)

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