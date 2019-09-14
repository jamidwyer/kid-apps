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
            terms = ['rages over impeachement in ', 'taliban to camp david', 'Zillow that is being shown by a rat mascot', 'md court of appeals', 'baltimore insults', 'Laying Groundwork for Genocide', 'baltimore housing', 'trump says baltimore', 'kushner about baltimore', 'homes owned by jared kushner', 'long American history of denying racism', 'underestimate the depth of racism in America', 'baltimore and cummings', 'Obama shares tribute to Baltimore', 'cummings criticism', 'pretending his criticism of Baltimore has nothing to do with race', 'Better To Have A Few Rats Than To Be One', 'disgusting, rat and rodent infested mess', 'how little a lot of rich people care about the environment', '90yr old baltimore lady', 'dental care crisis', '18 migrant children under the age of 2 were separated from parents', 'students spray painted swastikas', 'bernie is the gold standard', 'generosity shower', 'ICE shows up at your door', 'transgender woman murdered in Washington suburb', 'elijah cummings', 'cummings threatens', 'contempt votes on barr', 'Do You Know Which Nations Own Your Data', 'fbi warned maryland', 'spelled podrick wrong', 'baltimore public school', 'small town is banning public comments at council meetings', 'md. house of delegates', 'paid federal public defender', 'Jamie Raskin', 'baltimore trolls', 'drug pricing control board', 'ad from trone', 'gov hogan', 'maryland election', 'capital gazette shooting', 'shooting at capital gazette', 'Annapolis Newsroom Shooting', 'call for shooting journalists', 'md primary', 'maryland candidate', 'ben jelous', 'maryland vote', 'Baltimore State\'s Attorney', 'bmoreceasefire', 'maryland green party', 'maryland senate', 'md. lawmakers', 'gerrymandering in maryland', 'benjealous', 'Maryland Single-Payer Bill', 'Baltimore cops kept toy guns', 'ben cardin', 'md-gov', 'gov. hogan', 'andy harris', 'ben jealous', 'larry hogan', 'maya for maryland', 'alec ross', 'maryland governor', 'MD\'s next governor ', 'governor of maryland', 'md gov', 'md governor\'s', 'Maryland governor’s race', 'md. governor', 'maryland gubernatorial candidate', 'Maryland workers need paid sick leave']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Maryland 2020 Election \n\n"
            "[Primary Election Registration Deadline](https://voterservices.elections.maryland.gov/OnlineVoterRegistration/VoterType): April 7, 2020 \n\n"
            "[Primary Election](https://voterservices.elections.maryland.gov/OnlineVoterRegistration/VoterType): April 28, 2020 \n\n"
            "[General Election Registration Deadline](https://voterservices.elections.maryland.gov/OnlineVoterRegistration/VoterType): October 13, 2020 \n\n"
            "[General Election](https://voterservices.elections.maryland.gov/OnlineVoterRegistration/VoterType): November 3, 2020 \n\n")
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