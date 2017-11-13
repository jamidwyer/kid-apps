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

# Get the top values from our subreddit
subreddit = reddit.subreddit('philadelphia')
for submission in subreddit.hot(limit=50):
    #print(submission.title)

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['ryan costello', 'Democrats back military veterans as candidates']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search("costello", submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Pennsylvania 2018 Election \n\n"
            "[Voter Registration Deadline](https://www.pavoterservices.pa.gov/Pages/VoterRegistrationApplication.aspx): April 16, 2018 \n\n"
            "[Primary Election](https://www.pavoterservices.pa.gov/Pages/PollingPlaceInfo.aspx): May 15, 2018 \n\n"
            "[General Election](https://www.pavoterservices.pa.gov/Pages/PollingPlaceInfo.aspx): November 6, 2018 \n\n")
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