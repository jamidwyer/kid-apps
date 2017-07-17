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

# Get the top 500 values from our subreddit
subreddit = reddit.subreddit('indivisibleguide')
for submission in subreddit.hot(limit=2000):
    #print(submission.title)

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Do a case insensitive search
        if re.search("rohrabacher", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.reply("Tony Zarkades is running against Dana Rohrabacher. \n\n Campaign website: https://www.tonyzforcongress.org/on-the-issues \n\n Register to vote: http://registertovote.ca.gov/ \n\n Donate: https://secure.actblue.com/contribute/page/tonyzforcongress \n\n Facebook: https://www.facebook.com/tonyzforcongress/ \n\n Twitter: https://twitter.com/tonyz4congress \n\n Zarkades supports single-payer health care, living wages, paid family leave, Social Security, Medicare, affordable college, equal pay for equal work, renewable energy, common-sense gun control, funding science and the EPA, DACA, and a path to citizenship for hard-working, law-abiding people, while deporting criminals. \n\n ^(I'm a bot and I'm learning. Let me know if I can do better. It's a lot of work to add all this info, but if you prefer a different candidate, let me know, and I'll add them.)")
            print("Bot replying to : ", submission.title)

            # Store the current id into our list
            posts_replied_to.append(submission.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
