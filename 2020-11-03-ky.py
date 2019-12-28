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
            terms = [
                'beshear', \
                'matt bevin', \
                'ky-06', \
                'congressman andy barr', \
                'kentucky will accept', 'trump tax cuts', 'trump impeached', \
                'kentucky lieutenant governor', 'turtle faced traitor', 'drinking water across kentucky', \
                'congress silently killed', \
                'kentucky democrat', 'kentucky outcome', 'rally in kentucky', 'poor ky. county', 'kentucky mill shut', 'u.s. deficit', 'flip the senate', 'kentucky capitol', 'cut taxes for rich people', 'minimum wage bill has all but died in the Senate', 'ky gun violence', 'massacremitch', 'secure the 2020 elections', 'american mitch', 'amy mcgrath', 'no pay, we stay', 'mitch mctreason', 'armed and misogynist', 'kentucky miner', 'moscow mitch', 'moscowmitch', 'kentucky teachers', 'fuck you, mitch', 'fuck mitch', 'the fucking turtle', 'in the Way of Federal Weed Legalization', 'bitch mitch', 'kentucky coal', 'kentucky is a top target', 'Louisville, Kentucky Metro Council', 'kentucky vot', 'kentucky gop', 'war against free and fair elections', 'senate majority bitch', 'Bipartisan marijuana banking bill', 'russian investment in a kentucky', 'ky-sen', 'firefighting jobs with largest federal', 'lives are lost every day to our broken health care system', 'rep. yarmuth', 'kentucky ranks among worst states', 'toyota rebukes trump', '\"2019 Congressional District Census\"', 'remitcha', 'mcconnell']
            for term in terms:
                 search(term, submission)

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Kentucky 2020 Election \n\n"
            "[Primary Election Party Affiliation Deadline](https://vrsws.sos.ky.gov/ovrweb/default): December 31, 2019 \n\n"
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
     searchAndPost(sub)

text_file.close()
local_subs.close()
