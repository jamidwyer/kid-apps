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

local_subs = open("arizona.dat", "r")
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
            terms = ['ducey', 'arizona governor', 'takes on McCain over health care vote', 'Trump attacks McCain and other Republicans over healthcare failure', 'permission to vote for Obamacare repeal', 'Murkowski is in the health-care spotlight. Again.', 'Obamacare Is Suddenly in Grave Danger', 'Momentum builds for Obamacare repeal', 'Revived Health Care Effort Is Just as Much of an Uphill Climb as the Last One', 'Scheme Fulfills an Old Conservative Dream', 'Arpaio Pardon Help Swing Arizona', 'az. gubernatorial race', 'arizona\'s race for governor', 'arizona gubernatorial', 'arizona\'s republican governor', 'so divisive that not even the GOP governor is showing up']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://servicearizona.com/webapp/evoter/register?execution=e1s2) by July 30, 2018 \n\n"
            "[Sign up to vote by mail](https://www.vote.org/absentee-ballot/) \n\n\n"

            "[**David Garcia**](http://dg4az.com/) is running to be Arizona's Governor. \n\n"
            "[Donate](https://act.myngp.com/Forms/-4374401513548677120) | "
            "[Facebook](https://act.myngp.com/Forms/-4374401513548677120) | "
            "[Twitter](https://twitter.com/dg4az) \n\n"
            "Garcia supports public schools. \n\n\n"

            "Primary Election: August 28, 2018 | General Election: November 6, 2018 \n\n"
            "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people.)")

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