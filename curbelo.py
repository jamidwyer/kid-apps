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

local_subs = open("florida.dat", "r")
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
            terms = ['curbelo', 'congressional GOP helped Trump keep tax returns secret', 'Congress gives Trump a pass on releasing his tax returns', 'Republicans vote against forcing Trump to release tax returns', 'Congress gives Trump pass on his tax returns']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://dos.myflorida.com/elections/for-voters/voter-registration/register-to-vote-or-update-your-information/) by July 30, 2018 \n\n"
            "[Sign up to vote by mail](http://dos.myflorida.com/elections/for-voters/voting/absentee-voting/) \n\n\n"

            "[**Steven Machat**](http://machat2018.com/issues/) is running against Carlos Curbelo. \n\n"
            "[Facebook](https://www.facebook.com/stevenmachat) | "
            "[Twitter](https://twitter.com/machat2018) | "
            "[Volunteer](http://machat2018.com/volunteer/) | "
            "[Donate](https://secure.actblue.com/donate/machat) \n\n "
            "Machat supports Medicare for All (HR 676), public schools, affordable college, living wages, protecting Social Security, affordable housing, equal pay for equal work, renewable energy, campaign finance reform, LGBTQ equality, and DACA. \n\n\n"

            "[**Debbie Mucarsel-Powell**](https://debbiemucarselpowell.com/) is running against Carlos Curbelo. \n\n"
            "[Facebook](https://www.facebook.com/debbieforfl/) | "
            "[Twitter](https://twitter.com/debbieforfl) | "
            "[Volunteer](https://debbiemucarselpowell.com/) | "
            "[Donate](https://secure.actblue.com/donate/debbiemucarselpowell) \n\n"
            "Mucarsel-Powell supports universal health care, living wages, affordable college, renewable energy, and DACA. \n\n\n\n"

            "Primary Election: August 28, 2018 | General Election: November 6, 2018 \n\n"
            "[Map of Florida District 26](https://www.govtrack.us/congress/members/FL/26) \n\n"

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