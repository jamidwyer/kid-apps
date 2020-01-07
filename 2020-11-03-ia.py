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

local_subs = open("iowa.dat", "r")
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
            terms = [
                'kim reynolds', \
                'gov. reynolds', \
                'joni ernst', \
                'ia-01', \
                'abby finkenauer', \
                'ia-03', \
                'Iowa\'s 3rd District race', \
                'ia-4', 'ia-04', \
                'congressman king', \
                'rod blum', 'rep. blum', 'congressman blum', 'rep blum', 'steve king', 'representative king', \
                'Alasandro', \
                'first in iowa', \
                'sanders overtakes joe', \
                'biden will lose', 'iowa passes law', \
                'days til iowa', \
                'castro supporters', \
                'warren thanks castro', \
                'poll in iowa', \
                'republican as vice president', \
                'fought for working families my entire life', \
                'Woman Ran Over Girl Because She Was', \
                'asking, why this moment', \
                'insurance deductible', \
                'narcissist bernie', \
                'becoming the frontrunner', \
                'the 2020 election', \
                'warren for president', \
                'wealth tax', 'electability', 'trump supporters from iowa', 'democrats have shifted left', \
                'essay praising bernie sanders', 'Sanders lead Democrat', \
                'leading in iowa', \
                'endorsements in iowa', 'IBEW Local 1634', 'farmers endorse sanders', 'primary vot', 'iowa capitol', \
                'democratic party centrism', 'not accept a middle ground approach', 'take on the corporate elite', \
                'joe biten', 'bags and bags of money', '^(?!.*delectable).*electable.*$', 'sanders for iowa', \
                'bernie in iowa', 'bernie surge', 'sanders tied', 'new emerson poll', 'tied with biden', \
                'canvassing in iowa', 'tax the rich', \
                'defeat donald trump', 'emerson national poll', 'latest emerson poll', 'stacey walker endorse', \
                'iowa endors', 'iowa field director', 'voters in iowa', 'flip the senate', 'event in des moine', \
                '1,000 times more than his workers', 'Iowa teacher on leave after \'sniper rifle\' comment', \
                'feelthebern', \
                'warren accuses trump', \
                'quinnipiac national poll', 'iowa steak fry', \
                'iowa contender', 'polk county steak fry', 'huge iowa crowd', 'vote blue, no matter who', \
                'iowa senat', 'iowa field director', \
                'Trade War Disaster', 'iowa labor day', 'presidential playbook', 'Iowa State College Dem Straw Poll', \
                'battleground iowa', 'iowa state fair kernel poll', 'warren on the register', 'bernie beats trump', \
                'community leaders in iowa', 'yang in iowa', 'iowa4yang', 'giving up on iowa', \
                'bernie sanders dominates', \
                'deep-red sioux county', 'iowa vote', 'reddest corner of iowa', 'iowa ground game', \
                'donations from billionaires', 'iowa city campaign', 'donations from iowa', 'iowa union', \
                'caucusing for ', \
                'marching in cedar rapids', 'workers in cedar rapids', 'iacaucus', 'tied in iowa', 'rising in iowa', \
                'iowa trump vote', 'iowa dems', 'iowa legislat', 'rally in iowa', 'sioux city rally', 'virtual caucus', \
                'sanders in iowa', 'giant democratic primary field', 'corporate middlemen', 'is that really so radical', \
                'iowa kickoff speech', 'rwdsu in cedar rapids', 'iowa caucus', 'iowa democrat', 'climate crisis summit', \
                'iowa\'s medicaid', 'zach wahls', 'iowa abortion ban', 'iowa race as house candidate', 'peteforiowa', \
                'iowa is feeling the bern', 'new office in iowa', 'Bernie Sanders returns to Iowa', \
                'Iowa representatives', 'NRA president\'s Iowa business', \
                'Factory Farming in Iowa', \
                'national democratic primary', \
                'dead heat in iowa', \
                'austin frerick', \
                'Iowa Lawmakers', \
                'nate boulton', \
                'rob sand', 'Iowa Poll', \
                'Iowa went big for Trump', 'david young', 'anti-Iowa positions', 'Iowa Candidate', \
                'Running For Congress In Iowa', 'Trump sinks in Iowa', \
                'julian castro drops out', \
                'Trump Hate Iowa'
            ]
            for term in terms:
                 search(term, submission)

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Iowa 2020 Election \n\n"
            "[Caucus Voter Pre-Registration Deadline](https://mymvd.iowadot.gov/Account/Login?ReturnUrl=%2fVoterRegistration): January 24, 2020 \n\n"
            "[Caucus](https://www.aclu-ia.org/en/how-find-your-caucus-site): February 3, 2020 \n\n"
            "[General Election](https://sos.iowa.gov/elections/voterinformation/index.html): November 3, 2020 \n\n")
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
