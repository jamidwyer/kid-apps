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

local_subs = open("washington.dat", "r")
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
            terms = ['dave reichert', 'rep. reichert', 'rep reichert', 'representative reichert', 'congressmen reichert', 'congressman reichert', 'wa-8', 'wa-08', '@davereichert', 'wa\'s 8th district', 'Majority of Democrats Want Bold Leftward Shift', 'Here Come the Republican Retirements', 'Three repub congressman have bailed on 2018 run', 'Reichert announces he will not seek reelection in 2018']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://weiapplets.sos.wa.gov/MyVoteOLVR/MyVoteOLVR) \n\n"
            "[**Robert Hunziker**](http://voteroberthunziker.com/) is running to represent Washington's 8th Congressional District. \n\n"
            "[Facebook](https://www.facebook.com/VoteRobertHunziker/) | "
            "[Twitter](https://twitter.com/VoteRobertH) | "
            "[Volunteer](http://voteroberthunziker.com/volunteer/) | "
            "[Donate](https://secure.anedot.com/marts/donate) \n\n "
            "Hunziker supports Medicare for all (HR 676), a living wage, affordable housing, affordable college, renewable energy, campaign finance reform, and automatic voter registration.  \n\n"

            "[**Tom Cramer**](http://www.tomcramerforcongress.org/) is running to represent Washington's 8th Congressional District. \n\n"
            "[Volunteer](http://www.tomcramerforcongress.org/volunteer) | "
            "[Donate](https://tomcramer.nationbuilder.com/donate) \n\n "
            "Cramer supports Medicare for all, affordable college, and LGBTQ equality.  \n\n"

            "[**Kim Schrier**](https://www.drkimschrier.com/) is running to represent Washington's 8th Congressional District. \n\n"
            "[Facebook](https://www.facebook.com/DrKimSchrier/) | "
            "[Twitter](https://twitter.com/DrKimSchrier) | "
            "[Volunteer](https://schrier.bsd.net/page/s/volunteer) | "
            "[Donate](https://secure.actblue.com/donate/kimschrier) \n\n "
            "Schrier supports universal health care with a subsidized Medicare public option, public schools, affordable college, a living wage, campaign finance reform, and DREAM and DACA.  \n\n"

            "[**Brayden Olson**](https://www.braydenforourfuture.com/) is running to represent Washington's 8th Congressional District. \n\n"
            "[Facebook](https://www.facebook.com/BraydenOlson) | "
            "[Volunteer](https://www.braydenforourfuture.com/#takeaction) | "
            "[Donate](https://secure.actblue.com/donate/braydenforcongress) \n\n "
            "Olson supports universal health care and renewable energy.  \n\n"

            "[**Brian Kostenko**](http://kostenkoforcongress.com/home) is running to represent Washington's 8th Congressional District. \n\n"
            "[Twitter](https://twitter.com/votekostenko) | "
            "[Volunteer](http://kostenkoforcongress.com/volunteer) | "
            "[Donate](http://kostenkoforcongress.com/support) \n\n "
            "Kostenko supports universal health care and a living wage.  \n\n"

            "[**Mona Das**](https://www.electmona.com/more-about-mona) is running to represent Washington's 8th Congressional District. \n\n"
            "[Facebook](https://www.facebook.com/electmona/) | "
            "[Twitter](https://twitter.com/elect_mona) | "
            "[Donate](https://secure.squarespace.com/commerce/donate?donatePageId=595b20538419c2e81ee2f471) \n\n"

            "Das supports universal health care.  \n\n"

            "[Map of Washington District 8](https://www.google.com/maps/d/u/0/viewer?ll=47.59875500000003%2C-121.21215799999999&spn=2.222513%2C2.883911&hl=en&t=m&msa=0&z=8&source=embed&ie=UTF8&mid=1qzIBZU5QZgKWh_woys_JM2h5HqY) \n\n"

            "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people.)")

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