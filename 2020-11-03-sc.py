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
            terms = ['union President James Sanderson', 'sanders host basketball tournament at allen', 'Event in Beaufort, SC', 'denali stuckey', 'Trump criticized the U.S. for years', 'library in s. carolina', 'in the Way of Federal Weed Legalization', 'Rare sea turtles are smashing nesting records', 'sc-04', 'scdp', 'having a moment in south carolina', 'working with segregationist', 'fish fry, columbia, sc', 'at least there was some civility', 'remarks on segregation senators', ' sc 2020', 'south carolina democrat', 'equal rights amendment', '#scdem', 'south carolina campaign', ' sc campaign', 'denmarkwatercri', 'campaign team in south carolina', '700-mile border fence', 'stand with south carolina teachers', 'south carolina to seoul', 'teachers marching down bicentennial plaza', 'leningradlindsey', 'lindseygraham', ' If Migrants Kept In Facilities ', 'lindsey fucking graham', 'sc teacher rally', 'lindsey graham', 'first primary in the south', 'south carolina support', 'bernieinsc', 'supporters in greenville', 'charleston church massacre', 's.c. congress', 'south carolina vote', 'kinder-guardians', 'henrymcmaster', 'charleston church shooting', 's.c. governor', 'southcarolinapolitics', 'Boeing workers in Charleston, South Carolina', 'sc governor', 'benghazi', 'governor in sc', ' SC Democrat', 'South Carolina inmates sue', 'south carolina general election', 'south carolina senate', 'sc house votes', 'sc legislat', 'dylann roof', 'SC needs gerrymandering', 'South Carolina party primaries', 'phil noble', 'mal hyman', 'gowdy', 'rep. joe wilson', 'jeff duncan', 'archie parnell', 'henry mcmaster', 'kevin bryant', 'south carolina governor', 'Catherine Templeton', 'Republicans in South Carolina']
            for term in terms:
                 search(term, submission);

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