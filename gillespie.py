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

local_subs = open("virginia.dat", "r")
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
            terms = ['^(?!.*west virginia governor).*virginia governor.*$', 'virginia\'s governor race', 'va governor', 'what va. voters can agree on', 'Judgment Day for Trump', 'resistance in question in Virginia race', 'talk to me about showing up', 'Grip on the GOP Gets Stronger as the Party Gets Smaller', 'Our Great Heritage', 'Why Conservatives Blame Poverty on the Poor', 'Northam touts', 'candidate stirs no love in Virginia\'s Trump country', 'giant turnout operation has been underway in VA', 'The Democrats should be terrified by this governor', 'Virginia Democrats Spooked', 'Obama tells Democrats to reject politics of division, fear', 'Virginia tests whether an establishment Republican can succeed', 'obama\'s back', 'our democracy is at stake', 'Candidate for Governor in Virginia', 'politics while rallying for Virginia Dem', 'Northam/Fairfax/Herring', 'Republicans Have Stockholm Syndrome', 'va gov:', 'cities are you seeing these ads', 'Americans Suck at Voting, But', 'scamming runs very, very deep', 'got a governor to elect in three weeks', 'tiny crowd at a rally in the reddest part of Virginia', 'GOP nominee quietly plots with white nationalists', 'Richmond rally for Northam', 'northam and gillespie', 'mcauliffe', 'gillespie', 'va gov race', 'VA gov candidate', 'Virginia needs a governor', 'va. gubernatorial race', 'gillespe', 'Virginia\'s race for governor', 'virginia gubernatorial']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; VOTE &#9733;&#9733;&#9733;](http://www.elections.virginia.gov/voter-outreach/where-to-vote.html) November 7, 2017 \n\n"

            "[**Ralph Northam**](http://ralphnortham.com/) is running to be Governor of Virginia. \n\n"
            "[Reddit](https://www.reddit.com/r/RalphNortham/) | "
            "[Facebook](https://www.facebook.com/ralph.northam) | "
            "[Twitter](https://twitter.com/RalphNortham) | "
            "[Donate](https://act.myngp.com/northam/homepage) \n\n "
            "Northam supports universal health care, paid family leave, college affordability, equal pay for equal work, renewable energy, and LGBT equality. \n\n\n"

            "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people instead of billionaire political donors.)")

        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Store the current id into our list
        posts_replied_to.append(submission.id)

for sub in subs:
     print(sub)
     searchAndPost(sub);

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

text_file.close()
local_subs.close()