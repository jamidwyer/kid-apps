# coding: utf-8
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

local_subs = open("kentucky.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['states to force Medicaid recipients to work', 'Any Regulation Is Bad, Even If It Protects Sick Old People', 'You Can See The Anger In Her Face', 'Battling Over Who Even Gets to Go to the Polls', 'kim davis', 'andy barr', 'rep. barr', 'rep barr', 'representative barr', 'congressman barr', 'kentucky\'s 6th congressional district', 'ky-6', 'ky-06', 'Kentucky\’s 6th Congressional District', 'Canceling healthcare subsidies will hurt Americans in pro-Trump states the most', 'Fighter pilot candidate in Kentucky', 'Democrats Turn To Veterans For 2018 Races']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Kentucky 2018 Election \n\n"
            "[Primary Election Registration Deadline](https://vrsws.sos.ky.gov/ovrweb/): April 23, 2018 \n\n"
            "[Primary Election](https://vrsws.sos.ky.gov/VIC/): May 22, 2018 \n\n"
            "[General Election Registration Deadline](https://vrsws.sos.ky.gov/ovrweb/): October 9, 2018 \n\n"
            "[General Election](https://vrsws.sos.ky.gov/VIC/): November 6, 2018 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write the post id back to the file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()
