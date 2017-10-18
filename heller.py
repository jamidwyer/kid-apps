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
            terms = ['^(?!.*hellerweather).*heller.*$', 'sbaih', 'Hatch Has High Hopes', 'White House fed up with the Senate', 'Steve Bannon Tears Into GOP Agenda', 'Republican gov warns Trump on health care cuts', 'going to hurt everybody', 'Democrats Revive Failed', 'Dems still dumb as shit and have learned nothing', 'invited all 52 GOP senators to come on tonight', 'Vilify Single Payer', 'GoFundMe campaigns for their medical expenses tells you everything you need to know about our healthcare system', 'Get your priorities straight, America', 'The GOP insists that the Vegas shooter', 'Rights in America', 'the most important takeaway from the Las Vegas massacre is the need for universal health care', 'Las Vegas Official Sets Up GoFundMe to Aid Shooting Victims', 'The GOP anti-establishment', 'quit Obamacare repeal because of their donors', 'Medical groups urge lawmakers to reject Graham-Cassidy bill', 'The Graham-Cassidy counterattack', 'obamacare attack', 'Trumpcare zombie', 'Graham-Cassidy Obamacare Repeal Bill', 'Graham-Cassidy ACA Repeal Bill', 'intellectual and moral garbage truck fire', 'Complacency Could Kill Health Care', 'As Candidates Line Up, Questions Grow', 'Bannon plotting primaries against slate of GOP incumbents', 'health care after trump threats', '7 Senate seats most likely to flip in 2018', 'endangered republicans stick with trump']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://nvsos.gov/sosvoterservices/Registration/step1.aspx) \n\n"
        "[**Jesse Sbaih**](https://jessefornevada.com/) is running against Dean Heller. \n\n "
        "[Facebook](https://www.facebook.com/jessesbaihsenate) | "
        "[Twitter](https://twitter.com/JesseSbaih) | "
        "[Volunteer](http://go.jessefornevada.com/page/s/homepage-volunteer) | "
        "[Donate](https://secure.actblue.com/contribute/page/jesse-homepage) \n\n"
        "Sbaih supports Medicare for all, a living wage, equal pay for equal work, protecting Social Security, affordable college, renewable energy, and campaign finance reform. \n\n\n"

        "[**Jacky Rosen**](https://www.rosenfornevada.com/) is running against Dean Heller. \n\n "
        "[Facebook](https://www.facebook.com/rosenfornevada/) | "
        "[Twitter](https://twitter.com/RosenforNevada) | "
        "[Volunteer](https://jackyrosen.cp.bsd.net/page/signup/volunteer) | "
        "[Donate](https://secure.actblue.com/donate/rosen-homepage) \n\n"
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