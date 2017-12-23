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

local_subs = open("florida.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top 500 values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['Another opportunity in Florida', 'Puerto Rican governor vows to unseat House GOP in 14 states', 'pedestrian tickets are wrongly issued, statewide', 'latvala', 'profit from undocumented laborers, dump them after injuries', 'Mueller in escalating GOP attacks', 'Republicans are refusing to continue Trump investigation', '^(?!.*gov. scott walker).*gov. scott.*$', 'Florida law punishes immigrant workers', 'Florida HD-58', 'GOP congressmen stop obstructing the critical', 'Watch A Republican Congressman Go Bat Shit Crazy', 'gaetz', '2018 congressional races in Florida', 'going to the one on Lake Underhill', 'Verizon Protest in North Miami', 'Where in the world can children be legally married at the age of 13', 'Scott request to remove Pariente from case', 'attention to the 2018 Gov races', 'rick scott', 'Florida Democratic governor', 'Florida online voter registration finally arrives', 'deletes voicemails from nursing home', 'Florida Nursing Home, Many Calls for Help', 'Voicemail to Governor Deleted', 'Florida hurt sick kids to help big GOP donors', 'governor scott', 'florida governor', 'fla. governor', 'governor of florida', 'Time To Talk About Climate Change', 'curbelo', 'Million dollar bracket in the works for GOP tax plan', 'congressional GOP helped Trump keep tax returns secret', 'register ONLINE to vote in Florida! Spread the news', 'Congress gives Trump a pass on releasing his tax returns', 'Republicans vote against forcing Trump to release tax returns', 'Congress gives Trump pass on his tax returns', 'brian mast', 'rep mast', 'rep. mast', 'representative mast', 'congressman mast', 'fl-18', 'lehtinen', 'fl-27', 'Republican candidate believes aliens abducted her', 'Jesus-Like Aliens', 'candidate claims she was visited by aliens', 'desantis', 'dennis ross', 'fl-15', 'andrew learned', 'balart', 'fl-25']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Florida 2018 Election \n\n"
            "[Primary Voter Registration Deadline](https://registertovoteflorida.gov/en/Registration/Eligibility): July 30, 2018 \n\n"
            "[Primary Election](http://dos.myflorida.com/elections/for-voters/voting/absentee-voting/): August 28, 2018 \n\n"
            "[General Election](http://dos.myflorida.com/elections/for-voters/voting/absentee-voting/): November 6, 2018 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write the post id to the tracking file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()