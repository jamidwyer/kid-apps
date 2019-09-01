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
            terms = ['iowa labor day', 'presidential playbook', 'Iowa State College Dem Straw Poll', 'battleground iowa', 'contracts from any company that busts unions or offshores', 'We love our national pastime folks', 'iowa cops buy an armored vehicle', 'State Laws That Ban Locally-Owned ISPs', 'iowa state fair kernel poll', 'he spoke to almost no one', 'warren on the register', 'farm subsidies with price supports', 'bernie at the iowa state fair', 'register soapbox', 'community leaders in iowa', 'yang in iowa', 'iowa4yang', 'giving up on iowa', 'bernie sanders dominates', 'Pentagon testing mass surveillance balloons across the U.S.', 'deep-red sioux county', 'iowa vote', 'reddest corner of iowa', 'iowa ground game', 'sanders laughs about small town life', 'iowa city campaign', 'donations from iowa', 'trump trails biden, warren, and sanders', 'beto in independence, iowa', 'iowa union', 'beto for ia', 'climate change by mobilizing an unlikely team', 'caucusing for ', 'polling in top six', 's Theory of the Case', 'joni ernst', 'marching in cedar rapids', 'bernie at capital city pride', 'workers in cedar rapids', 'iacaucus', 'Campaign Is Showing Solidarity with Striking Workers Like', 'iowa swing back to dem', 'the floor, not the ceiling', 'tied in iowa', 'rising in iowa', 'iowa trump vote', 'cnn to host beto o', 'beto CNN Town Hall 5', 'iowa dems', 'iowa legislat', '2020 buzz fizzles', 'farming, agricultural subsidies, and price controls', 'sioux city rally', 'iowa, nevada, or california', 'virtual caucus', 'we asked democratic activists who they', 'build out their iowa teams', 'viable candidate after Iowa City stop', 'entire town shows up for bernie', 'washing hands and talking to the next future president', 'sanders in iowa', ' 230 showed up for', 'sanders as a gadfly', 'giant democratic primary field', 'rourke returns to iowa', 'corporate middlemen', 'iowa kickoff speech', 'iowa caucus', 'iowa democrat', 'DACA student killed after being deported to Mexico', 'ICE deports Iowa HS student', 'Iowa student killed after being deported to Mexico', 'iowa\'s medicaid', 'zach wahls', 'iowa abortion ban', 'iowa race as house candidate', 'peteforiowa', 'iowa is feeling the bern', 'Burma Refugees Living in Des Moines', 'Bernie Sanders returns to Iowa', 'Iowa representatives', 'NRA president\'s Iowa business', 'ia-03', 'Factory Farming in Iowa', 'kim reynolds', 'Alasandro', 'Iowa\'s 3rd District race', 'austin frerick', 'Iowa Lawmakers', 'nate boulton', 'rob sand', 'Iowa Poll', 'Iowa went big for Trump', 'david young', 'anti-Iowa positions', 'Iowa Candidate', 'Running For Congress In Iowa', 'Trump sinks in Iowa', 'rod blum', 'rep. blum', 'congressman blum', 'rep blum', 'steve king', 'rep. king', 'rep king', 'representative king', 'Trump Hate Iowa', 'congressman king', 'ia-01', 'ia-4', 'ia-04']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Iowa 2020 Election \n\n"
            "[Caucus Voter Registration Deadline](https://mymvd.iowadot.gov/Account/Login?ReturnUrl=%2fVoterRegistration): January 24, 2020 \n\n"
            "Caucus: February 3, 2020 \n\n"
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
