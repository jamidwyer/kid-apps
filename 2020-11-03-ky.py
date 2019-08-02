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

local_subs = open("kentucky.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['no pay, we stay', 'mitch mctreason', 'Protecting American elections from sabotage', 'billboard grabs attention on Interstate 65', 'armed and misogynist', 'moscow mitch', 'miners are fighting for the pensions', 'moscowmitch', 'Kentucky to Remove Up to 250,000 Inactive Voters', 'fuck mitch', 'the fucking turtle', 'in the Way of Federal Weed Legalization', 'bitch mitch', 'plan for avoiding debt default', 'Threatened, Beat, Tased, And Arrested A Man For Complaining About Being Beaten By him', 'kentucky coal', 'glasses to the homeless is against the law', 'kentucky is a top target', 'Louisville, Kentucky Metro Council', 'kentucky vot', 'trump over escalating tensions', 'Election security bills face GOP buzzsaw', 'war against free and fair elections', 'senate majority bitch', 'Bipartisan marijuana banking bill', 'russian investment in a kentucky', 'ky-sen', 'firefighting jobs with largest federal', 'lives are lost every day to our broken health care system', 'rep. yarmuth', 'kentucky ranks among worst states', 'toyota rebukes trump', '\"2019 Congressional District Census\"', 'remitcha', 'mcconnell']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Kentucky 2020 Election \n\n"
            "[Primary Election Registration Deadline](https://vrsws.sos.ky.gov/ovrweb/): April 20, 2020 \n\n"
            "[Primary Election](https://vrsws.sos.ky.gov/VIC/): May 19, 2020 \n\n"
            "[General Election Registration Deadline](https://vrsws.sos.ky.gov/ovrweb/): October 5, 2020 \n\n"
            "[General Election](https://vrsws.sos.ky.gov/VIC/): November 3, 2020 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write the post id back to the file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()
