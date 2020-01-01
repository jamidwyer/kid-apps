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

local_subs = open("indiana.dat", "r")
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
            terms = [
                'Where do Americans die of gunfire', 'Democrats Take Control Of Mike Pence', \
                'indiana nears 20 baby boxes', \
                'senator randy head', 'security threat after she supports Bernie Sanders', \
                'Renewables and Storage Soon Beat Natural Gas', 'coming for birth control next', \
                'indiana man who vandalized a synagogue', 'your move, mayor pete', 'indiana, conservation', 'Planned Parenthood - Stop The Bans Event', 'faith-based trump rule', 'mike pence decent', 'congressman jim banks', 'fester at north side apartment', 'justification to harm people', 'Infowarrior aims to educate and preserve precious bodily fluids', 'rally in indiana', 'Marion County early vot', 'indiana\'s early vot', 'indiana law', 'liz watson', 'conservative county in indiana', 'indiana congress', 'ag curtis hill', 'Indiana precinct', 'in-sen', 'lizforindiana', 'matt cummings', 'Chicago sees its most violent week', 'states with lax gun laws ', 'in-9', 'pride parade in mike pence', 'Mike Pence\'s hometown', 'stephen chancellor', 'in09', 'Indiana Senate', 'Medicaid work requirements for Indiana', 'Illegal Guns From Indiana', 'Indiana Green Party', 'in-09', 'pelath', 'Joe Donnelly', 'Better Know a State: Indiana']
            for term in terms:
                 search(term, submission)

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Indiana 2020 Election \n\n"
            "[Register to Vote](https://indianavoters.in.gov/) \n\n"
            "[Primary Registration Deadline](https://indianavoters.in.gov/): April 6, 2020 \n\n"
            "[Primary Election](https://indianavoters.in.gov/): May 5, 2020 \n\n"
            "[Voter Registration Deadline](https://indianavoters.in.gov/): October 5, 2020 \n\n"
            "[General Election](https://indianavoters.in.gov/): November 3, 2020 \n\n")
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