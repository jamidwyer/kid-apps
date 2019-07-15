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

local_subs = open("virginia.dat", "r")
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
            terms = ['pregnant woman is shot right after failed gun debate', 'virginia, republican', 'colonial williamsburg', 'virginia would be one of the poorest states', 'charlottesville car attack', 'va hd-66', 'vahousedems', 'flipvablue', 'big red boy', '\"oink oink\" to a cop', '^(?!.*west virginia attorney general).*virginia attorney general.*$', 'senator amanda chase', 'equal rights amendment', 'platform for legalizing child porn', 'smother gun control', 'votes and laws, not thoughts and prayers', '^(?!.*west virginia gop).*virginia gop.*$', 'virginia house of delegates', 'crying nazi','election in virginia', 'legalize virginia', 'party of white supremacy', 'marijuana in virginia', '^(?!.*west virginia gop).*virginia gop.*$', 'heather heyer', 'danica roem', 'unite the right', 'jason kessler', '^(?!.*west virginia congressional candidate).*virginia congressional candidate.*$', 'Congressional Candidate In Virginia', '^(?!.*west virginia senat).*virginia senat.*$', 'virginiapolitics', 'errymandering in virginia', 'Va. House', 'Virginia Congressional Election']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        # No early voting
        text = ("Virginia 2019 Election \n\n"
            "[General Election Registration Deadline](https://vote.elections.virginia.gov/Registration/Eligibility): October 15, 2019 \n\n"
            "[General Election](https://vote.elections.virginia.gov/VoterInformation): November 5, 2019 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write our updated list back to the file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()