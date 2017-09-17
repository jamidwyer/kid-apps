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

local_subs = open("illinois.dat", "r")
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
            terms = ['mike bost', 'rep. bost', 'congressman bost', 'rep bost', 'representative bost', 'Yelled At In A Ritual By \'Orientals\'']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://ova.elections.il.gov/Step0.aspx) by February 20, 2018 \n\n"
            "[Sign up to vote by mail](https://www.elections.il.gov/VotingInformation/VotingByMail.aspx) \n\n\n"

            "[**Dean Pruitt**](http://www.deanforcongress.org/issues.htm) is running against Mike Bost. \n\n"
            "[Donate](http://www.deanforcongress.org/donate.htm) | "
            "[Facebook](https://www.facebook.com/deanforcongress) | "
            "Pruitt supports universal health care, protecting Social Security and Medicare, the Voting Rights Act, and universal pre-K. \n\n\n"

            "[**Brendan Kelly**](https://brendan4southernil.com/) is running against Mike Bost. \n\n"
            "[Donate](https://secure.actblue.com/donate/kelly-donate) | "
            "[Facebook](https://www.facebook.com/Brendan4SouthernIllinois/) | "
            "[Twitter](https://twitter.com/Kelly4SouthrnIL) \n\n"

            "Primary Election: March 20, 2018 | General Election: November 6, 2018 \n\n"
            "[Map of Illinois District 12](https://www.govtrack.us/congress/members/IL/12) \n\n"

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