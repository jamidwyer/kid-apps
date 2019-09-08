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

local_subs = open("colorado.dat", "r")
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
            terms = ['ludlow massacre', 'keep the pressure on ice', 'rally at civic center park', 'nervous republicans', 'ruth bader ginsburg', 'Electoral College Members Can Defy Vote', 'leads in colorado', 'hickenlooper', 'after columbine', 'Babies Born Near Oil and Gas Wells', 'donations to senate republicans', '1 Billion Reasons Why More States Will Legalize', 'ICE shows up at your door', 'cory gardner', 'Candidates Mostly Agree on Marijuana', 'colorado unveils roadmap', 'Cannabis Banking', 'colorado passes bill', 'colorado cop', 'hospital services in colorado', 'david sirota', 'abuse you and you will have to like it', 'Pushing people this hard for a min wage job ugh', 'purchase average home in denver', 'rep. eviscerates joe biden', 'm not clear on why exactly', 'infowarriors gotta park their rides somewhere', 'colorado public lands', 'colorado pot sales', 'colorado legislat', 'purged from the colorado rolls', 'Colorado Democratic candidate', 'boulder county Republican', 'Aurora ICE facility', 'national popular vote', 'Broadway telling people not to sign petitions', 'denver law', 'denver mayor', 'Mueller now, has to prep for NK.', 'rural teachers working second jobs', 'colorado green party', 'thousands and thousands teachers', 'co teachers strike', 'colorado lawmaker', 'colorado teachers are going on strike', 'Colorado must fight to protect net neutrality', 'colorado state rep.', 'colorado fracking company', 'Colorado Teachers Walk', 'action by colorado teachers', 'great sand dunes national park', 'co-gov' 'dsA denver', 'colorado bill', 'political group in Colorado', 'colorado state senate', 'cynthia coffman', 'colorado governor', 'colorado poll', 'colorado vot', 'emily sirota', 'jared polis', 'Doug Lamborn', 'ken buck', 'steve curtis', 'mike coffman', 'co-06', 'co-6', 'rep. coffman', 'rep coffman', 'representative coffman', 'congressman coffman']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Colorado 2020 Election \n\n"
            "[Register to Vote](https://www.sos.state.co.us/voter/pages/pub/olvr/verifyNewVoter.xhtml) \n\n"
            "[Presidential Primary Election](https://www.sos.state.co.us/voter/pages/pub/home.xhtml): March 3, 2020 \n\n"
            "[Primary Election](https://www.sos.state.co.us/voter/pages/pub/home.xhtml): June 30, 2020 \n\n"
            "[General Election](https://www.sos.state.co.us/voter/pages/pub/home.xhtml): November 3, 2020 \n\n")
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