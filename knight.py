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
subreddit = reddit.subreddit('california_politics')
for submission in subreddit.hot(limit=500):
    #print(submission.title)

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Do a case insensitive search
        if re.search("steve knight", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.reply("Katie Hill is running against Steve Knight. \n\n Campaign site: http://www.katiehillforcongress.com/ \n\n Register to vote: http://registertovote.ca.gov/ \n\n Donate: https://secure.actblue.com/contribute/page/katie-hill-for-congress-1 \n\n Reddit AMA: https://www.reddit.com/r/SandersForPresident/comments/6kie1a/katie_hill_for_congress_ama/ \n\n Facebook: https://www.facebook.com/KatieHillforCongress/ \n\n YouTube: https://www.youtube.com/channel/UCPywtKt4VZZgj4P1hVNvizAA \n\n Hill supports single-payer health care, renewable energy, living wages, campaign finance reform, net neutrality, and affordable higher education.\n\n I'm a bot and I'm learning. Let me know if I can do better.")
            print("Bot replying to : ", submission.title)

            # Store the current id into our list
            posts_replied_to.append(submission.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
