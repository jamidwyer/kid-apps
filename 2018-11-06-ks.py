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
    for submission in subreddit.hot(limit=50):
        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['oppose all efforts to validate transgender identity', 'kansas state house', 'AR-15 raffle, just days after Parkland shooting', 'Colyer tells people on Medicaid expansion', 'Green Party Expands Candidate Recruitment to Idaho and Kansas', 'Kansas vulnerable to election hacking', 'Kansas Scrambles To Change Rules', 'Legislative Update 2018 Session ', 'ksleg', 'Kansas and Oklahoma Are Fighting the Good Fight', 'No, Kansas, you can', 'Happy Fasting Kansas', 'Kansas Attorney General', 'ks legislature', 'Week 2 KS Politics Recap', 'KS Politics Week 2 Recap', 'brent welder', 'Kansas Legislative', 'White House admits in court filing that it hasn', 'steve alford', 'Kansas lawmaker', 'Kansas lawmaker', 'racist thoughts on marijuana at Garden City Forum', 'http://bloomsmag.com/a-mathematician-may-have-uncovered-widespread-election-fraud-and-kansas-is-trying-to-silence-her/', 'Republicans are openly attacking American Democracy', 'voter fraud commission', 'voter-fraud commission', 'election fraud commission', 'Links Related to The Koch Brothers', 'kelly rippel', 'Kansas Congressional Delegation', 'Moderate Republican Win in Kansas', 'No tax increase for Kansas schools', 'paul davis', 'Net neutrality protests planned in Kansas City, Olathe', 'Kansas official goes off on bizarre racist rant', 'kansas budget crisis', 'Even Try to Defend Its Israel Anti-Boycott Law', 'candidates for the 2018 elections in Kansas', 'yoder', 'ks-3', 'ks-03', 'chris haulmark', 'ks-2', 'ks-02', 'jenkins, lynn', 'congressman jenkins', 'lynn jenkins', 'rep jenkins', 'steve fitzgerald', 'The House Retirement Tide Is Coming', 'A list of who\'s leaving Congress', 'ks-4', 'ks-04', 'Kansas\' 4th Congressional District', 'kansas 4th congressional district', 'congressman estes', 'ron estes', 'rep estes', 'kansas veteran james thompson', 'brownback', 'kobach', 'colyer', '^(?!.*arkansas governor).*kansas governor.*$', 'carl brewer', 'Trump voter fraud panel', 'trump voting commission', 'destroyed the Kansas economy', 'Trump Election Fraud Panel Leader', 's Election Commission', 'Kansas tax cut experiment', 'governor in kansas', 'voter-fraud propandist', 'kansas republican governance experiment', 'house minority leader jim ward', 'Trump Voter Fraud Probe', '\"election integrity commission\"', '\'election integrity commission\'', 'Trump\'s voter-fraud panel', 'Trump\'s election commission co-chair', '\'election integrity\' panel', 'Trump voting panel']
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

        # Write the post id back to the file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()