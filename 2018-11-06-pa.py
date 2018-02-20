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

local_subs = open("pennsylvania.dat", "r")
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
            terms = ['New map for Pennsylvania', 'Pennsylvania after court issues new congressional district map', 'Pennsylvania Supreme Court releases new congressional map', 'Pennsylvania Supreme Court draws', 'Pennsylvania\'s Supreme Court Releases a New Congressional District Map', 'Pennsylvania House District', 'Court-Drawn Map in Pa.', 'Putting your vote over corporate profits', 'hal english', 'pennsylvania voting map', 'new Pennsylvania map', 'Pennsylvania Supreme Court just issued a new congressional map', 'Voters are supposed to pick their leaders. Not the other way around.', 'Maps Could Improve Democrats\' Chances in Pennsylvania', 'Pennsylvania Republicans Plan Another Lawsuit', 'Pennsylvania Governor Rejects GOP Gerrymander', 'Gov. Wolf rejects GOP map of congressional districts', 'pa. congressional map', 'Pennsylvania GOP responds to court order', 'Pennsylvania Republicans Are Trying to Replace One Gerrymander with Another', 'Supreme Court Delivers HUGE Blow To PA Gerrymandering', 'Pa. Republicans have proposed a brand new congressional map', 'any less Gerrymandered than the last one', 'turzai', 'Pennsylvania Proposes New Districts', 'Eight views of Pennsylvania', 'proposed Pennsylvania map has 13 Trump districts, 5 Clinton districts', 'Leaning benches at a bus stop in Pittsburgh', 'Pennsylvania congressional map', 'Map Proposed to Governor Tom Wolf', 'Pennsylvania will require voting machines', 'Pennsylvania to require voting machines', 'congressional map headed to Gov. Wolf', 'Pa. GOP to meet deadline in submitting new map', 'Pennsylvania GOP Lawmakers', 'Pennsylvania Republican launches effort', 'Pennsylvania GOP lawmaker', 'GOP breaks glass in Pennsylvania race', 'Donation From GOP Defendant In Gerrymandering Suit', 'Pennsylvania congressional redistricting', 'Pennsylvania Republicans Delay', 'pa redistricting', 'Eagles, Patriots are on opposite sides of political spectrum', 'Pennsylvania GOP leader tells state supreme court he will ignore it', 'Pennsylvania GOP leader says laws don\'t apply to GOP', 'Marijuana legalization cannot be stopped', 'Recreational Pot For Pennsylvania', 'Pennsylvania GOP\'s leading Senate candidate', 'Pa. governor', 'Coal Jobs Not Set to Increase in the Future', 'lou barletta', 'legalizing marijuana in PA', 'American democracy is failing', 'Vincent Hughes', 'GOP congressman says Obamacare made him sexually harass former aide', 'PA\'s 16th Congressional', 's gerrymandered House map was just struck down', 'new headquarters flip the presidential vote in a swing state', 'Women\'s March Philadelphia', 'on the parkway right now for the Women\'s March', 'Women\'s March on Philadelphia', 'Philly Women\'s March', 'GOP in Philly, suburbs, rocked by wave of legislative retirements', 'This is what the Democratic special election wave looks like', 'Adventures in Extreme Gerrymandering', 'Pennsylvania Could Be On The Verge Of Dealing Partisan Gerrymandering A Big Blow', 'Pennsylvania coal mine closes', 'stable genius act', 'Pa. coal power plant closing leads to', 'Pennsylvania Election Districts Give Republicans an Edge', 'be prepared for the worst\' in 2018', 'Trump is going to create more jobs for us!', 'Shutdown of coal-fired power plant results in significant fetal health improvement', 'Pennsylvania redistricting', 'After Big Wins This Election, Pittsburgh', 'pennsylvania state senate', 'Pennsylvania lawmaker calls fellow rep gay', '\'goofy\' gerrymandering', 'gerrymandering data top Pa. Republicans', 'letter directed to president Trump', 'pittsburghers Protest In Suppport Of Net Neutrality', 'rallying against the GOP tax scam in a Republican county in Pennsylvania', 'Bernie rally in Reading', 'smucker', 'pa-16', 'joe billie', 'pa-7', 'pa-07', '^(?!.*john meehan).*meehan.*$', 'pennsylvania gerrymandering', 'Vote for this guy if you live in PA', 'in PA, this guy is pretty good', 'ryan costello', 'Democrats back military veterans as candidates']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Pennsylvania 2018 Election \n\n"
            "[Primary Election Registration Deadline](https://www.pavoterservices.pa.gov/Pages/VoterRegistrationApplication.aspx): April 16, 2018 \n\n"
            "[Primary Election](https://www.pavoterservices.pa.gov/Pages/PollingPlaceInfo.aspx): May 15, 2018 \n\n"
            "[General Election Registration Deadline](https://www.pavoterservices.pa.gov/Pages/VoterRegistrationApplication.aspx): October 7, 2018 \n\n"
            "[General Election](https://www.pavoterservices.pa.gov/Pages/PollingPlaceInfo.aspx): November 6, 2018 \n\n")
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