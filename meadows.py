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

local_subs = open("northcarolina.dat", "r")
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
            terms = ['mark meadows', 'rep. meadows', 'Skeptical Reception From Some in Congress', 'republicans think trump is unstable', 'Meadows: Time to ', 'highlight broader concerns in GOP', 'Retiring GOP lawmaker defends Corker', 'Trump, GOP weigh surtax on wealthy', 'money gets into politics but still not be bothered by it', 'closed until Republicans pass health and tax reform', 'House Crazies Angry At Trump', 'Mistakenly Put on Brief Against Partisan Gerrymandering', 'Trump blasts own party', 'Mean to Sign Brief Against Gerrymandering', 'accidentally asked the Supreme Court to end gerrymandering', 'Inside the Freedom Caucus', 'Deal with Democrats Is Nightmare Come True', 'Freedom Caucus leaders vent to Paul Ryan', 'Meadows: Shutdown possible without border wall funding', 'freedom caucus leader', 'Republicans Are Already Fighting With Each Other Over How To Pass Harvey Disaster Relief Bill', 'Representative meadows', 'congressman meadows', 'rep meadows']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://www.ncsbe.gov/Voters/Registering-to-Vote) by October 12, 2018 \n\n"
            "[Sign up to vote by mail](https://www.ncsbe.gov/Portals/0/Forms/NCAbsenteeBallotRequestForm.pdf) \n\n\n"

            "[**Phillip Price**](https://price4wnc.com/visions/) is running to represent North Carolina District 11. \n\n"
            "[Donate](https://price4wnc.com/#donation-form-page-anchor) | "
            "[Facebook](https://www.facebook.com/phillippriceforcongress/) | "
            "[Twitter](https://twitter.com/price4wnc) \n\n"
            "Price supports universal health care, public schools, protecting Social Security, equal pay for equal work, renewable energy, and campaign finance reform. \n\n\n"

            "General Election: November 6, 2018 \n\n"
            "[Map of North Carolina District 11](https://www.govtrack.us/congress/members/NC/11) \n\n "

            "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people instead of billionaire political donors.)")

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