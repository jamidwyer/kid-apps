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
subreddit = reddit.subreddit('kansas city')
for submission in subreddit.hot(limit=1000):
    #print(submission.title)

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Do a case insensitive search
        if re.search("yoder", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.reply("James Cargas is running against John Culberson. \n\n Campaign website: http://www.jamescargas.com/on-the-issues/ \n\n Register to vote: http://www.votetexas.gov/register-to-vote/ \n\n Donate: https://secure.actblue.com/contribute/page/james-cargas-1 \n\n Facebook: https://www.facebook.com/Cargas7/ \n\n Twitter: https://twitter.com/Cargas7 \n\n Cargas supports renewable energy, science, universal pre-K, public schools, affordable college, LGBTQ equality, background checks on every gun sale, and the Voting Rights Act. \n\n\n ^(I'm a bot and I'm learning. Constructive feedback welcome! It's a lot of work to add all this info, but if you prefer a different candidate, let me know what you like about them, and I'll add them.)")
            print("Bot replying to : ", submission.title)

            # Store the current id into our list
            posts_replied_to.append(submission.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
