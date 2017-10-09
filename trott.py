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

local_subs = open("michigan.dat", "r")
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
            terms = ['^(?!.*trotte).*trott.*$', 'Gerrymandering complaints lead to ballot campaign', 'frustrations may doom their majority', 'GOP worries as state Dems outperform in special elections', 'Mercurial Trump Rattles Republican Party Ahead of Midterms', '2018 as 3rd House Republican Says He', 'Michigan Republican congressman won\'t seek re-election', 'Congressional GOP Retirement Surge']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://www.dmv.org/mi-michigan/voter-registration.php) by July 8, 2018 \n\n"
            "[**Haley Stevens**](https://haleystevensforcongress.com/) is running to represent Michigan's 11th U.S. Congressional District. \n\n"
            "[Facebook](https://www.facebook.com/HaleyStevensForCongress/) | "
            "[Twitter](https://twitter.com/haleylive) | "
            "[Donate](https://secure.actblue.com/contribute/page/hs_website) \n\n"
            "Stevens supports single-payer health care, affordable college, and DACA. \n\n\n"

            "[**Fayrouz Saad**](https://www.fayrouzsaad.com/) is running to represent Michigan's 11th U.S. Congressional District. \n\n"
            "[Facebook](https://www.facebook.com/FayrouzSaadForCongress/) | "
            "[Twitter](https://twitter.com/saadforcongress) | "
            "[Donate](https://www.fayrouzsaad.com/contribute/) \n\n"
            "Saad supports public schools, paid family leave, equal pay for equal work, and DACA. \n\n\n"

            "[Map of Michigan District 11](https://www.govtrack.us/congress/members/MI/11) \n\n"

            "Primary Election: August 7, 2018 | General Election: November 6, 2018 \n\n"
            "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people.)"
            "[Find your polling place](https://webapps.sos.state.mi.us/MVIC/votersearch.aspx) \n\n")

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