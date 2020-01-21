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
            terms = [
                'ny-11', \
                'ny-19', 'ny19', \
                'ny-21', \
                'ny27', \
                'Ocasio', \
                'peter king', \
                'katko', \
                '^(?!.*burkina faso).*faso.*$', \
                'daniel donovan', 'dan donovan', \
                'rep. donovan', 'rep donovan', 'representative donovan', 'congressman donovan', \
                'michael grimm'
                'sara idleman', \
                'you know how women drive', \
                'surveillance video from jeffrey epstein', \
                'manhattan luxury-condo', \
                'kolb was twice the legal', \
                'ny republican', \
                'bone spurs', \
                'evelyn yang', \
                'new york to rally', \
                'House member from western New York', \
                'skyscrapers are empty', \
                'evelyn shared her story', \
                'sdny', 'trump is copying hitler', \
                'trump tower kept 2 sets of books', 'trump kept 2 sets of books', 'apartment hunting in nyc', \
                'ties soleimani to 9', \
                'mta kiosk', 'tax cut was a scam', 'bernie speaking in queens', 'berniesback', 'new york endors', \
                'new york cannabis', 'new york proposes a cannabis', 'tax documents show trump', \
                'trump tax documents', 'stealing from a charity', 'demanding to meet his accuser', \
                'collins resignation', 'rep. chris collins', 'new york banned fracking', 'hogging all the selfies', \
                'house judiciary chief', 'climate strike in nyc', 'new york climate protest', \
                'de blasio ends campaign', 'de blasio pulls the plug', 'billdeblasio', 'climate strike nyc', \
                'selfie line in new york city', 'first look at the crowd in NYC', \
                'Fighting Corruption A Feminist Rallying Cry', 'new york rally', 'donor who owns an all-woman woodworking company', 'Sit-in at Microsoft Store in Manhattan', 'giuliani', 'beto in rockaway', 'NY eliminated religious exemptions', 'even the haters and losers', 'Trump claiming he helped look for survivors', 'Trump backlash in suburbs', 'ny officially decriminalize', 'new yorkers to see their marijuana', 'blocking funding for first responders', 'declares millions of us jews', 'not trying to appeal to jewish voters', 'models for donald trump', 'coverage of his racism', 'Temporary Lifting of the Statute of Limitations on Sex Abuse Cases', 'Trump Tower Named After Obama', 'Donation Map from The NY Times', 'the highway was supposed to save this city', 'new york post names beto', 'richly deserves impeachment', 'new york blackout', 'did not clear trump', 'future of the city is childless', 'governor cuomo', 'House rejects Saudi weapons sales', 'House blocks arms sales to Saudi', 'tweets are a distraction for something else', 'eric gardner', 'reports that she violated immigration laws', 'climate apartheid', 'alex acosta', 'sanders took a walk down wall street', 'pizzagate was real', 'symbol of plutocratic rot', 'donald trump raped a 13', 'trump admitting he', 'Sworn deposition by a 13 year old', 'joey salads', 'Immigrant Workers Fired From President Trump', 'Baseball Team Trolls Pride Night Hater', 'bomb a Muslim community in New York state', 'officer luis alvarez', 'stonewall\'s first park ranger', 'How did this become our reality? We', 'new york city declares a climate emergency', 'protestors outside new york', 'planned ice raids', 'ICE shows up at your door', 'democratic shift in new york', 'e jean carroll', 'e. jean carroll', 'new york expands marijuana', 'marijuana use in new york', 'elle columnist accuses donald', 'james felton keith', 'labor charges against tesla buffalo', 'jon stewart goes off on congress', 'Marijuana Employment Policies', '11 victims fund', 'new york fundraiser', 'inmate found dead in rikers', 'new york, new jersey do the same', 'Father Fred Investigated for War Profiteering', 'anthony brindisi', 'I Honestly Don\'t Care\' If I\'m Breaking Federal Law', 'buttigieg says he will not repent', 'Trump falls short on infrastructure', 'injury to get out of military service', \
                'republican voters seem to love ', 'new york introduces new marijuana', 'kat brezler', 'new york attorney general', 'new york state\'s attorney general', 'new york city is creating jobs', 'knock down the house', 'knockdownthehouse', 'civil_ny keeping it real', 'new york legislat', 'sister retires to avoid fraud allegation', 'Protestors in NYC', 'No Blind People are Going to Live in Trump Tower', 'blake morris', \
                'new york repub', 'new york chapter of the proud boys', 'ny11', 'nyc bill passes', 'rally in Times Square', \
                'new york bans', 'Democratic headquarters in Albany', 'opioid use in nyc', 'julia salazar', \
                '^(?!.*aoch).*aoc.*$', 'bronx dsa', 'nyc public schoolteachers', 'yearning to breathe free', \
                'activists in new york', 'single payer new york health act', 'new york state assembly', \
                'taxi driver in debt', 'nadler', 'new york\'s housing crisis', 'preet bharara', 'marijuana charges in new york', 'eric schneiderman', 'new york city dsa', 'new york state senat', 'new york senate', 'steve stern', 'new york may legaliz', 'trump tower fire', 'fire at trump tower', 'ny-24', 'n.y. passes bill', 'kurt schlickter', 'green party of new york', '9/11 first responders', \
                'tenney', \
                'NY State bill', \
                'Billionaires Row', \
                'new york lawmaker', \
                'New York City\'s fossil fuel divestment'
            ]
            for term in terms:
                 search(term, submission)

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post

        text = ("New York 2020 Election \n\n"
            "[Primary Election Party Affiliation Deadline](https://voterreg.dmv.ny.gov/MotorVoter/): February 14, 2020 \n\n"
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