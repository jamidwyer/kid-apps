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
            terms = ['you believe tulsi', 'SC refused to give Biden', '40 years of Republican tax cuts failed', 'fight with Senate Republicans is bizarre', 'lindsay graham', 'in support from black voters', 'South Carolina city kills residential solar', 'whistleblower as impeachment inquiry deepens', 'president said his White House is trying to uncover it', 'Warren Courts African American Voters', 'Hours That Sealed Trump', 'storm thurmond', 's the one rigging them', 'canceling gop primaries', 'paid staff in south carolina', 'Sanford says he is launching primary', 'cancelling gop primaries', 'union President James Sanderson', 'denali stuckey', 'library in s. carolina', 'sc-04', 'scdp', 'working with segregationist', 'at least there was some civility', ' sc 2020', ' sc poll', 'remarks on segregation senators', ' sc 2020', 'south carolina democrat', 'equal rights amendment', '#scdem', 'south carolina campaign', ' sc campaign', 'denmarkwatercri', 'campaign team in south carolina', 'stand with south carolina teachers', 'teachers marching down bicentennial plaza', 'leningradlindsey', 'lindseygraham', ' If Migrants Kept In Facilities ', 'lindsey fucking graham', 'sc teacher rally', 'lindsey graham', 'first primary in the south', 'south carolina support', 'bernieinsc', 'supporters in greenville', 'charleston church massacre', 's.c. congress', 'south carolina vote', 'kinder-guardians', 'henrymcmaster', 'charleston church shooting', 's.c. governor', 'southcarolinapolitics', 'sc governor', 'governor in sc', ' SC Democrat', 'south carolina general election', 'south carolina senate', 'sc house votes', 'sc legislat', 'dylann roof', 'SC needs gerrymandering', 'South Carolina party primaries', 'phil noble', 'mal hyman', 'gowdy', 'rep. joe wilson', 'jeff duncan', 'archie parnell', 'henry mcmaster', 'kevin bryant', 'south carolina governor', 'south carolina republican', 'Catherine Templeton', 'Republicans in South Carolina']
            for term in terms:
                 search(term, submission)

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("South Carolina 2020 Election \n\n"
            "[Primary Registration Deadline](https://info.scvotes.sc.gov/eng/ovr/start.aspx): January 30, 2020 \n\n"
            "[Primary Election](https://info.scvotes.sc.gov/eng/voterinquiry/VoterInformationRequest.aspx?PageMode=VoterInfo): February 29, 2020 \n\n"
            "[General Election](https://info.scvotes.sc.gov/eng/voterinquiry/VoterInformationRequest.aspx?PageMode=VoterInfo): November 3, 2020 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write our post id to the tracking file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()