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
            terms = ['topless in utah', 'Top Anti-Cannabis Lawmaker is Also One of the State', 'Losing at Least 11 Republicans', 'gold mine for facial-recognition searches', 'equal rights amendment', 'thousands of phone calls threatening to kill members of Congress', 'Utah Man Arrested After Allegedly Threatening to Kill Members of Congress', 'Utah man accused of threatening to kill members of Congress', 'beginning of the fascist takeover', 'utah judge was suspended', 'police in utah', 'nerds out and the crowds go crazy', 'utah proposition 4', 'steve schmidt', 'House Speaker Greg Hughes', 'alicia colvin', 'utah republican', 'Utah medical marijuana ballot initiative,', 'senate in utah', 'Utah Medical Marijuana Initiative', 'ballot in Utah', 'medical marijuana in utah', 'us congress from utah', 'sheldon kirkham', 'donald trump highway bill', 'the Utah House', 'romney', 'Sittner', 'legalized in Utah', 'utah legislat', 'House Bill 330', 'utah lawmaker', 'rep stewart', 'utah state senate', 'legalize medical marijuana in Utah', 'Hatch\'s Seat', 'jenny wilson', 'Bears Ears Deserves Protection', 'Congressman Stewart', 'bears ears reductions', 'john curtis', 'ut-3', 'ut-03', 'Utah national monument', 'StandWithBearsEars', 'chris stewart', 'rob bishop', 'ut-01', 'orrin hatch', 'sen. hatch', 'senator hatch', 'shrink Bears Ears', 'sponsored by Hatch', 'mia love', 'mia b. love', 'rep love', 'rep. love', 'representative love', 'congresswoman love', 'ut-04', 'ut-4']
            for term in terms:
                 search(term, submission)

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Utah 2020 Election \n\n"
            "[Register to Vote](https://secure.utah.gov/voterreg/login.html?selection=REGISTER) \n\n"
            "[Primary Election](https://votesearch.utah.gov/voter-search/search/search-by-address/how-and-where-can-i-vote): November 3, 2020 \n\n"
            "[General Election](https://votesearch.utah.gov/voter-search/search/search-by-address/how-and-where-can-i-vote): November 3, 2020 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write post id back to the file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub)

text_file.close()
local_subs.close()