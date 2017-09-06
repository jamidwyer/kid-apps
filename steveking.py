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

local_subs = open("iowa.dat", "r")
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
            terms = ['steve king', 'rep. king', 'rep king', 'representative king', 'After 16 Futile Years', 'Republican suicide', 'congressman king', 'ia-4', 'ia-04']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://mymvd.iowadot.gov/Account/Login?ReturnUrl=%2fVoterRegistration) \n\n"
            "[**Leanne Jacobsen**](https://www.leannjacobsen.com/) is running against Steve King. \n\n"
            "[Donate](https://secure.actblue.com/donate/leann-for-iowa) | "
            "[Facebook](https://www.facebook.com/LeannforIowa) | "
            "[Twitter](https://twitter.com/LeannforIowa) \n\n"
            "Jacobsen supports universal health care, renewable energy, public schools, and protecting Medicare. \n\n\n"

            "[**J.D. Scholten**](http://www.scholten4iowa.com/) is running against Steve King. \n\n"
            "[Donate](http://www.scholten4iowa.com/Contribute) | "
            "[Facebook](https://www.facebook.com/Scholten4Iowa/) | "
            "[Twitter](https://twitter.com/scholten4iowa) \n\n"
            "Scholten supports universal health care. \n\n\n"

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