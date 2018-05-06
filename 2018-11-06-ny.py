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

local_subs = open("newyork.dat", "r")
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
            terms = ['cynthia effect', 'Judge rules New York condo board may remove', 'new york state senat', 'cuomo signs bill', 'May Day Protesters Rally in New York City', 'maggie haberman', 're glancing toward rural ones, too', 'ICE held an American man in custody for 1,273 days', 'howie hawkins', 'You can clesrly see the Trumpgret.', 'new york senate', 'steve stern', 'Milo Yiannopoulos shouted out of NYC bar', 'cynthianixon', 'crazy jew', 'new york may legaliz', 'trump tower fire', 'well built building', 'cynthia nixon', 'fire at trump tower', 'ny-24', 'n.y. passes bill', 'kurt schlickter', 'green party of new york', 'nra-backed n.y. pols', '9/11 first responders', 'tenney', 'NY State bill', 'ny-21', 'Billionaires Row', 'ny-19', 'Alexandria Ocasio-Cortez', 'ny19', 'new york lawmakers', 'Governor Cuomo', 'New York gov', 'ny27', 'New York City\'s fossil fuel divestment could spur global shift', 'New York City Declares War on the Oil Industry', 'New York Finally Consider Legalizing Cannabis', 'sara idleman', 'peter king', 'katko', '^(?!.*burkina faso).*faso.*$', 'daniel donovan', 'dan donovan', 'ny-11', 'rep. donovan', 'rep donovan', 'representative donovan', 'congressman donovan', 'michael grimm', 'GOP incumbent over Grimm']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post

        text = ("New York 2018 Election \n\n"
            "[Federal Primary Election Date](https://voterlookup.elections.state.ny.us/votersearch.aspx): June 26, 2018 \n\n"
            "[State Primary Election Date](https://voterlookup.elections.state.ny.us/votersearch.aspx): September 13, 2018 \n\n"
            "[General Election Registration Deadline](https://voterreg.dmv.ny.gov/MotorVoter/): October 12, 2018 \n\n"
            "[General Election Date](https://voterlookup.elections.state.ny.us/votersearch.aspx): November 6, 2018")
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