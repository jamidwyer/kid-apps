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

local_subs = open("california.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.selftext)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['andrew janz', 'Energized Battle Ahead in California', 'Republicans are selling out everything to protect their Dear Leader', 'Republican coverup on Trump and Russia', 'In states where marijuana is legal, entrepreneurs should be able to access the same banking services', 'polling looks extremely good for Democrats ', 'All California Republicans Are At Risk', 'Proposition 13 and what to do about it', 'The GOP Are Aiding and Abetting', 'Democrats need only one thing to win', 'Activist Who Confronted Caitlyn Jenner', 'Californians will vote by mail', 'vicious attack in Congress by anti-conservation zealots', 'ca-45', 'duncan hunter', 'rep. hunter', 'congressman hunter', 'rep hunter', 'ca-50', 'Can The Dems Take The House in 2018', 'We have to end the use of private prisons in the United States', 'Rackauckas', 'todd spitzer', 'orange county da ', 'orange county d.a.', 'orange county district attorney', 'gerrymandering, political reform, and saving democracy', 'A Serial Killer In Orange County', 'restorative justice for all those who had their lives destroyed', 'Southern California wildfire now largest in state history', 'with a Pen, 5 Seconds After Exiting His Patrol Car', 'progressive renaissance of 2018', 'CASEN 2018', 'Plot To Use Classified Information To Discredit', 'expansion of mass surveillance', 'polling results for 36 districts', 'Democrats Are Pulling Away in the Generic Ballot', 'NSA Expansion Bill', 'Ballot average gives Democrats highest advantage yet', 'Thomas Fire is on track to become the largest', 'Trump predicts Republicans will do', 'deny global warming all he wants, but the price can', 'full rights are restored to every American who spent time in jail for marijuana', 'we can do it in cd4', 'Coroner resigns due to sheriff interference', 'A Deep Vein of Poverty Runs Through the U.S.', 'mimi walters', 'Kia Hamadanchy', 'Putin Is Not Omnipotent', 'Climate change is part of California', 'congressional districts to target for 2018', 'much closer districts than the Alabama Senate Seat', 'Climate Change Has Come for Los Angeles', 'exacerbate California droughts', 'devin nunez', 'Orange County Alt-Right', 'devin nunes', 'rep. nunes', 'congressman nunes', 'House Intel chief', 'Nunes Subpoenaed', 'House intel Democrat on Russia probe', 'rep nunes', 'darrell issa', 'rep. issa', 'rep issa', 'the california gop\'s last gasp', 'rohrabacher', 'michael kotick', '@danarohrabacher', 'rohrabracher', 'Transcript of McCarthy', 'pro-assange gop congressman', 'pro-putin california congressman', 'Pro-Russia GOP Rep.', 'Putin\'s congressman', 'rhorabacher', 'steve knight', 'rep. knight', 'congressman knight', 'rep knight', 'representative knight', 'ca-25', 'valadao']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("California 2018 Election \n\n"
            "[Primary Election Registration Deadline](http://registertovote.ca.gov/): May 16, 2018 \n\n"
            "[Primary Election](http://www.sos.ca.gov/elections/voter-registration/vote-mail/#apply): June 5, 2018 \n\n"
            "[General Election Registration Deadline](http://registertovote.ca.gov/): October 22, 2018 \n\n"
            "[General Election](http://www.sos.ca.gov/elections/voter-registration/vote-mail/#apply): November 6, 2018 \n\n")
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