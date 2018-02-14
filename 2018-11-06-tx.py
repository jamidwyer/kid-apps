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
            terms = ['Texas Dem Senate Candidate', 'repay taxpayers for sex harassment suit', 'texas gubernatorial', 'cruz to the curb', 'Cruz warns Texas GOP', ' After Conservatives Accuse Them of ', 'Texas has slashed funding for family planning', 'Texas\' statewide elections of judges', 'Koch-backed group fights paid sick leave laws', 'Target Republicans in 12 states', 'texas redistricting', 'Flip a Red District in Texas', 'A Texas Teacher Just Died Because She Couldn', 'North Texas teacher dies after getting the flu', 'North Texas teacher dies after getting the flu and not picking up her medication', 'Texas goes Democratic', 'decries mccaul', 'Loved ones should not be pulled from each others arms', 'Texas Democrats Who Worked For Obama', 'town hall in Bay City Saturday February 10th', 'Rourke returning to Rio Grande Valley', 'rick trevino', '2018 Primaries for Texas', 'Stave Off Beto', 'Texas Democrats plan winner-take-all fundraiser', 'will hurd', 's Coming to UNT Denton', 'participate in the March 6th primary', '2018 Texas primaries', 'Texas\' Next Senator', 'Democrats up 14', 'Deficit Explodes Yet Again Under Republican Rule', 's Coming to UNT', 'Texas congressional races', 'Texas 3rd Congressional District', 'texas voters', 'Texas countryside, undocumented immigrants', 'Voter registration surges in Houston', 'Texans, get ready to vote', 'beto makes his case', 'no-PAC campaign paying off against Cruz', 'cruz vs. o', 'Texas, Louisiana, Mississippi, Alabama, and South Carolina still have laws punishing educators', '25 on Generic Ballot', 's Generic Ballot', 'saari', 'vote for beto', 'House Republicans in Texas', 'Plano Democrat Wants to Replace Republican', 'who Texas sends to Congress', 'Candidates Who Signed Up to Battle Donald Trump', 'Republican Crusade Against Pregnant Women', 'Difference In Texas, UTA Political Scientist', 'GOP senators who pushed Trump to ditch', 'dan patrick', 'Senate is Getting Ready to Erode Obama', 'derrick crowe', 'Cruz leads DEM', 'TX district judge', 'Single-Digit Lead In Texas', 'sam johnson', 'single digits of cruz', 'requested records for all Texans with Hispanic surnames', 'Thank you, Mr. Williams.', 'At the Women\'s March in Fort Worth', 'colin allred', 'Texas Justice Democrat', 'tx-32', 'Republicans file lawsuit to kick 128 Democrats off election ballot', 'Women\'s Rights March 2018 - Photo Album', 'in both blue and red states', 'your party was holding our districts children as political hostage', 'tx-16', 'March in Dallas today', 'Austin, TX broke the record for largest gathering in Texas history', 'dallas women\'s march', 'Marches in Dallas on Saturday', 'March scheduled for Saturday, Jan. 20, in downtown Austin', 'Most Powerful Political Office: Lieutenant Governor', 'Senate Passes Warrantless Spying Reauthorization Bill', 'Congress demanded NSA spying reform', 'legal medical marijuana decreased drug crime in US states', 'rep. dukes', 'Boost Turnout In GOP Primaries', 'I believe the impossible is possible', 'primaries start in mere WEEKS', '65 just voted to expand NSA spying', '256 representatives that just voted to reauthorize and expand unconstitutional NSA spying', 'Care About Your Religion, I Care About My Rights', 'Federal programs to protect Americans against extreme weather', '44 LGBTQ Texans Are Running for Office in 2018', 'Texas Democratic judicial candidates' 'Running for Office to Make Texas a Better Place', 'When Mexico succeeds, the U.S. succeeds', 'US shatters record for disaster costs in 2017', 'beto o', 'Voting in Texas for 2018', 'tx23', 'jason westin', 'joe straus', 'txgov', 'larry kilgore', 'Battleground Texas: 2018 Edition', 'Texas House of Representatives and State Senate', 'michael c. burgess', 'texas gop congressman', 'randy weber', 'rep. weber', 'Representative weber', 'congressman weber', 'rep weber', 'tx31', 'vanessa adia', 'kevin brady', 'roger williams', 'lupe valdez', 'Senators Sanders and Cruz', 'medrick yhap', 'joe barton', 'rep. roger williams', 'ted cruz', 'sen. cruz', 'senator cruz', 'ted. cruz', 'Cruz claims repealing the estate tax', 'Bernie calls GOP tax plan a \'Robin Hood proposal in reverse', 'Sanders, Cruz spar', 'Ted Lies Again', 'tedcruz', 'texas district 07', 'pete sessions', 'rep. sessions', 'rep sessions', 'representative sessions', 'congressman sessions', 'john culberson', 'rep. culberson', '@congculberson', 'culberson\'s texas', 'congressman culberson', 'rep culberson', 'kenny marchant', 'rep. marchant', 'Rep (Marchant)', 'congressman marchant', 'rep marchant', 'letitia plummer', 'pete olson', 'rep. olson', 'rep olson', 'representative olson', 'congressman olson', 'tx-22', 'tx22', 'ted poe', 'H.R. 620', 'hr 620', 'tx-02', 'rep poe', 'representative poe', 'congressman poe', 'rep. poe', '^(?!.*anthony lamar smith).*lamar smith.*$', 'house science committee chair', 'tx-21', 'tx21', 'john carter', 'tx-31', 'farenthold', 'tx-27', 'hensarling', 'gohmert', 'tx-01', 'brian babin', 'rep. babin', 'rep babin', 'representative babin', 'congressman babin', 'greg abbott', 'texas governor', 'TX\'s next governor ', 'rolando pablos', 'governor of texas', 'tx gov', 'governor in Texas', '@gregabbott_tx', 'sb-4', 'sb4', 'sb 4', 'Senate Bill 4', 'rape insurance', 'Texas\' redistricting fight', 'tx governor\'s', 'ken paxton', 'texas attorney general', 'michael burgess', 'rep. burgess', 'rep burgess', 'representative burgess', 'congressman burgess', 'tx-26', 'tx26', 'will fisher', 'Michael McCaul', 'rep. mccaul', 'Representative mccaul', 'congressman mccaul', 'rep mccaul', 'mike mccaul']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Texas 2018 Election \n\n"
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