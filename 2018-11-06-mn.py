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

local_subs = open("minnesota.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Minnesota 2018 Election \n\n"
            "[General Election Registration Deadline](https://mnvotes.sos.state.mn.us/VoterRegistration/VoterRegistrationMain.aspx): November 6, 2018 \n\n"
            "[General Election Date](https://mnvotes.sos.state.mn.us/ABRegistration/ABRegistrationStep1.aspx): November 6, 2018 \n\n")

        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write our post id to the tracking file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['minnesota moms rise up', 'Chapo Trap House for a full hour on AM950', 'mn-02', 'ilhan omar', 'compared gay people to rapists', 'mn dfl', 'minnesota gubernatorial', 'minnesota dfl', 'tim walz', 'and view themselves as victims', 'minnesota congress', 'justin vold', 'tina smith', 'jon applebaum', 'al franken', 'pawleny', 'pawlenty', 'minnesota state lawmaker', 'mary franson', 'keith ellison', 'Billboard in Hampton, MN', 'Spotted in Hampton, Minnesota', 'angie craig', 'MeToo Movement Is Coming to the Ballot Box This Month', 'all-in on defense in Minnesota', 'michele bachmann', 'Poison a Minnesota Wilderness', 'Am I Being Called to Do This Now', 'adam jennings', 'Pro-Trump Republican Rep Just Deleted Her Twitter', 'mary franson', 'Lt. Gov. Tina Smith', 'plans to gerrymander the Electoral College in three states', 'erik paulsen', 'rep. paulsen', 'rep paulsen']
            for term in terms:
                 search(term, submission);

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()