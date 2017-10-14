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
    for submission in subreddit.hot(limit=200):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['fred upton', 'mi-06', 'mi-6', 'michigan\'s 6th District', 'rep. upton', 'rep upton', 'representative upton', 'congressman upton', 'benac']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://www.dmv.org/mi-michigan/voter-registration.php) by July 8, 2018 \n\n"
            "[**Paul Clements**](http://www.clementsforcongress.com/) is running to represent Michigan District 6. \n\n"
            "[Facebook](https://www.facebook.com/ClementsForCongress/) | "
            "[Twitter](https://twitter.com/Clem4Congress) | "
            "[Volunteer](http://www.clementsforcongress.com/volunteer/) | "
            "[Donate](https://secure.actblue.com/donate/fromcfcwebsite) \n\n"
            "Clements supports Medicare for all (HR 676), a living wage, public schools, affordable college, protecting Social Security, renewable energy, campaign finance reform, voting rights, LGBTQ equality, and net neutrality. \n\n\n"

            "[**Eponine Garrod**](http://garrod4thehouse.com/homepage/) is running to represent Michigan District 6. \n\n"
            "[Facebook](https://www.facebook.com/garrodforthehouse) | "
            "[Twitter](https://twitter.com/garrod4thehouse) | "
            "[Donate](https://secure.actblue.com/entity/fundraisers/50599) \n\n"
            "Garrod supports Medicare for all (HR 676), a living wage, public schools, renewable energy, LGBTQ equality, police body cameras, and legalizing marijuana. \n\n\n"

            "[**David Benac**](http://www.clementsforcongress.com/) is running to represent Michigan District 6. \n\n"
            "[Facebook](https://www.facebook.com/jeffforthethird) | "
            "[Twitter](https://twitter.com/David_Benac) | "
            "[Volunteer](https://benacforcongress.com/organize/) | "
            "[Donate](https://www.crowdpac.com/campaigns/235937/i-am-running-for-office-in-michigans-cd6-currently-held-by-fred-upton-with-medicare-for-all-as-one-of-my-core-issues-please-help-me-get-to-washington-dc-and-i-will-be-your-champion-for-health-care) \n\n"
            "Benac supports Medicare for all (HR 676), a living wage, protecting Social Security, affordable college, and voting rights. \n\n\n"

            "[Map of Michigan District 6](https://www.govtrack.us/congress/members/MI/6) \n\n"

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