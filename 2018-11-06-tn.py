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

local_subs = open("tennessee.dat", "r")
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
            terms = ['Democrats see new prospects in U.S. South', 'elected to Congress despite their scandals', 'In Ohio they are about to vote', 'Retaking the Senate in Tennessee', 'fighting for Net Neutrality in Knoxville', 'protest tonight at the Verizon on Gunbarrel', 'TN Democrats Vote To Support Medical Marijuana', 'Knoxville demolishes the mental health ward', 'last Democrat to win a statewide race in Tennessee', 'bredesen', 'Net Neutrality protections in North Knoxville', 'where you stand, Marsha', 'david kustoff', 'tennessee governor', 'tn gubernatorial', 'gov. of tn', 'tennessee gubernatorial candidates', 'governor haslam', 'randy boyd', 'kay white', 'tn governor', 'House Budget chair', 'Diane Black', 'bill lee', 'beth harwell', 'karl dean', 'mae beavers', 'tennessee senate race', 'Possible 2020 run against Trump not ruled out', 'A Democratic Senate Majority Hinges on Tennessee', 'The GOP Budget Is A Mess', 'Senate Republicans pass budget that will add', 'discuss Tennessee politics and candidates', '1.5 trillion to deficit, slash Medicare and Medicaid', 'Corker Rages About', 'Senate GOP passes Trump\'s tax plan', 'Senate GOP votes to revoke Democrats', 'How Republicans Got Trump Catastrophically Wrong', 'Trump-Corker spat complicates drive for tax reform', 'bob corker', 'sen. corker', 'mackler', 'blackburn', 'corker\'s u.s. senate seat', 'replace corker', 'Senate narrowly passes 2018 budget', 'Participated in Normalizing', 'TWITTER shuts down anti-abortion campaign video', 'disgusting lies about Planned Parenthood', 'Senate candidate from advertising false claim about Planned Parenthood', 'Corker fight', 'baby body parts', 'Twitter takes down GOP lawmaker', 'alliance with powerful Republican senator broke down into verbal warfare', 'become an adult day care center', 'announces her bid by trashing the Republican Senate', 'Berke considering run', 'Budget battles loom on Capitol Hill', 'tax reform will make health care look like', 'peyton manning', 'andy ogles', 'senator corker', 'Corkers seat', 'Tennesseeans, and this nation to the Telecom lobby', 'Come join our fight for Net Neutrality', 'marsha blackburn', 'tn-7', 'tn-07']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Tennessee 2018 Election \n\n"
            "[Primary Election Registration Deadline](https://ovr.govote.tn.gov/Registration/#BM): July 3, 2018 \n\n"
            "[Primary Election](http://web.go-vote-tn.elections.tn.gov/): August 2, 2018 \n\n"
            "[General Election Registration Deadline](https://ovr.govote.tn.gov/Registration/#BM): October 9, 2018 \n\n"
            "[General Election](http://web.go-vote-tn.elections.tn.gov/): November 6, 2018 \n\n")
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