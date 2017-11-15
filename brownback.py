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

local_subs = open("kansas.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=100):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['brownback', 'kobach', 'colyer', 'kansas governor', 'carl brewer', 'Kansas proposes Medicaid work requirement', 'Trump voter fraud panel', 'As Trump Proposes Tax Cuts, Kansas Deals With Aftermath Of Experiment', 'More than a dozen states still refuse to release voter data', 'trump voting commission', 'Trump-style tax cuts in Kansas', 'story of the 2016 election is voter suppression', 'disastrous Republican plan did to Kansas', 'Kansas Republicans Warn Congress Not to Repeat', 'destroyed the Kansas economy', 'Trump Election Fraud Panel Leader', 'Kansas still underfunds schools', 'Denying A Lifeline To Rural Hospitals And Patients', 'Kansas literally has no rules for Governorship elections', 's Election Commission', 'kansas: tax experiment failed', 'if a dog tried to run for Governor', 'Kansas tax cut experiment', 'governor in kansas', 'State workers at site of shooting had guards, security until Kansas', 'Trump\'s Voter Fraud Commission', 'waging war on the right to vote', 'GOP Is Plowing Ahead with an Audacious Effort to Hijack the VotexR', 'Voter Commission Reveals Its Bias', 'voter-fraud propandist', 'GOP to Latinos: Drop Dead', 'testify at Trump voter commission meeting', 'Voter Fraud Commission Clashes Over New Hampshire Count', 'Trump official accused 5,000 people of voter fraud with no proof', 'Lawsuits, Falsehoods, and a Lot of White Men', 'kansas republican governance experiment', 'house minority leader jim ward', 'Trump Voter Fraud Probe', '\"election integrity commission\"', 'Trump\'s voter-fraud panel', 'Trump\'s election commission co-chair', '\'election integrity\' panel', 'Trump voting panel']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Kansas 2018 Election \n\n"
            "[Primary Voter Registration Deadline](https://www.kdor.ks.gov/apps/voterreg/default.aspx): July 17, 2018 \n\n"
            "[Primary Election](http://www.kssos.org/forms/elections/AV1.pdf): August 7, 2018 \n\n"
            "[General Election](http://www.kssos.org/forms/elections/AV1.pdf): November 6, 2018 \n\n")
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