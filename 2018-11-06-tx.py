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

local_subs = open("texas.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['Democrats introduce resolution to reverse FCC net neutrality repeal', 'Texas Democrats are so excited to vote', 'Texas is no longer Solid Republican', 'Texas establishment GOP scared', 'keep voting, texans', 'generic congressional ballot is back on double digits', 'The Primary Election Is the Real Election', 'Democrats up 54-38 on generic ballot', 'Democrats trying to regain a foothold in Texas', 'The Left is Energized. Now It Needs to Vote.', '2013 addressing media outside of the Senate after senators refused to pass a bipartisan gun control measure', 'stomps Cruz', 'UT Tower Shooting', 'activism across Texas', '400 Anderson High students walk out', 'candidates increase across Texas', 'early voting records at start of Texas primaries', 'Texans turn out in force on first day of early voting', 'North Texas school is getting a police station', 's keep it going, Texas', 'millions into Texas races', 'Democratic turnout in Texas', 'Sanders to make stops in Austin, San Antonio', 'Protesting, FUCKING DO IT ANYWAY', 'Democrats in Texas are exceptional', 'thomas dillingham', 'Gov. Abbott', 'Superintendent Curtis Rhodes', 'blue texas', 'need to win texas', 'Thousands vote in Harris County', 'Dem early voting up 300', '300-percent surge in early voting', 'Texas And Arizona Elections Start NOW', 'Texas Republicans getting almost 90 percent of money', '538 Generic congressional ballot average shows a recovery', 'Democrats up 15 on generic ballot', 'Progressive Voter Guide', 'mike collier', 'Texas Democrat Writes Giant-Killer Narrative', 'Early Voting Poll map. Sorry for the convenience.', ' but the attacks keep happening', 'tx votes', 'Cruz approval underwater', 'Conservative Californians are moving to Texas', 'Texas Dem Senate Candidate', 'texas gubernatorial', 'texas redistricting', 'Flip a Red District in Texas', 'Texas goes Democratic', 'rick trevino', '2018 Primaries for Texas', 'will hurd', 'participate in the March 6th primary', '2018 Texas primaries', 'Texas\' Next Senator', 'Texas congressional races', 'Texas 3rd Congressional District', 'texas voters', 'Texans, get ready to vote', 'cruz vs. o', 'saari', 'vote for beto', 'House Republicans in Texas', 'dan patrick', 'derrick crowe', 'TX district judge', 'sam johnson', 'colin allred', 'Texas Justice Democrat', 'tx-32', 'tx-16', 'March scheduled for Saturday, Jan. 20, in downtown Austin', 'Most Powerful Political Office: Lieutenant Governor', 'Senate Passes Warrantless Spying Reauthorization Bill', 'Congress demanded NSA spying reform', 'legal medical marijuana decreased drug crime in US states', 'rep. dukes', 'Boost Turnout In GOP Primaries', 'I believe the impossible is possible', 'primaries start in mere WEEKS', '65 just voted to expand NSA spying', '256 representatives that just voted to reauthorize and expand unconstitutional NSA spying', 'Care About Your Religion, I Care About My Rights', 'Federal programs to protect Americans against extreme weather', '44 LGBTQ Texans Are Running for Office in 2018', 'Texas Democratic judicial candidates', 'beto o', 'Voting in Texas', 'tx23', 'jason westin', 'joe straus', 'txgov', 'larry kilgore', 'Battleground Texas: 2018 Edition', 'Texas House of Representatives and State Senate', 'michael c. burgess', 'texas gop congressman', 'randy weber', 'rep. weber', 'Representative weber', 'congressman weber', 'rep weber', 'tx31', 'vanessa adia', 'kevin brady', 'roger williams', 'lupe valdez', 'medrick yhap', 'joe barton', 'rep. roger williams', 'ted cruz', 'sen. cruz', 'senator cruz', 'ted. cruz', 'tedcruz', 'texas district 07', 'pete sessions', 'rep. sessions', 'rep sessions', 'representative sessions', 'congressman sessions', 'john culberson', 'rep. culberson', '@congculberson', 'culberson\'s texas', 'congressman culberson', 'rep culberson', 'kenny marchant', 'rep. marchant', 'Rep (Marchant)', 'congressman marchant', 'rep marchant', 'letitia plummer', 'pete olson', 'rep. olson', 'rep olson', 'representative olson', 'congressman olson', 'tx-22', 'tx22', 'ted poe', 'H.R. 620', 'hr 620', 'tx-02', 'rep poe', 'representative poe', 'congressman poe', 'rep. poe', '^(?!.*anthony lamar smith).*lamar smith.*$', 'house science committee chair', 'tx-21', 'tx21', 'john carter', 'tx-31', 'farenthold', 'tx-27', 'hensarling', 'gohmert', 'tx-01', 'brian babin', 'rep. babin', 'rep babin', 'representative babin', 'congressman babin', 'greg abbott', 'texas governor', 'TX\'s next governor ', 'rolando pablos', 'governor of texas', 'tx gov', 'governor in Texas', '@gregabbott_tx', 'sb-4', 'sb4', 'sb 4', 'Senate Bill 4', 'rape insurance', 'Texas\' redistricting fight', 'ken paxton', 'texas attorney general', 'michael burgess', 'rep. burgess', 'rep burgess', 'representative burgess', 'congressman burgess', 'tx-26', 'tx26', 'will fisher', 'Michael McCaul', 'rep. mccaul', 'Representative mccaul', 'congressman mccaul', 'rep mccaul', 'mike mccaul']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Texas 2018 Election \n\n"
            "[Primary Election Early Voting Starts](https://teamrv-mvp.sos.texas.gov/MVP/mvp.do): February 20, 2018 \n\n"
            "[Primary Election](https://teamrv-mvp.sos.texas.gov/MVP/mvp.do): March 6, 2018 \n\n"
            "[General Election Registration Deadline](http://www.votetexas.gov/register-to-vote/): October 9, 2018 \n\n"
            "[General Election](https://teamrv-mvp.sos.texas.gov/MVP/mvp.do): November 6, 2018 \n\n")
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