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
        text = ("Minnesota 2020 Election \n\n"
            "[Presidential Primary Early Voting Begins](https://mnvotes.sos.state.mn.us/ABRegistration/ABRegistrationStep1.aspx): January 17, 2020 \n\n"
            "[Presidential Primary Election Pre-Registration Deadline](https://mnvotes.sos.state.mn.us/VoterRegistration/VoterRegistrationMain.aspx): March 3, 2020 \n\n"
            "[Presidential Primary Election](https://mnvotes.sos.state.mn.us/ABRegistration/ABRegistrationStep1.aspx): March 3, 2020 \n\n"
            "[Primary Election Pre-Registration Deadline](https://mnvotes.sos.state.mn.us/VoterRegistration/VoterRegistrationMain.aspx): July 23, 2020 \n\n"
            "[Primary Election](https://mnvotes.sos.state.mn.us/ABRegistration/ABRegistrationStep1.aspx): August 11, 2020 \n\n"
            "[General Election Pre-Registration Deadline](https://mnvotes.sos.state.mn.us/VoterRegistration/VoterRegistrationMain.aspx): November 3, 2020 \n\n"
            "[General Election](https://mnvotes.sos.state.mn.us/ABRegistration/ABRegistrationStep1.aspx): November 3, 2020 \n\n")

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
            terms = [
                'mn-02', \
                'mn-08', \
                'rep omar', 'rep. omar', 'ilhan', \
                'first muslim congresswoman', \
                'erik paulsen', 'rep. paulsen', 'rep paulsen', \
                'super tuesday', 'minnesota state capitol', \
                'minnesota republican', 'minneapolis mayor', \
                'threatens to sue minneapolis', 'twin cities climate strike', \
                'federal building in minnesota', 'MI, MN and WI', 'attacks on omar', 'protesters as terrorists', 'send her back', 'Trump admin holding back billions in transit funding', 'alcaida', 'pipeline in minnesota', 'minnesota house', 'mn state senate', 'rep. jason lewis', 'doug wardlow', 'rich stanek', 'political ad in minnesota', 'hennepin county sheriff', 'minnesota gop ', 'minnesota moms rise up', \
                'mn dfl', 'minnesota gubernatorial', 'minnesota dfl', \
                'tim walz', 'minnesota congress', 'justin vold', 'tina smith', 'jon applebaum', \
                'pawleny', 'pawlenty', 'minnesota state lawmaker', 'mary franson', \
                'keith ellison', 'angie craig', 'michele bachmann', 'adam jennings', 'Lt. Gov. Tina Smith', \
                # moveme
                'other for 2020', \
                'medical debt', \
                'blue, no matter who', \
                '2020 democratic nomin', \
                'clinton hating on bernie', \
                'poll numbers rise after warren', \
                'trump vs bernie'
            ]
            for term in terms:
                search(term, submission)

for sub in subs:
    print(sub)
    searchAndPost(sub)

text_file.close()
local_subs.close()