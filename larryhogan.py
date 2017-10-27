# coding: utf-8
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

local_subs = open("maryland.dat", "r")
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
            terms = ['larry hogan', 'kamenetz', 'alec ross', 'maryland governor', 'MD\'s next governor ', 'governor of maryland', 'md gov', 'md governor\'s', 'Maryland governor’s race', 'md. governor', 'maryland gubernatorial candidate', 'DSA candidates and Justice Democrats running in these 2018 primaries', 'Only two African Americans have been elected governor', 'Maryland workers need paid sick leave']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://voterservices.elections.maryland.gov/OnlineVoterRegistration/VoterType) by June 5, 2018 \n\n"
            "[Sign up to vote by mail](https://voterservices.elections.maryland.gov/OnlineVoterRegistration/InstructionsStep1) \n\n\n"

            "[**Ben Jealous**](https://benjealous.com/) is running to be Governor of Maryland. \n\n"
            "[Volunteer](https://benjealous.com/) | "
            "[Donate](https://secure.actblue.com/donate/bj1706) | "
            "[Reddit](https://www.reddit.com/r/BenJealous/) | "
            "[Facebook](https://www.facebook.com/benjealous/) | "
            "[Twitter](https://twitter.com/BenJealous) \n\n"
            "Jealous supports single-payer health care, renewable energy, LGBTQ equality, and the DREAM Act. \n\n"

            "[**Rich Madaleno**](http://www.madalenoformaryland.com/our-issues/) is running to be Governor of Maryland. \n\n"
            "[Volunteer](http://www.madalenoformaryland.com/) | "
            "[Donate](https://secure.actblue.com/donate/jim-shea-for-maryland-1) | "
            "[Facebook](https://www.facebook.com/richardmadaleno/) | "
            "[Twitter](https://twitter.com/richmadaleno) \n\n"
            "Madaleno supports universal health care with a public option, public schools, affordable college, a living wage, renewable energy, and LGBTQ equality. \n\n"

            "[**Alec Ross**](https://alecross.com/) is running to be Governor of Maryland. \n\n"
            "[Volunteer](https://alecross.com/) | "
            "[Donate](https://act.alecross.com/page/contribute/default) | "
            "[Facebook](https://www.facebook.com/Alec4MD/) | "
            "[Twitter](https://twitter.com/alecjross) \n\n"
            "Ross supports universal health care with a public option, public schools, childcare assistance, voting by mail, automatic voter registration, and redistricting reform. \n\n"

            "[**Jim Shea**](https://www.jimshea.com/) is running to be Governor of Maryland. \n\n"
            "[Volunteer](https://www.jimshea.com/get-involved) | "
            "[Donate](https://secure.actblue.com/donate/jim-shea-for-maryland-1) | "
            "[Facebook](https://www.facebook.com/sheaforMD/) | "
            "[Twitter](https://twitter.com/sheaformd) \n\n"
            "Shea supports universal health care, public schools, affordable college, renewable energy, and LGBTQ equality. \n\n"

            "[**Maya Rockeymoore Cummings**](https://mayaformaryland.com/) is running to be Governor of Maryland. \n\n"
            "[Volunteer](https://mayaformaryland.com/) | "
            "[Donate](https://secure.actblue.com/donate/maya-rockeymoore-cummings-for-maryland-1) | "
            "[Facebook](https://www.facebook.com/MayaForMaryland/) | "
            "[Twitter](https://twitter.com/MayaForMaryland) \n\n"
            "Rockeymoore Cummings supports universal health care and paid sick leave. \n\n"

            "[**Rushern Baker**](http://www.rushernbaker.com/) is running to be Governor of Maryland. \n\n"
            "[Volunteer](https://rushern.bsd.net/page/s/volunteer-with-rushern) | "
            "[Donate](https://secure.actblue.com/donate/rb-home) | "
            "[Facebook](https://www.facebook.com/RushernLBaker/) | "
            "[Twitter](https://twitter.com/rushernbaker) \n\n"
            "Baker supports universal health care, public schools, affordable college, renewable energy, and LGBTQ equality. \n\n"

            "[**Kevin Kamenetz**](http://krishformaryland.com/) is running to be Governor of Maryland. \n\n"
            "[Volunteer](https://act.myngp.com/Forms/-7197369037305476352) | "
            "[Donate](https://act.myngp.com/Forms/-7701772195570971904) | "
            "[Facebook](https://www.facebook.com/KevinKamenetz/) | "
            "[Twitter](https://twitter.com/kevinkamenetz) \n\n"
            "Kamenetz supports renewable energy and public schools. \n\n"

            "[**Krishanti Vignarajah**](http://krishformaryland.com/) is running to be Governor of Maryland. \n\n"
            "[Volunteer](http://krishformaryland.com/volunteer/) | "
            "[Donate](https://www.crowdpac.com/campaigns/323377/krish-for-maryland) | "
            "[Facebook](https://www.facebook.com/krishformaryland) | "
            "[Twitter](https://twitter.com/KrishForMD) \n\n"

            "Primary Election: June 26, 2018 | General Election: November 6, 2018 \n\n"
            "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will vote in the interests of working-class people.)")

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