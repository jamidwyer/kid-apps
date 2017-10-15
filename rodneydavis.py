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

local_subs = open("illinois.dat", "r")
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
            terms = ['rodney davis', 'davis\'s seat', 'All 6 Missouri Republicans in House vote against Trump']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://ova.elections.il.gov/Step0.aspx) by February 20, 2018 \n\n"
            "[Sign up to vote by mail](https://www.elections.il.gov/VotingInformation/VotingByMail.aspx) \n\n\n"

            "[**David Gill**](https://www.davidgill2018.com/platform) is running against Rodney Davis. \n\n"
            "[Facebook](https://www.facebook.com/DavidGill2018/) | "
            "[Twitter](https://twitter.com/davidgill2018) | "
            "[Volunteer](https://www.davidgill2018.com/get-involved) | "
            "[Donate](https://secure.actblue.com/contribute/page/doctorgillforcongress) \n\n"
            "Gill supports universal health care, public schools, living wages, affordable college, renewable energy, standing with our international allies, LGBTQ equality, and background checks on every gun sale. \n\n\n"

            "[**Jon Ebel**](http://www.jonebel.com/) is running against Rodney Davis. \n\n"
            "[Facebook](https://www.facebook.com/Friends-of-Jonathan-Ebel-229030640931027/) | "
            "[Twitter](https://twitter.com/jonathan_ebel) | "
            "[Volunteer](http://www.jonebel.com/get-involved/) | "
            "[Donate](https://contributions.jonebel.com/) \n\n"

            "[**Betsy Dirksen Londrigan**](http://www.betsydirksenlondrigan.com/) is running against Rodney Davis. \n\n"
            "[Facebook](https://www.facebook.com/BetsyDirksenLondrigan/) | "
            "[Twitter](https://twitter.com/BetsyforIL) | "
            "[Volunteer](http://betsydirksenlondrigan.com/index.php/volunteer) | "
            "[Donate](https://secure.actblue.com/donate/betsydirksenlondriganforillinois) \n\n"

            "[**Erik Jones**](https://erikjonesforcongress.com/) is running against Rodney Davis. \n\n"
            "[Facebook](https://www.facebook.com/ErikJones4IL/) | "
            "[Twitter](https://twitter.com/ErikJones4IL) | "
            "[Donate](https://secure.actblue.com/donate/erikjones) \n\n"

            "Primary Election: March 20, 2018 | General Election: November 6, 2018 \n\n"
            "[Map of Illinois District 13](https://www.govtrack.us/congress/members/IL/13) \n\n"

            "^(I'm a bot and I'm learning. Let me know if I can do better. It's a lot of "
            "work to add all this info, but if you prefer a different candidate, let me know, and I'll add them.)")
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