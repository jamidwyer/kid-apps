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

local_subs = open("southcarolina.dat", "r")
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
            terms = ['SC law keeps sexual harassment', 'female Democratic lawmakers ask House to investigate Trump', 'Templeton comes out guns blazing', 'mal hyman', 'gowdy', 'Congressional Russia Inquiries as Parties Clash', 'Fear Him', 'Republicans who obsessed over Benghazi', 'The Republican Plan to Use the Steele Dossier to Attack James Comey', 'rep. joe wilson', 'jeff duncan', 'GOP tries to make mass shootings even easier after Vegas massacre', 'Gun Lobby Wants to Deregulate Gun Silencers', 'archie parnell', 'henry mcmaster', 'kevin bryant', 'south carolina governor', 'south carolina a candidate for governor', 'Catherine Templeton', 'Steve Bannon tells Republicans in South Carolina', 'Defunding Clinics, GOP Governor']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("South Carolina 2018 Election \n\n"
            "[Voter Registration Deadline](https://info.scvotes.sc.gov/eng/ovr/start.aspx): May 13, 2018 \n\n"
            "[Primary Election](https://info.scvotes.sc.gov/eng/voterinquiry/VoterInformationRequest.aspx?PageMode=VoterInfo): June 12, 2018 \n\n"
            "[General Election](https://info.scvotes.sc.gov/eng/voterinquiry/VoterInformationRequest.aspx?PageMode=VoterInfo): November 6, 2018 \n\n")
        print("Bot replying to : ", submission.title)
        submission.reply(text)
        # Write our updated list back to the file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()