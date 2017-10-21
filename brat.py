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

local_subs = open("virginia.dat", "r")
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
            terms = ['dave brat', 'rep. brat', 'congressman brat', 'rep brat', 'representative brat', 'Conservatives drop demands for bigger spending cuts to get to tax reform', 'GOP Congressmen Call For Mueller Hearings', 'Republicans in Congress Cheered', 'Freedom Caucus endorses GOP tax plan']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://vote.elections.virginia.gov/Registration/Eligibility) by October 15, 2018. \n\n"
            "[**Eileen Bedell**](https://www.bedellforvirginia.com/issues) is running against Dave Brat. \n\n"
            "[Donate](https://secure.actblue.com/contribute/page/bedell-for-virginia--inc-1) | "
            "[Facebook](https://www.facebook.com/EileenBedellforVirginia/) | "
            "[Twitter](https://twitter.com/BedellforVA) \n\n"

            "Bedell supports universal health care, renewable energy, living wages, and LGBTQ equality.  \n\n"

            "[**Abigail Spanberger**](https://abigailspanberger.com/) is running against Dave Brat. \n\n"
            "[Donate](https://secure.actblue.com/donate/spanberger_website) | "
            "[Facebook](https://www.facebook.com/SpanbergerForCongress/) | "
            "[Twitter](https://twitter.com/SpanbergerVA07) \n\n"

            "Spanberger supports public schools, funding the State Department to promote international diplomacy, and net neutrality.  \n\n"

            "Primary Election: June 12, 2018 | General Election: November 6, 2018 \n\n"
            "[Map of Virginia District 7](https://www.govtrack.us/congress/members/VA/7) \n\n"
            "[Find your polling place](http://www.elections.virginia.gov/voter-outreach/where-to-vote.html) \n\n"

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