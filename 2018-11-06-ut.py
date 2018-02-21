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
            terms = ['Mitt should have predicted it', 'Today, MR accepts Trump\'s endorsement', 'Utahns like the sound of voting', 'Want to find out who are Utah', 'Bears Ears Is Sacred to Native Tribes', 'dear mitt', 'romney', 'Southern Utah GOP official arrested', 'Sittner jumps into 2nd Congressional District race', 'marijuana will be legalized in Utah', 'Bill would ban policing quotas in Utah', 'Utah taxpayers paid for hotel room', 'Bill seeks to limit how Utah city and local officials speak up', 'Sexual assualt advocacy day on capitol hill Tuesday, february 13', 'utah legislators', 'taxpayer money for sex with escort', 'recording bill supported by the Salt Lake Chamber and Mormon', 'national monuments slashed by Trump', 'House Bill 330', 'utah lawmaker', 'rep stewart', 'utah state senate', 'legalize medical marijuana in Utah', 'Hatch\'s Seat', 'jenny wilson', 'Trump begged Hatch', 'These 16 Major Environmental Protections Were Cut in 2017', 'Provo lawmaker eyes DUI change', 'Bears Ears Deserves Protection', 'Congressman Stewart', 'Yo Utah!', 'Senate GOP Passes Tax Bill', 'Koch brothers, campaign donors, and corporations', 'tax breaks for billionaires, and not extending a health insurance program for children', '14 GOP Senators stand to reap millions', 'declaring pornography a public heath crisis', 'bears ears reductions', 'john curtis', 'ut-3', 'ut-03', 'feud with Patagonia', 'shrink Utah national monument', 'House committee trying to gaslight the country', 'big one hits, you won\'t be able to deduct your losses', 'Republicans would rather give heirs and heiresses a tax break', 'Republican War on Children', 'Sugar House net neutrality protest', 'monuments downsizing', 'Trump Is Coming For Your National Monuments', 'evil hatch', 'Attack on Public Land Threatens America', 'No Wonder Millennials Hate Capitalism', 'Ruhle easily stumps Republican', 'The President Stole Your Land', 'StandWithBearsEars', 'rep. chris stewart', 'rob bishop', 'ut-01', 'orrin hatch', 'sen. hatch', 'senator hatch', 'shrink Bears Ears', 'sponsored by Hatch', 'mia love', 'mia b. love', 'rep love', 'rep. love', 'representative love', 'congresswoman love', 'ut-04', 'ut-4']
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

        # Write post id back to the file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()