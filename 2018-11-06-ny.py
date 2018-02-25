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
            terms = ['drone wars going up all over Syracuse, NY', 'claudia tenney', ' Deaths Be in Vain', 'NY State bill to legalize marijuana', 'New York Post\'s call for Trump to enact gun control', 'Not Crimes of Character', '34 states, police officers can legally have sex with detainees', 'Blasio wants more people to vote', 'ny-21', 'Billionaires Row', 'Our laws regarding sexual consent must be brought into line with basic common sense', 'NYC Taxi Driver Kills Himself', '35 states where police officers can claim that a detainee consented', 'New York and 34 other states allow cops to have sex with someone in their custody', 'ny-19', 'Lottery Winner Dies of Cancer 23 Days After', 'Alexandria Ocasio-Cortez', 'take a look at Saudi Arabia, open the documents', 'ny19', 'Self-employed carpenter couldn\'t afford to go to the doctor', 'new york lawmakers', 'Governor Cuomo', 'Women\'s March on NYC', 'New York gov', 'hoping for a terrorist attack to counter 2018 elections', 'nyc women\'s march', 'A man who knows. Women', 'Trump suggests that a terror attack could help Republicans in the 2018 midterms', 'terror attack could save him and GOP from 2018 election bloodbath', 'New York City homeless shelter faces resistance', 'New York to look at legalizing recreational marijuana', 'Marijuana legalization may be coming to New York sooner rather than later', 'ny27', 'New York City\'s fossil fuel divestment could spur global shift', 'New York City Declares War on the Oil Industry', 'New York Finally Consider Legalizing Cannabis', 'New York Police Union Sues to Stop Release of Body Camera Videos', 'Fund Early Voting', 'Republicans Poised for Collapse in New York', 'sara idleman', 'New York introduces its own net neutrality bill', 'barely disguised reward for billionaire donors', 'GOP tax plan the result of a runaway campaign finance system', 'peter king', 'Net Neutrality Supporters At NYC Verizon Store', 'House Seats Democrats Are Hoping to Win in 2018', 'GOP Tax Bill Displays American Oligarchy', 'katko', '^(?!.*burkina faso).*faso.*$', 'daniel donovan', 'dan donovan', 'ny-11', 'rep. donovan', 'rep donovan', 'representative donovan', 'congressman donovan', 'michael grimm', 'GOP incumbent over Grimm']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post

        text = ("New York 2018 Election \n\n"
            "[Primary Election Date:](https://voterlookup.elections.state.ny.us/votersearch.aspx): June 26, 2018 \n\n"
            "[General Election Registration Deadline](https://voterreg.dmv.ny.gov/MotorVoter/): October 12, 2018 \n\n"
            "[General Election Date:](https://voterlookup.elections.state.ny.us/votersearch.aspx): November 6, 2018")
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