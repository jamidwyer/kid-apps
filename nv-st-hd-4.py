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

local_subs = open("nevada.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=100):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['Richard McArthur', 'tony smith', 'tony smith', 'fighting at the State level to protect our online privacy', '250 in my campaign for NV Assembly', 'Candidate for Local Office in Nevada Fights Big Money by Voluntarily Refusing Any Donation', 'Democratic Candidate for NV Assembly is Refusing Any Donation Over', 'Why Am I Capping Donations to My Campaign']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://nvsos.gov/sosvoterservices/Registration/step1.aspx) \n\n"
        "[**Tony T. Smith**](https://tonytfornv.com/honestdeal/) is running to represent Nevada State Assembly District 4. \n\n "
        "[Donate](https://secure.squarespace.com/commerce/donate?donatePageId=597c5d1af14aa1fbe7888103) | "
        "[Facebook](https://www.facebook.com/TonyTforNV) | "
        "[Twitter](https://twitter.com/TonyT4NV) \n\n "
        "Smith supports renewable energy, a living wage, college affordability, campaign finance reform, and net neutrality. \n\n\n"

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