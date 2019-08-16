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

local_subs = open("wisconsin.dat", "r")
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
            terms = ['Trump underwater in... - Wisconsin', 'wisconsin poll', 'Trump Won Because Of Lower Democratic Turnout', 'bernie map', 'MI, MN and WI', 'DNC Army That Could Soon Descend', 'lulac', 'bern in milwaukee', 'unflattering numbers leak', 'Ten cities say Trump owes them money', 'wisconsin is flying the rainbow', 'democratic party of wisconsin', 'terrill thomas', 'Trump Would Have Lost Election Without Russian Help', 'wisconsin democrat', 'loss in wisconsin', 'now hit 10,000', 'permanent minority rule', 'wisconsin conservative', 'leah vukmir', 'candidate won wisconsin', 'wisconsin senat', 'caleb frostman', 'Milwaukee County ballot', 'Foxconn', 'rebecca dallet', 'Wisconsin Supreme Court', 'Dane County Supervisor', 'judge rejects walker', 'wisconsin green party', 'wisconsin gop', 'Milwaukee vot', 'wisconsin legislat', 'Bryce rally', 'kyle frenette', 'Commissioner Seat in Wisconsin', 'wi-07', 'Milwaukee jail', 'Milwaukee Sheriff', 'Wisconsin Dairy Farms declar', 'Wisconsin Elect', 'Wisconsin Republican', 'tammy baldwin', 'matt flynn', 'Sensenbrenner', 'randy bryce', 'scott walker', 'governor walker', 'wisconsin governor', 'wi governor\'s', 'Wisconsin gubernatorial candidate', 'Wisconsin\'s partisan gerrymander', 'Voters in Wisconsin', 'Wisconsin Strict ID Law', 'paul ryan', 'rep. ryan', 'congressman ryan', 'rep ryan', 'speaker ryan', '@speakerryan', 'IronStache', 'Republican tax scam', 'Wisconsin\'s First Congressional District', 'brad schimel']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Wisconsin 2020 Election \n\n"
            "[Register to Vote](https://myvote.wi.gov/en-us/RegisterToVote) \n\n"
            "[Presidential Preference Primary Election](https://myvote.wi.gov/en-us/FindMyPollingPlace): April 7, 2020 \n\n"
            "[General Election](https://myvote.wi.gov/en-us/FindMyPollingPlace): November 3, 2020 \n\n")
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