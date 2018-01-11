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
            terms = ['tim kaine', 'I emailed a long letter to my congressman, and got this back', 'March on Roanoke', 'Recount court denies Democrat', 'These childish attacks raise the risk of stumbling into an avoidable war', 'looks good for 2018 state legislature candidates in rural areas', 'vote has changed the balance of power in the Virginia House of Delegates', 'wins by one vote, leaving Virginia House', 'Virginia State House race by single vote', 'Virginia race comes down to 1 vote', 'One-vote recount win', 'Newport News Dem wins seat by 1 vote', 'One vote can make a difference', 'Shelly Simonds', 'single vote leads to a rare tie', 'Va. House seat in recount by single vote', 'winning a seat in recounts by a single vote', 'margin down to 6 votes', 'Families warned they may lose children\'s health coverage', 'appeal to the secretary of the commonwealth', 'corey stewart', 'rob wittman', 'Republicans flee from McConnell', 'scott taylor', 'rep. taylor', 'congressman taylor', 'rep taylor', 'my Virginia Congressional Elections ratings', 'Ralph Northam won in 2 Republican', 'dave brat', 'rep. brat', 'congressman brat', 'rep brat', 'representative brat', 'Totally normal politician behavior', 'first Dem to win key Virginia county in 56 years', 'Conservatives drop demands for bigger spending cuts to get to tax reform', 'GOP Congressmen Call For Mueller Hearings', 'Republicans in Congress Cheered', 'Freedom Caucus endorses GOP tax plan', 'goodlatte', 'wave of Republicans leaving Congress', 'House Judiciary chairman', 'U.S. House panels open probe into Justice Department', 'House GOP leaders open probe into FBI', 'latest Republican patsy', 'Lawmakers grapple with warrantless wiretapping program', 'barbara comstock', 'rep. comstock', 'congresswoman comstock', 'rep comstock', 'representative comstock', 'va-10', 'comstock challenger', 'Dems think Trump can deliver suburbs to their party', 'Every Member of Congress Who Took Money From the NRA and Tweeted', 'who in Congress is getting money from the NRA', 'Obamacare repeal effort into doubt', 'tom hicks']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Virginia 2018 General Election \n\n"
            "[Primary Election Registration Deadline](https://vote.elections.virginia.gov/Registration/Eligibility): May 21, 2018 \n\n"
            "[Primary Election](http://www.elections.virginia.gov/voter-outreach/where-to-vote.html): June 12, 2018 \n\n"
            "[General Election Registration Deadline](https://vote.elections.virginia.gov/Registration/Eligibility): October 15, 2018 \n\n"
            "[General Election](http://www.elections.virginia.gov/voter-outreach/where-to-vote.html): November 6, 2018 \n\n")
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