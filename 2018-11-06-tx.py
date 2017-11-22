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
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['Her New Sticker Says FUCK the Sheriff', 'discourage women from getting abortions. Republicans claim they don', 'Congressional Republicans block vote on amendment to let marijuana businesses use banks', 'texas district 07', 'hitting fire code limits, running out of parking spaces, and spilling out of living rooms and into yards', 'Can Democrats retake Southern legislatures', 'The Good Old Boys in the Texas Legislature', 'pete sessions', 'rep. sessions', 'rep sessions', 'representative sessions', 'congressman sessions', '13 polls in GOP-held House districts conducted', 'john culberson', 'rep. culberson', '@congculberson', 'congressman culberson', 'rep culberson', 'GOP strategists worry incumbents aren', 'kenny marchant', 'rep. marchant', 'Rep (Marchant)', 'congressman marchant', 'rep marchant', 'letitia plummer', 'pete olson', 'rep. olson', 'rep olson', 'representative olson', 'congressman olson', 'tx-22', 'tx22', 'ted poe', 'H.R. 620', 'hr 620', 'Republicans are deciding they want no part of the 2018 elections', 'tx-02', 'rep poe', 'representative poe', 'congressman poe', 'rep. poe', '^(?!.*anthony lamar smith).*lamar smith.*$', 'Where All 533 Members of Congress Stand on Bump Stocks', 'house science committee chair', 'tx-21', 'tx21', 'john carter', 'disaster funds cut to finance wall', 'tx-31', 'House DACA deal won\'t need Democratic votes', 'farenthold', 'tx-27', 'Congress plays by different rules on sexual harassment and misconduct', 'hensarling', 'gohmert', 'tx-01', 'brian babin', 'rep. babin', 'rep babin', 'representative babin', 'congressman babin', 'greg abbott', 'texas governor', 'TX\'s next governor ', 'Texans are more open to legalizing marijuana', 'Harvey Relief Program Nixes Requirement to Not Boycott Israel', 'caveat is the result of a strange new state law', 'Abbott Plan to Amend Constitution', 'Texas Is No Longer Feeling Miraculous', 'The Racist Map Wins', 'Democrats Must Take a Shot at Texas', 'Federal Judge Blocks Texas', 'rolando pablos', 'Texas Republican turns down donated blankets', 'Judge blocks provisions in Texas law punishing \'sanctuary cities\'', 'bill restricting insurance coverage of abortion', 'governor of texas', 'tx gov', 'runs for governor in Texas', '@gregabbott_tx', 'Texas crackdown on sanctuary cities', 'sb-4', 'sb4', 'sb 4', 'Senate Bill 4', 'rape insurance', 'Texas\' redistricting fight', 'tx governor\'s', 'ken paxton', 'texas attorney general', 'Another reason AG\'s are important in 2018.', 'future of DACA suddenly looks very shaky', 'immigrants in Houston brace for a DACA decision', 'distract from his own felony trial', 'Courts repeatedly chastise Texas for voting-rights violations', 'racist attack on minority voting rights might finally backfire', 'U.S. Supreme Court temporarily blocks ruling against Texas congressional map', 'blocks Texas ban on sanctuary cities', 'A federal judge just blocked Texas', 'Fix Its Discriminatory Voting Laws', 'michael burgess', 'rep. burgess', 'rep burgess', 'representative burgess', 'congressman burgess', 'tx-26', 'tx26', 'will fisher', 'Michael McCaul', 'rep. mccaul', 'Representative mccaul', 'congressman mccaul', 'rep mccaul', 'mike mccaul']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Texas 2018 Election \n\n"
            "[Primary Voter Registration Deadline](http://www.votetexas.gov/register-to-vote/): February 5, 2018 \n\n"
            "[Primary Election](https://teamrv-mvp.sos.texas.gov/MVP/mvp.do): March 6, 2018 \n\n"
            "[General Election](https://teamrv-mvp.sos.texas.gov/MVP/mvp.do): November 6, 2018 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass
        # Store the current id into our list
        posts_replied_to.append(submission.id)

for sub in subs:
     print(sub)
     searchAndPost(sub);

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

text_file.close()
local_subs.close()