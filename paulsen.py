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

# Get the top 100 values from our subreddit
subreddit = reddit.subreddit('minnesota')
for submission in subreddit.hot(limit=100):
    #print(submission.title)

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Do a case insensitive search
        if re.search("erik paulsen", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.reply("Dean Phillips is running against Erik Paulsen. \n\n Campaign site: https://www.phillipsforcongress.org/ \n\n Register to vote: https://mnvotes.sos.state.mn.us/VoterRegistration/VoterRegistrationMain.aspx \n\n Donate: https://secure.actblue.com/contribute/page/deanforcongress?refcode=web_invest&sc=web_invest \n\n Facebook: https://www.facebook.com/deanphillipsforcongress \n\n Twitter: https://twitter.com/deanbphillips \n\n He supports net neutrality.\n\n I'm a bot and I'm learning. Let me know if I can do better.")
            print("Bot replying to : ", submission.title)

            # Store the current id into our list
            posts_replied_to.append(submission.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
