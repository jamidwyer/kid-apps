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

local_subs = open("kansas.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['kansas hits hemp farmers', 'rural hospital closures', 'republicans will never say that racism is', 'when schools need more funding', '77M more in taxes in May', 'kansas counties eligible for disaster', 'ksvotes', 'wichita police chief', 'sharice davids', 'kansas primary', 'deep-red kansas', 'primary in kansas', 'kansas with sanders', 'kansas rally', 'Harley-Davidson shutdown', 'jamesthompsonks', 'candidate in Kansas', 'kansas is one of the worst', 'vermin supreme', 'svaty', 'state representative in kansas', 'kansas senate', 'kansas house', 'kansas statehouse', 'andrew finch', 'kansas republican', 'kansas gop', 'ks03', 'gay Kansas rep', 'kansas state house', 'ksleg', 'Kansas Attorney General', 'ks legislat', 'brent welder', 'Kansas Legislat', 'steve alford', 'Kansas lawmaker', 'voter fraud commission', 'voter-fraud commission', 'election fraud commission', 'kelly rippel', 'ks-sen', 'Kansas Congressional Delegation', 'Steve Bannon a subpoena', 'kansas budget crisis', 'elections in Kansas', 'yoder', 'ks-3', 'ks-03', 'chris haulmark', 'ks-2', 'ks-02', 'jenkins, lynn', 'congressman jenkins', 'lynn jenkins', 'rep jenkins', 'steve fitzgerald', 'ks-4', 'ks-04', 'Kansas\' 4th Congressional District', 'kansas 4th congressional district', 'congressman estes', 'ron estes', 'rep estes', 'kansas veteran james thompson', 'brownback', 'kobach', 'colyer', '^(?!.*arkansas governor).*kansas governor.*$', 'carl brewer', 'Trump voter fraud panel', 'trump voting commission', 'Kansas economy', 'Trump Election Fraud Panel', 'Kansas tax cut', 'governor in kansas', 'leader jim ward', 'Trump Voter Fraud Probe', 'election integrity commission', 'Trump\'s voter-fraud panel', 'Trump\'s election commission co-chair', '\'election integrity\' panel', 'Trump voting panel']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Kansas 2020 Election \n\n"
            "[Register to Vote](https://www.kdor.ks.gov/Apps/VoterReg/secure/default.aspx) \n\n"
            "[Primary Election](https://myvoteinfo.voteks.org/VoterView/PollingPlaceSearch.do): August 4, 2020 \n\n"
            "[General Election](https://myvoteinfo.voteks.org/VoterView/PollingPlaceSearch.do): November 3, 2020 \n\n")
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