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

local_subs = open("massachusetts.dat", "r")
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
            terms = ['massachusetts unions', 'Reclaim Patriotism and the American Flag', 'boston climate strike', 'boston hospitals face deportation', 'deport sick, dying children', 'DEPORTING KIDS WITH CANCER', 'coverage of his racism', 'Fourth U.S. City Bans Facial Recognition', 'Massachusetts banks, credit unions expand services for marijuana', 'straightprideparade', 'massachusetts public defender', 'heat days by 2050 will not spare Berkshires', 'harvard students about bernie sanders', 'gaining steam on beacon hill', 'boston will protect residents', 'windham campaign', 'alan dornan from somerville', 'A Second U.S. City Has Banned Facial Recognition', 'contempt resolution for barr', 'boston straight pride', '24 Facebook pages spreading anti-muslim vitriol', 'senmarkey', 'gov. of massachusetts', 'boston common to fight for worker', 'MIT for cannabis', 'rachael rollins', 'black people are too stupid to vote for me', 'transgender protections in Massachusetts', 'ma-sen', 'massachusetts marijuana', 'mass. voters', 'Green-Rainbow Party of Massachusetts', 'ma-3', 'bob massie', 'boston march for our lives', 'jim mcgovern', 'marijuana in Massachusetts', 'Cambridge women\'s march', 'Boston PD', 'alexandra chandler']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Massachusetts 2020 Election \n\n"
            "[Primary Election Voter Registration Deadline](https://www.sec.state.ma.us/OVR/Welcome.aspx): February 12, 2020 \n\n"
            "[Primary Election](http://www.sec.state.ma.us/wheredoivotema/bal/MyElectionInfo.aspx): March 3, 2020 \n\n"
            "[General Election](http://www.sec.state.ma.us/wheredoivotema/bal/MyElectionInfo.aspx): November 3, 2020 \n\n")
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