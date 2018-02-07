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
            terms = ['North Carolina\'s House District 79', 'Democrats twist geographical disadvantage into rhetorical tool', 'Solar tariffs could cost N.C. hundreds of job', 'NC House District 79', 'nc13', 'abandoning elections of judges', 'She has a gay son and wants a clean repeal', 'markmeadows', 'sit-in at Cooper\'s office', 'NC\'s 2nd congressional district', 'NC Supreme Court', 'ncae', 'Top NC court', '830K earmark in NC budget', 'NC redistricting case', 'North Carolina redistricting case', 'North Carolina Gerrymandering Ruling', 'CIA rendition flights from rustic North Carolina', 're-drawing of congressional district maps in North Carolina', 'House conservatives demand vote on tough border bill to avoid shutdown', 'can enthusiasm push them to victory', 'The remarkable thing that happens to poor kids when you give their parents a little money', 'Gap In Education Spending Among North Carolina Counties', 'North Carolina and Illinois are mulling similar legislation', 'North Carolina\'s Pro-GOP Gerrymander', 'How Gerrymandering Silenced North Carolina', 'Mark Loves Koch!', 'Sneaky Attack on Partisan Gerrymandering', 'North Carolina Is Ordered to Redraw Its Congressional Map', 'North Carolina GOP refuses to share', 'NC GOP Senate', 'The ruling on North Carolina', 'NC Congressional map', 'NC electoral map', 'redrawn map in North Carolina', 'North Carolina congressional map', 'Republicans Gerrymander North Carolina', 'The sexual harassment vote the GOP would like to forget', 'Racial Gerrymandering and Voter Suppression Laws', 'The head of a conservative Republican faction in the U.S. Congress', 'the least we can pay you. and we are going to hold there forever', 'North Carolina Democrats hope for 2018 gains', 'dd adams', 'nc-5', 'NC GOP is still gutting our elementary schools', 'unregulated chemical entered a North Carolina community', 'snub of Roy Cooper rep', 'nC over HB2', 'nc 6th', 'We do not have constituents. We cannot take a side', 'Congress shamefully shills for new bible museum', 'nc-cd5', 'ken romley', 'Audit reveals massive power of the NRA in Washington', 'pittenger', 'Trump ignored the world\'s Chicken Littles', 'Does new version of the AHCA protect coverage for pre-existing conditions?', 'absolutely does not eliminate protections for pre-existing conditions', 'mark walker', 'rep. walker', 'GOP eyes move to lower premiums right before 2018 elections', 'Huge, Exploding Deficits', 'Representative walker', 'congressman walker', 'rep walker', 'warns GOP to change course on ObamaCare', 'repealing the Johnson Amendment isn', 'Ignore The Deficit', 'virginia foxx', 'rep. foxx', 'Representative foxx', 'congresswoman foxx', 'rep foxx', '5th congressional district of NC', 'nc-05', 'mchenry', 'nc-10', 'Is Your Representative Setting Us Up for Another Dieselgate', 'mark meadows', 'rep. meadows', 'sexual harassment policy', 'Republican Party is a broken marriage', 'Skeptical Reception From Some in Congress', 'republicans think trump is unstable', 'Meadows: Time to ', 'highlight broader concerns in GOP', 'Retiring GOP lawmaker defends Corker', 'Trump, GOP weigh surtax on wealthy', 'money gets into politics but still not be bothered by it', 'closed until Republicans pass health and tax reform', 'House Crazies Angry At Trump', 'Mistakenly Put on Brief Against Partisan Gerrymandering', 'Trump blasts own party', 'Mean to Sign Brief Against Gerrymandering', 'accidentally asked the Supreme Court to end gerrymandering', 'Inside the Freedom Caucus', 'freedom caucus leader', 'Representative meadows', 'congressman meadows', 'rep meadows']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("North Carolina 2018 Election \n\n"
            "[Primary Voter Registration Deadline](https://www.ncsbe.gov/Voters/Registering-to-Vote): April 13, 2018 \n\n"
            "[Primary Election](https://www.ncsbe.gov/Voting-Options): May 8, 2018 \n\n"
            "[General Election](https://www.ncsbe.gov/Voting-Options): November 6, 2018 \n\n")
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