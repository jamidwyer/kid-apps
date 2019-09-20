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

local_subs = open("northcarolina.dat", "r")
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
            terms = ['sanders coming to north carolina', 'town hall in greensboro', 'republicans hold surprise vote on budget', 'Republicans staged a surprise attack on Democracy on 9', 'north carolina house republicans', 'nc house gop', 'gop holds two US House seats in special election', 'nc-09', 'disaster declaration at the request of North Carolina', 'nervous republicans', 'genetics on display in Hillsboro, NC', 'attorney general josh stein', 'evangelicals chafe at trump', 'Trump Won Because Of Lower Democratic Turnout', 'm not owned by the NRA', 'north carolina gun shop', 'How the hell is this not inciting violence', 'rick scott', 'More Tax Cuts For Mega-Rich', 'GOP Demands Emergency Tax Cut for the Rich', 'Give Rich Americans Another Tax Cut', 'pretend this is normal election', 'Voting Machine Makers Claim The Names Of The Entities That Own Them Are Trade Secrets', 'donations to senate republicans', 'trump is leading a hate movement', 'contributors in nc', 'nc attorney general', 'rains holy hell on two GOP senators', 'ncsen', 'republicans even believe in democracy', 'electoral map bias', 'Remember when conservatives believed no one was above the law', 'Rev. William Barber', 'equal rights amendment', 'files again prove Republicans lied in court', 'nc governor', 'gov. roy cooper', 'bern in charlotte', 'Bernie speaks to thousands in Asheville', 'chuck mcgrady', 'teachers marching down bicentennial plaza', 'ncpol', 'north carolina ag', 'one of our own made it to the front page', 'tillis challenger', 'christopher holliday', 'thom tillis', ' nc environment', 'voting in north carolina', 'republican behind north carolina', 'north carolina rally', 'crime victims in nc', 'nc vot', 'republicans in north carolina', 'gerrymandering in north carolina', 'silent sam', 'north carolina constituion', 'nc gop', 'north carolina Republican', 'berger challenger', 'lee walker shooting', 'god is racist', 'north carolina election', 'steven buccini', 'nccapitol', 'nc senate', 'nc democrats', 'diamond and silk', 'n carolina lawmaker', 'gerrymandering of nc', 'nc election 2018', 'jenny marshall', 'N Carolina Green Party', 'house bill 185', 'vote in nc', 'North Carolina State Board of Elections', 'Democrats of Forsyth County', 'north carolina green party', 'nc republicans', 'north Carolina gop', 'NC candidates', 'north Carolina General assembly', 'roger w. allison', 'nc 5th congressional district', 'buncombe county sheriff', 'peter boykin', 'larry pittman', 'nc lawmaker', 'larry pittman', 'nc rep. lewis', 'beverly boswell', 'North Carolina\'s House District 79', 'NC House District 79', 'nc13', 'markmeadows', 'NC\'s 2nd congressional district', 'NC Supreme Court', 'ncae', 'Top NC court', 'NC redistricting', 'North Carolina redistricting', 'nc gerrymandering', 'North Carolina Gerrymander', 'North Carolina\'s Pro-GOP Gerrymander', 'NC Congressional map', 'NC electoral map', 'redrawn map in North Carolina', 'North Carolina congress', 'dd adams', 'nc-5', 'nc 6th', 'nc-cd5', 'ken romley', 'pittenger', 'mark walker', 'rep. walker', 'Representative walker', 'congressman walker', 'rep walker', 'virginia foxx', 'rep. foxx', 'Representative foxx', 'congresswoman foxx', 'rep foxx', '5th congressional district of NC', 'nc-05', 'mchenry', 'nc-10', 'mark meadows', 'rep. meadows', 'freedom caucus leader', 'Representative meadows', 'congressman meadows', 'rep meadows']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("North Carolina 2020 Election \n\n"
            "[Primary Election Voter Registration Deadline](https://www.ncsbe.gov/Portals/0/Forms/NCVoterRegForm06W.pdf): February 7, 2020 \n\n"
            "[Primary Election](https://www.ncsbe.gov/Voting-Options): March 3, 2020 \n\n"
            "[General Election Voter Registration Deadline](https://www.ncsbe.gov/Portals/0/Forms/NCVoterRegForm06W.pdf): October 9, 2020 \n\n"
            "[General Election](https://www.ncsbe.gov/Voting-Options): November 3, 2020 \n\n")
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