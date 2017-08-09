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

local_subs = open("alabama.dat", "r")
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
            terms = ['luther strange', 'sen. strange', 'senator strange', 'special election in alabama', 'alabama special election', 'alabama senate race', 'no strange']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://www.alabamainteractive.org/sos/voter_registration/voterRegistrationWelcome.action) \n\n"
            "[**Will Boyd**](http://willboydforcongress.com/) is running against Luther Strange. \n\n "
            "[Donate](https://www.paypal.com/donate/?token=eJ3NLueUO7muzRmyxdxsUyuVSYU95UJYcCy75iWFxDw0TtnkRKcKN-VciFQn10rGB9xJQm&country.x=US&locale.x=US) | "
            "[Facebook](https://www.facebook.com/wboyd4senate) | "
            "[Twitter](https://twitter.com/wboyd4senate) \n\n "

            "Boyd supports universal health care, public schools, living wages, protecting Social Security and Medicare, affordable college, equal pay for equal work, renewable energy, and LGBTQ equality.  \n\n "

            "[**Doug Jones**](http://dougjonesforsenate.com/) is running against Luther Strange. \n\n "
            "[Donate](https://secure.actblue.com/donate/homepage-donate) | "
            "[Facebook](https://www.facebook.com/dougjonessenate) \n\n "

            "Jones supports universal health care, public schools, living wages, protecting Medicare, equal pay for equal work, and renewable energy.  \n\n "

            "[**Michael Hansen**](http://www.hansenforalabama.com/) is running against Luther Strange. \n\n "
            "[Donate](https://hansenforalabama.nationbuilder.com/donate) | "
            "[Facebook](https://www.facebook.com/hansenforalabama/) | "
            "[Twitter](https://twitter.com/Hansen4Alabama) \n\n "

            "Hansen supports universal health care, public schools, living wages, affordable college, renewable energy, and LGBTQ equality.  \n\n "

            "[**Jason Fisher**](https://fisherforsenate.com/) is running against Luther Strange. \n\n "
            "[Donate](https://secure.actblue.com/contribute/page/jasonfisher) | "
            "[Facebook](https://www.facebook.com/FisherforSenateAL/) | "
            "[Twitter](https://twitter.com/fisher4senate) \n\n "

            "Fisher supports renewable energy, public schools, LGBTQ equality, and equal pay for equal work.  \n\n "

            "[**Robert Kennedy, Jr.**](http://www.teamkennedy2017.org/) is running against Luther Strange. \n\n "
            "[Donate](https://secure.actblue.com/donate/rkjr2017) | "
            "[Facebook](https://www.facebook.com/BobbyK4Senate) | "
            "[Twitter](https://twitter.com/BobbyK4Senate) \n\n "

            "Kennedy supports public schools, and protecting voting rights.  \n\n "

            "^(I'm a bot and I'm learning. Let me know how I can do better.)")
        submission.reply(text)
        print("Bot replying to : ", submission.title)

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