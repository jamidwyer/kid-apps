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

local_subs = open("wisconsin.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=100):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['GOP could lose House and Senate in 2018', 'Bowed, Completely, to the Mad King', 'Democrats\' 2018 advantage expands', 'Last Attack on Indigenous Rights of 2017', 'The Republicans are stealing from you to give themselves a Christmas bonus', 'tax theft scam', 'Republican Candidate Goes Full Nazi', 'House has to revote on Tax Bill', 'Tax Bill Moves to Senate After House Passage Along Party Lines', 'House Republicans just passed their disastrous tax bill', 'wholesale looting of America', 'GOP Tax Scam', 'Public opposition to tax bill grows as vote approaches', 'Republican tax bill got worse', 'GOP want to maintain or increase funding for Medicaid, Medicare and Social Security', 'GOP Polling Shows Democrats Have 12-Point Advantage', 'Even R internal polling has D+12 on the generic ballot', 'earn homes, education, and a support in old age', 'world champion of extreme inequality', 'A Massive Class Warfare Attack', '10.4M in illegal contributions from Russians', 'No Country for Older Men and Women', 'Whatever happened to the \"WILL OF THE PEOPLE', 'funnel millions into GOP campaigns', 'Biggest Fake in American Politics', 'Republicans Despise the Working Class', 'support GOP tax bill', 'Republicans fret over tax bill', 'Republican moderate Susan Collins undecided on final tax cut vote', 'Fire Sale for Big Business', 'Republicans promote the myth that red low', '7.35 million from oligarch linked to Putin-Russia', 'Toxic Algae Blooms Spike In Wisconsin', 'GOP Angles for More Campaign Cash', 'Tax reform is a joke on the middle class', 'sharpen knives for retirement program cuts', 'Ryan says Republicans to target welfare, Medicare, Medicaid', 'Ryan called on Congress to target Medicare', 'matt flynn', 'ACA v. Tax Cuts and Jobs Act', 'tax cut for the wealthy in the name of economic growth', 'debt panic was a fraud', 'Biggest Tax Increase in American History, By Far', 'Sensenbrenner', 'randy bryce', 'Major Attack on Medicare', 'TFW you know that your party is trash and your president is trash', 'Tax Cut Bonanza Is a Major Attack on Medicare', 'Wisconsin gutted its unions', 'Gutting Wisconsin teachers unions hurt students, study finds', 'If you can hold it, you can shoot it', 'Voter Suppression Won Trump Wisconsin', 'GOP Resurrects Bill Exempting Rent', 'sensible center of American politics needs to step up', 'scott walker', 'governor walker', 'wisconsin governor', 'wi governor\'s', 'Wisconsin gubernatorial candidate', 'Wisconsin democratic governor candidate', 'Wisconsin vs Minnesota', 'Voter Suppression Handed Wisconsin to Trump', 'Voter Suppression Threw Wisconsin', 'Pass a tax overhaul, or else', 'The Kochs want that tax cut', 'kill Obamacare subsidies fuels calls to soften blow in Wisconsin', 'Vice President Pence implores Koch', 'Starting-Line Advantage of 10 Percent', 'Wisconsin Democratic candidates for governor', 'Gerrymandering Is Still About Race', 'How Much Gerrymandering Is Too Much', 'Gorsuch was a pompous bore', 'Ginsburg Slaps Gorsuch in Gerrymandering Case', 'Return Control of Our Elections to the People', 'Did district lines rig Wisconsin elections', 'Redistricting Case That Could Remake American Politics', 'skeptical of partisan gerrymandering', 'Wisconsin\'s partisan gerrymander', 'state voter ID law confusion', 'Deterred Voters in Wisconsin', 'Wisconsin Strict ID Law', 'Republican Governors Association', 'Republican Gov Association', 'paul ryan', 'rep. ryan', 'congressman ryan', 'rep ryan', 'speaker ryan', '@speakerryan', 'IronStache', 'Republican tax scam', 'Middle-Class Tax Hike', 'Wisconsin\'s First Congressional District', 'brad schimel']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Wisconsin 2018 Election \n\n"
            "[Primary Election Registration Deadline](https://myvote.wi.gov/en-us/registertovote): August 14, 2018 \n\n"
            "[Primary Election](https://myvote.wi.gov/en-us/FindMyPollingPlace): August 14, 2018 \n\n"
            "[General Election Registration Deadline](https://myvote.wi.gov/en-us/registertovote): November 6, 2018 \n\n"
            "[General Election](https://myvote.wi.gov/en-us/FindMyPollingPlace): November 6, 2018 \n\n")
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