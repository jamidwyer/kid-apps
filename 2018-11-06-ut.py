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

local_subs = open("utah.dat", "r")
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
            terms = ['Hatch says changes to tax bill', 'GOP tax bill hits the poor harder', 'Senate GOP tax bill hurts the poor more than originally thought', 'rep. chris stewart', 'Senate Insurgency Hits a Stumbling Block in Utah', 'rob bishop', 'ut-01', 'orrin hatch', 'sen. hatch', 'senator hatch', 'Tax Fight Gets Personal as Senators Spar Over Bill', 'Senate panel approves GOP tax plan', 'Senate Tax Bill Revisions Make Its Fundamental Tradeoffs', 'Republicans are cutting health care to pay for a corporate tax cut', 'Democrats furious over new GOP attempt to gut Obamacare', 'Mitt Romney May Be Headed to the Senate', 'Trump headed to Utah in December with plans to shrink Bears Ears', 'tax bill shrouded in secrecy', 'open marine sanctuaries to oil drilling', 'attack on Bears Ears National Monument', 'Trump plans to shrink two national monuments in Utah', 'secret oatmeal cookie president', 'Trump plans to shrink size of Utah national monuments', 'Trump shrinks national monument sacred to local tribe', 'President Donald Trump is shrinking two national monuments in Utah', 'Trump to shrink Utah national monument', 'Trump to Shrink Two Utah National Monuments', 'Trump says he will shrink Bears Ears National Monument', 'Hatch-authored drug law that may hurt DEA enforcement', 'Corporations to keep tax break lost by millions of Americans', 'sponsored by Hatch', 'Bannon putting Senate majority at risk in 2018', 'no significant benefit for poorest families', 'Congress to hold off on gun silencer legislation', 'jokes that Republican tax-reform plan is', 'Will Hatch run again or retire', 'governor and senator for two different states', 'Wilson would beat Hatch', 'Mitt Romney has politicos asking', 'Bipartisan Push Shakes Up Capitol Hill', 'Hatch has some daunting numbers to overcome', 'hatch: calling trump racist', 'racist bone in his body ', 'shot their wad', 'Meant It the Civil War Way', 'definitively say whether he is breaking promise, running again', 'announcement on his political future has been pushed back', 'mia love', 'mia b. love', 'rep love', 'rep. love', 'representative love', 'congresswoman love', 'ut-04', 'ut-4', 'Love used campaign funds for Disney World', 'Love wants to morph a Forest Service building', 'love\'s constituent meeting format', 'constituents say they were left off her invite list', 'Love has a new chief of staff', 'Love\'s not on board.', 'better way to talk with constituents']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Utah 2018 Election \n\n"
            "[Primary Voter Registration Deadline](https://secure.utah.gov/voterreg/index.html): June 19, 2018 \n\n"
            "[Primary Election](https://elections.utah.gov/Media/Default/Documents/Elections%20Resources/Absentee%20Ballot%20Application.pdf): June 26, 2018 \n\n"
            "[General Election](https://elections.utah.gov/Media/Default/Documents/Elections%20Resources/Absentee%20Ballot%20Application.pdf): November 6, 2018 \n\n")
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