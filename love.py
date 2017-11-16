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

local_subs = open("utah.dat", "r")
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
            terms = ['mia love', 'mia b. love', 'rep love', 'rep. love', 'representative love', 'congresswoman love', 'ut-04', 'ut-4', 'Love used campaign funds for Disney World', 'Love wants to morph a Forest Service building', 'love\'s constituent meeting format', 'constituents say they were left off her invite list', 'Love has a new chief of staff', 'Love\'s not on board.', 'better way to talk with constituents']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Utah 2018 Election \n\n"
            "[Primary Voter Registration Deadline](https://secure.utah.gov/voterreg/index.html): June 19, 2018 \n\n"
            "[Primary Election](https://elections.utah.gov/Media/Default/Documents/Elections%20Resources/Absentee%20Ballot%20Application.pdf): June 26, 2018 \n\n"
            "[General Election](https://elections.utah.gov/Media/Default/Documents/Elections%20Resources/Absentee%20Ballot%20Application.pdf): November 6, 2018 \n\n")
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