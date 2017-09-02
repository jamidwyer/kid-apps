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

local_subs = open("texas.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top 500 values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=200):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['john culberson', 'rep. culberson', '@congculberson', 'congressman culberson', 'rep culberson', 'Culberson is screwing us over']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post

        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://www.votetexas.gov/register-to-vote/) \n\n"
        "[**Jason Westin**](https://westinforcongress.com/) is running against John Culberson. \n\n"
        "[Donate](https://secure.actblue.com/contribute/page/nbijw2017) | "
        "[Facebook](https://www.facebook.com/WestinForCongress) | "
        "[Twitter](https://twitter.com/DrWestinForTX07) \n\n"

        "Westin supports single-payer health care, public schools, universal pre-K, equal pay for equal work, renewable energy, LGBTQ equality, voting rights, and funding science.  \n\n\n"

        "[**Alex Triantaphyllis**](http://www.alextfortexas.com/index.html) is running against John Culberson. \n\n"
        "[Donate](https://secure.actblue.com/contribute/page/alexthomepage) | "
        "[Facebook](https://www.facebook.com/AlexTforTexas/) | "
        "[Twitter](https://twitter.com/AlexTforTexas) \n\n"

         "Triantaphyllis supports renewable energy, public schools and protecting Social Security and Medicare. \n\n\n"

        "[**James Cargas**](http://www.jamescargas.com/on-the-issues/) is running against John Culberson. \n\n"
        "[Donate](https://secure.actblue.com/contribute/page/james-cargas-1) | "
        "[Facebook](https://www.facebook.com/Cargas7/) | "
        "[Twitter](https://twitter.com/Cargas7) \n\n"

         "Cargas supports public schools, affordable college, universal pre-K, renewable energy, LGBTQ equality, background checks on every gun sale, voting rights, and funding science. \n\n\n"

        "[**Laura Moser**](https://moserforcongress.com/) is running against John Culberson. \n\n"
        "[Donate](https://secure.actblue.com/contribute/page/moser_website) | "
        "[Facebook](https://www.facebook.com/lauramosertx) | "
        "[Twitter](https://twitter.com/@lcmoser) \n\n\n"

        "[Map of Texas District 7](https://www.govtrack.us/congress/members/TX/7) \n\n "

        "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people instead of billionaire political donors.)")


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