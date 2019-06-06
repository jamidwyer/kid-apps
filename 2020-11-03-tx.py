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

local_subs = open("texas.dat", "r")
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
            terms = ['scheme to rig the 2020 census', 'texas democrat', 'texas primary', 'voter Suppression Is the Expressed Policy', 'el paso rally', 'Republicans Plan to Rig Elections for a Decade', 'Beto pays his bills on time', 'citizenship question to the Census', 'plans to rig elections for white Republicans', 'texas judge', 'running with beto', 'botched voter purge', 'a resignation in texas', 'gop in texas', 'republicans hate governing', 'chip roy', 'Trump falls short on infrastructure', 'Campaign Is Showing Solidarity with Striking Workers Like', 'pipeline in texas', 'san antonio prosecutor', 'migrant boy who died in custody', 'muhlaysia booker', 'As president, I will sign into law a new Voting Rights Act', 'dallas campaign', 'nerds out and the crowds go crazy', 'tx-sen', 'rep. al green', 'lt. gov. patrick', 'cornyn', 'texas law', 'fastest-warming cities', 'Eleven-year-old ordered deported without her family', 'demolished for border wall', 'texas capitol', 'beto will be at texas', 'wind power campaign in texas', 'bridge where refugees and asylum', 'turnout in Dallas', 'Bexar County, Texas police']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Texas 2020 Election \n\n"
            "[Registration Deadline](http://www.votetexas.gov/register-to-vote/): October 4, 2020 \n\n"
            "[General Election](https://teamrv-mvp.sos.texas.gov/MVP/mvp.do): November 3, 2020 \n\n")
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