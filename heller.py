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

local_subs = open("nevada.dat", "r")
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
            terms = ['^(?!.*hellerweather).*heller.*$', 'quit Obamacare repeal because of their donors', 'Senate prepares for another health-care debate', 'Medical groups urge lawmakers to reject Graham-Cassidy bill', 'The Graham-Cassidy counterattack', 'health bill will protect people with pre-existing conditions', 'ram Obamacare repeal through', '18 million more without insurance', 'plan stumbles under opposition from governors', 'blasted the new Republican healthcare bill', 'New push to replace Obamacare', 'new health bill will hurt Nevadans', 'GOP pushes last-ditch health care bill', 'latest ObamaCare repeal bill', 'ObamaCare repeal despite lack of full CBO analysis', 'swallow deep Medicaid cuts for GOP', 'phase out Medicaid in its entirety', 'worst ObamaCare repeal proposal yet', 'Congressional members focus on issues close to their hearts this week', 'care measure goes further than the failed one', 'obamacare attack', 'Trumpcare zombie', 'Republicans Really Could Repeal Obamacare', 'GOP ObamaCare repeal bill gains momentum', 'Yet Another Terrible Obamacare Repeal Bill', 'Graham-Cassidy Obamacare Repeal Bill', 'Graham-Cassidy ACA Repeal Bill', 'intellectual and moral garbage truck fire', 'Complacency Could Kill Health Care', 'Republican senators are trying to gut your health care', 'Senate GOP tries one last time to repeal Obamacare', 'the latest Obamacare repeal bill is terrible', 'The GOP learned nothing from their previous failure to pass Trumpcare', 'let insurers jack up premiums as soon as you get sick', 'Healthcare Bill Nears 50 Votes of Support', 'Wynn to rally field troops Wednesday in Vegas', 'As Candidates Line Up, Questions Grow', 'The last GOP health plan left standing, explained', 'Republicans have exactly 18 days to repeal Obamacare', 'desperate Hail Mary to repeal Obamacare', 'Bannon plotting primaries against slate of GOP incumbents', 'health care after trump threats', 'Congress resumes health care fight', 'Congress face packed September agenda', '7 Senate seats most likely to flip in 2018', 'endangered republicans stick with trump']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://nvsos.gov/sosvoterservices/Registration/step1.aspx) \n\n"
        "[**Jacky Rosen**](https://www.rosenfornevada.com/) is running against Dean Heller. \n\n "
        "[Donate](https://secure.actblue.com/donate/rosen-homepage) | "
        "[Facebook](https://www.facebook.com/rosenfornevada/) | "
        "[Twitter](https://twitter.com/RosenforNevada) \n\n "
        "Rosen supports affordable health care for every American, public schools, protecting Social Security and Medicare, renewable energy, net neutrality, and DACA. \n\n\n"

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