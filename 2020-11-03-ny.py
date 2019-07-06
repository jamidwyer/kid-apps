#!/usr/bin/python
# coding: utf-8

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

local_subs = open("newyork.dat", "r")
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
            terms = ['Immigrant Workers Fired From President Trump', 'Baseball Team Trolls Pride Night Hater', 'bomb a Muslim community in New York state', 'officer luis alvarez', 'stonewall\'s first park ranger', 'How did this become our reality? We', 'new york city declares a climate emergency', 'protestors outside new york', 'planned ice raids', 'ICE shows up at your door', 'democratic shift in new york', 'e jean carroll', 'e. jean carroll', 'new york expands marijuana', 'marijuana use in new york', 'elle columnist accuses donald', 'james felton keith', 'labor charges against tesla buffalo', 'jon stewart goes off on congress', 'Marijuana Employment Policies', '11 victims fund', 'new york fundraiser', 'inmate found dead in rikers', 'new york, new jersey do the same', 'Father Fred Investigated for War Profiteering', 'I Honestly Don\'t Care\' If I\'m Breaking Federal Law', 'buttigieg says he will not repent', 'Trump falls short on infrastructure', 'injury to get out of military service', 'republican voters seem to love ', 'new york introduces new marijuana', 'kat brezler', 'new york attorney general', 'new york state\'s attorney general', 'new york city is creating jobs', 'knock down the house', 'knockdownthehouse', 'civil_ny keeping it real', 'new york legislat', 'sister retires to avoid fraud allegation', 'Protestors in NYC', 'No Blind People are Going to Live in Trump Tower', 'blake morris', 'new york repub', 'new york chapter of the proud boys', 'ny11', 'nyc bill passes', 'rally in Times Square', 'Democratic headquarters in Albany', 'opioid use in nyc', 'julia salazar', '^(?!.*aoch).*aoc.*$', 'bronx dsa', 'nyc public schoolteachers', 'yearning to breathe free', 'activists in new york', 'single payer new york health act', 'new york state assembly', 'taxi driver in debt', 'nadler', 'new york\'s housing crisis', 'preet bharara', 'marijuana charges in new york', 'zephyr', 'eric schneiderman', 'new york city dsa', 'new york state senat', 'new york senate', 'steve stern', 'new york may legaliz', 'trump tower fire', 'fire at trump tower', 'ny-24', 'n.y. passes bill', 'kurt schlickter', 'green party of new york', '9/11 first responders', 'tenney', 'NY State bill', 'ny-21', 'Billionaires Row', 'ny-19', 'Ocasio', 'ny19', 'new york lawmaker', 'ny27', 'New York City\'s fossil fuel divestment', 'New York City Declares War on the Oil Industry', 'new york cannabis', 'New York Finally Consider Legalizing Cannabis', 'sara idleman', 'peter king', 'katko', '^(?!.*burkina faso).*faso.*$', 'daniel donovan', 'dan donovan', 'ny-11', 'rep. donovan', 'rep donovan', 'representative donovan', 'congressman donovan', 'michael grimm', 'incumbent over Grimm']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post

        text = ("New York 2020 Election \n\n"
            "[Primary Election Party Affiliation Deadline](https://voterreg.dmv.ny.gov/MotorVoter/): February 28, 2020 \n\n"
            "[Primary Election Voter Registration Deadline](https://voterreg.dmv.ny.gov/MotorVoter/): April 3, 2020 \n\n"
            "[Primary Election](https://voterreg.dmv.ny.gov/MotorVoter/): April 28, 2020 \n\n"
            "[General Election Registration Deadline](https://voterlookup.elections.state.ny.us/votersearch.aspx): October 9, 2020 \n\n"
            "[General Election](https://voterlookup.elections.state.ny.us/votersearch.aspx): November 3, 2020")
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