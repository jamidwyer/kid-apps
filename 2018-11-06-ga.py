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

local_subs = open("georgia.dat", "r")
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
            terms = ['cloud act', 'massive crowd at the March for our Lives', 'law in georgia', 'georgia democrats', 'Remove ALL Privacy Protections For Data Stored On The Cloud', 'georgia congressman', 'georgia gop pushes', 'georgia voters', 'students in atlanta take a knee', 'Obama generation is done with the Democratic Party', 'advances in ga. house', 'georgia gop chooses', 'Georgia 12 District', 'If you live in the 5th District like me, here is some information', 'Georgia Republican Stupidly Threatens Delta', 'Georgia senator claiming Planned Parenthood', 'ga-12', 'casey cagle', 'georgia boycott', 'Airplane Discount For NRA', 'Antigay Adoption Bill Moves Towards Passage in Georgia', 'trent nesmith', 'Prevent Another Decade of GOP Gerrymandering', 'Fat fuck cops suffocate man to death', 'Gwinnett State House district', 'georgia legislators', 'Georgia Democrats are zeroing in', 'georgia governor', 'Leaning States Drop From 44 to 39', 'georgia 6th', 'georgia lawmakers', 'Georgia Midterms', 'fran millar', 'Black Women Vote More, But Remain Underrepresented in Politics', 'Lawmakers propose switching Georgia', 'doug collins', 'rep. collins', 'rep collins', 'Reddest district in Georgia', 'representative collins', 'congressman collins', 'ga-9', 'ga-09', 'Georgia turns blue', 'kevin abel', 'Crackdown On Unlicensed Ga. Facilities', 'Republicans dust off Georgia special election playbook for midterms', 'State Legislators Across the Country Are Joining Forces to Fight for Reproductive', 'Trump approval rating 36.7' 'approval ratings in Georgia erode', ' Disapproval in Georgia', 'female political activism that could shift the course of US politics', 'GA House of Representatives', 'Georgia\'s Election System', 'Poverty Is Both a Political and a Moral Choice Made By the Powerful', 'Journalist found guilty of obstruction of justice after suing Sheriff Candidate', 'In Georgia, battle of the \'Staceys\'', 'jeffares' 'buddy carter', 'lisaringga', 'lisa ring', '@repbuddycarter']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Georgia 2018 Election \n\n"
            "[Primary Election Registration Deadline](https://www.mvp.sos.ga.gov/MVP/mvp.do): April 23, 2018 \n\n"
            "[Primary Election Early Voting Starts](https://www.mvp.sos.ga.gov/MVP/mvp.do): April 30, 2018 \n\n"
            "[Primary Election](https://www.mvp.sos.ga.gov/MVP/mvp.do): May 22, 2018 \n\n"
            "[General Election Registration Deadline](https://www.mvp.sos.ga.gov/MVP/mvp.do): October 9, 2018 \n\n"
            "[General Election Early Voting Starts](https://www.mvp.sos.ga.gov/MVP/mvp.do): October 15, 2018 \n\n")
            "[General Election](https://www.mvp.sos.ga.gov/MVP/mvp.do): November 6, 2018 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write our post id to the tracking file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()