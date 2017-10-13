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

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://ova.elections.il.gov/Step0.aspx) by February 20, 2018 \n\n"
            "[Sign up to vote by mail](https://www.elections.il.gov/VotingInformation/VotingByMail.aspx) \n\n\n"

            "[**Ryan Huffman**](http://www.huffmanforcongress.com/) is running against Peter Roskam. \n\n"
            "[Facebook](https://www.facebook.com/HuffmanForIL6/) | "
            "[Twitter](https://twitter.com/HuffmanForIL6) \n\n"
            "[Volunteer](http://www.huffmanforcongress.com/volunteer.html) | "
            "[Donate](https://secure.actblue.com/donate/ryanhuffman) | "
            "Huffman supports Medicare for all, public schools, affordable college, living wages, paid family leave, equal pay for equal work, renewable energy, campaign finance reform, LGBTQ equality, DACA, and background checks on every gun sale.\n\n"

            "[**Kelly Mazeski**](http://www.kellymazeski.com/) is running against Peter Roskam. \n\n"
            "[Facebook](https://www.facebook.com/kellymazeskiforcongress/) | "
            "[Twitter](https://twitter.com/KellyMazeski) \n\n"
            "[Volunteer](https://www.kellymazeski.com/get-involved/) | "
            "[Donate](https://secure.actblue.com/contribute/page/kelly-mazeski-website) | "
            "Mazeski supports universal health care, public schools, affordable college, living wages, paid family leave, protecting Social Security, equal pay for equal work, renewable energy, and DACA.\n\n"

            "[**Amanda Howland**](http://www.amandahowlandforcongress.com/) is running against Peter Roskam. \n\n"
            "[Facebook](https://www.facebook.com/howlandforcongress) | "
            "[Twitter](https://twitter.com/amandahowland06) \n\n"
            "Howland supports single-payer health care, renewable energy, the Paris Climate Agreement,"
             "and affordable college.\n\n"

            "Primary Election: March 20, 2018 | General Election: November 6, 2018 \n\n"
            "[Map of Illinois District 6](https://www.govtrack.us/congress/members/IL/6) \n\n "

            "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people instead of billionaire political donors.)")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Store the current id into our list
        posts_replied_to.append(submission.id)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['roskam', 'il-6', 'il-06', 'Suburban Chicago Republican congressmen back Trump', 'Tax Plan Cuts Rates for Individuals and Corporations and Eliminates Many Deductions', 'House GOP Worries About', 'GOP outraged after Trump refuses to consider Lois Lerner prosecution', 'GOP request to reopen case against former IRS official Lois Lerner']
            for term in terms:
                 search(term, submission);

for sub in subs:
     print(sub)
     searchAndPost(sub);

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

text_file.close()
local_subs.close()