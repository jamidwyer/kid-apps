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

local_subs = open("newjersey.dat", "r")
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
            terms = ['chris christie', 'guadagno', 'new jersey governor', 'NJ\'s next governor ', 'governor of new jersey', 'nj gov', 'nj governor\'s', 'close governor\'s beach house during shutdowns', 'christie\'s secret attorney fee']
            for term in terms:
                include_green = 1
                if subreddit == "bluemidterm2018":
                    include_green = 0

                    search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        vote_link = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://www.state.nj.us/state/elections/voting-information.html) \n\n")

        green = ""

        if include_green:
            green = ("[**Seth Kaper-Dale**](https://www.kaperdaleforgovernor.com/) is running to be Governor of New Jersey. \n\n"
                "[Donate](https://www.kaperdaleforgovernor.com/donate/) | "
                "[Reddit](https://www.reddit.com/r/SethKaperDale/) | "
                "[Facebook](https://www.facebook.com/kaperdaleforgovernor) | "
                "[Twitter](https://twitter.com/KaperDaleForGov) \n\n"
                "Kaper-Dale supports single payer Medicare for all, renewable energy, public schools, living wages, paid sick leave, affordable college, equal pay for equal work, and LGBTQ equality. \n\n\n")

        dems = ("[**Phil Murphy**](https://www.murphy4nj.com/issues) is running to be Governor of New Jersey. \n\n"
            "[Donate](https://act.myngp.com/Forms/2599649002085616384) | "
            "[Facebook](https://www.facebook.com/PhilMurphyNJ) | "
            "[Twitter](https://twitter.com/PhilMurphyNJ) \n\n"
            "Murphy supports renewable energy, public schools, living wages, paid sick leave, affordable college, equal pay for equal work, LGBTQ equality, and background checks on all gun sales. \n\n\n")

        disclaimer = ("^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people instead of billionaire political donors.)")

        text = '\n'.join([vote_link, green, dems, disclaimer])

        print("Bot replying to : ", submission.title)
        submission.reply(text)

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