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
            terms = ['medical marijuana in utah', 'Chopper 5 was over the March for Our Lives rally', 'March for Our Lives in Salt Lake City today', 'shining example of how unPatriotic the Republican Party has become. ', 'comment on bears ears', 'give me 1 sq inch of land', 'us congress from utah', 'hundreds of utah students', 'sheldon kirkham', 'gop reintroduces bill pitting', 'donald trump highway bill', 'selling off our public lands', 'utah republicans', 'passes the Utah House', 'romney', 'Sittner', 'marijuana will be legalized in Utah', 'utah legislators', 'national monuments slashed by Trump', 'House Bill 330', 'utah lawmaker', 'rep stewart', 'utah state senate', 'legalize medical marijuana in Utah', 'Hatch\'s Seat', 'jenny wilson', 'Bears Ears Deserves Protection', 'Congressman Stewart', 'bears ears reductions', 'john curtis', 'ut-3', 'ut-03', 'shrink Utah national monument', 'monuments downsizing', 'Attack on Public Land Threatens America', 'No Wonder Millennials Hate Capitalism', 'Ruhle easily stumps Republican', 'The President Stole Your Land', 'StandWithBearsEars', 'rep. chris stewart', 'rob bishop', 'ut-01', 'orrin hatch', 'sen. hatch', 'senator hatch', 'shrink Bears Ears', 'sponsored by Hatch', 'mia love', 'mia b. love', 'rep love', 'rep. love', 'representative love', 'congresswoman love', 'ut-04', 'ut-4']
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