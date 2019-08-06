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

local_subs = open("ohio.dat", "r")
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
            terms = ['ohio republican', 'trump back in cincinnati', 'ohio legaliz', 'ohio just passed', 'ohio farmer and i voted', 'ohio, lawmaker', 'les wexner', 'Remember when conservatives believed no one was above the law', 'medical board of ohio', 'householder', 'Transit for Five Corridors', 'ohio build a new economy', 'lee wexner', 'trump in ohio', 'ohio house speaker', 'ohio special election', 'oh12', 'ohio dems', 'balderson', 'oh-1', 'jim_jordan', 'stormy daniels\' arrest', 'arrest of stormy daniels', 'balderson race', 'stormy daniels arrested', 'black boy mowing lawn', 'ohio bill', 'dewine', 'ohio\'s voter purge', 'ohiogovernment', 'ohio legislat', 'take back ohio', 'rachel crooks', 'cincinnati rally', 'melissa ackison', 'oh 73', 'rick perales', 'kim mccarthy', 'running for office in ohio', 'Ismail Mohamed', 'erin neace', 'Ohio House district 65', 'ohio lawmaker', 'ohio gubernatorial', 'aftab pureval', 'ohio senate passes bill', 'sherrod brown', 'pillich', 'husted v.', 'jon husted', 'robert barr', 'kucinich', 'Ohio Attorney General', 'Ohio purge of voter rolls', 'ohio senate frontrunner', 'ohio senate candidate', 'jay goyal', 'Ohio congressional candidates', 'rick neal', 'Ohio House and Senate', 'stivers latest', 'Ohio\'s 16th District', 'Ohio ballot', 'Marijuana in Ohio', 'jimmy gould', 'cordray', 'stivers', 'mike turner', 'bob gibbs', 'jim jordan', 'renacci', 'dave joyce', 'Ohio politic', '2018 elections in Ohio', 'representative latta', 'Ohio members of Congress', 'Representative Bill Johnson', 'bill o\'neill', 'steve chabot', 'rep. chabot', 'rep chabot', 'representative chabot', 'congressman chabot', 'oh-01', 'ken harbaugh', 'josh mandel', 'kasich', 'ohio gov', 'oh gov', 'oh governor\'s', 'jerry springer', 'Mary Taylor']
            for term in terms:
                search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Ohio 2020 Election \n\n"
            "[Register to Vote](https://olvr.sos.state.oh.us/IdentificationInformationhttps://olvr.sos.state.oh.us/) \n\n"
            "[General Election](https://www.sos.state.oh.us/elections/voters/absentee-voting/#byMail): November 3, 2020 \n\n")
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
