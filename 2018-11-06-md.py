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

local_subs = open("maryland.dat", "r")
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
            terms = ['Housing and transportation are LGBTQ issues', 'benjealous', 'Maryland Single-Payer Bill', 'Pot legalization could be on November ballot', 'Baltimore cops kept toy guns', 'ben cardin', 'Years of Underinvestment in Urban Schools', 'chelsea manning', 'Legalizing Marijuana reduces violent crime and murder', 'Maryland House Votes To Override', 'md-gov', 'Hogan Proposes Term Limits', 'gov. hogan', 'Medicare for All will be a big win for Maryland', 's main newspaper, front page.', 'seats in Anne Arundel County', 'Baltimore Students Offer Solutions', 'second partisan gerrymandering case', 'second gerrymandering case', 's third congressional district', 'andy harris', 'Russian ads placed in Maryland', 'ben jealous', 'larry hogan', 'maya for maryland', 'kamenetz', 'alec ross', 'maryland governor', 'MD\'s next governor ', 'governor of maryland', 'md gov', 'md governor\'s', 'Maryland governor’s race', 'md. governor', 'maryland gubernatorial candidate', '9 Democratic primaries to watch in 2018', 'DSA candidates and Justice Democrats running in these 2018 primaries', 'Only two African Americans have been elected governor', 'Maryland workers need paid sick leave']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Maryland 2018 Election \n\n"
            "[Primary Election Registration Deadline](https://voterservices.elections.maryland.gov/OnlineVoterRegistration/VoterType): June 5, 2018 \n\n"
            "[Primary Election](https://voterservices.elections.maryland.gov/OnlineVoterRegistration/InstructionsStep1): June 26, 2018 \n\n"
            "[General Election Registration Deadline](https://voterservices.elections.maryland.gov/OnlineVoterRegistration/VoterType): October 16, 2018 \n\n"
            "[General Election](https://voterservices.elections.maryland.gov/OnlineVoterRegistration/InstructionsStep1): November 6, 2018 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write our updated list back to the file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()