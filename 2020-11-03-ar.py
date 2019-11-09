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

local_subs = open("arkansas.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)


# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=100):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['arkansas veterans', 'entry-level workers at Walmart', 'Political Shift in Arkansas', 'Editor of the Arkansas Times', 'gun show in arkansas', 'rally in little rock', 'rep. garry smith', 'worker advocates are coming to walmart', 'sen. rapert', 'arkansas republican', 'James M. Hinds', 'french hill', 'ar-02', 'ar-2', 'rep. hill', 'rep hill', 'representative hill', 'congressman hill']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Arkansas 2020 Election \n\n"
            "[Register to Vote](https://www.sos.arkansas.gov/elections/voter-information/voter-registration-information/request-for-a-voter-registration-application) \n\n"
            "[Presidential Preference Primary Election](https://www.voterview.ar-nova.org/VoterView/Home.do): March 3, 2020 \n\n"
            "[Primary Election](https://www.voterview.ar-nova.org/VoterView/Home.do): March 31, 2020 \n\n"
            "[General Election](https://www.voterview.ar-nova.org/VoterView/Home.do): November 3, 2020 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Store the current id into our list
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()