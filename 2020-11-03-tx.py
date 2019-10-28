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
            terms = ['texas homecoming shooting', 'preach beto', 'Beto responding to a homophobic Catholic priest', 'flip the senate', '400 Babies Have Been Forced to Wait in High-crime', 'Turning Away Pregnant Asylum-Seekers', 'thornberry retirement', 'DA is literally trying to throw the case', 'hate crime in dallas', 'Hispanics in El Paso probed by FBI', '\'fellow Latinos\' to vote Trump out', 'bravery in crenshaw', 'third democratic debate', 'gina ortiz jones', 'baby prison bus', 'Waqar Hasan', 'plano rally', 'my ar is ready for you', 'republican politician sends beto', 'texas state rep', 'supporters at austin event', 'nervous republicans', 'rep. dan crenshaw', 'el paso mayor', 'marches in el paso', 'trumpsbodycount', 'el paso grieve', 'texas is bracing for a blue wave', 'texas in 2020', 'voters see white nationalism', 'members of the press, what the fuck', 'white nationalist killers', 'texas cops beat', 'texas hit with lawsuit', 'trump is a white nationalist', 'senate has voted', 'transport technique', 'texas elect', 'el paso shoot', 'texas in play', 'trumpsterrorists', 'shooter in el paso', 'shooting in el paso', 'el paso gunman', 'el paso mall shooter', 'texas house gop', 'john zerwas', 'Retirements May Hobble House Republicans', 'tony timpa', 'serving under trump is embarrassing', 'More Tax Cuts For Mega-Rich', 'texas from trump', 'gop senate', 'texas poll', 'texas republican', 'texas racially discriminated', 'Carlos Gregorio Hernandez Vasquez', 'federal child abuse at our border', 'donations to senate republicans', 'House blocks arms sales to Saudi', 'jodey arrington', 'house impeachment resolution', 'plan for avoiding debt default', 'border city of mcallen', 'Republican Senate knew it when they confirmed him', 'texasgop', 'texas legislat', 'el paso court', 'texas a battleground', 'million children work unimaginably long hours', 'care about the kids in cages', 'FBI and ICE use DMV photos', 'texas young voter', 'march in clint', 'border patrol agents tried to delete', 'detained migrant children depict them being held behind bars', 'joaquin castro', 'concentration camps at its border', '2020 generic congressional ballot', 'tx border patrol', 'just drink from the toilet', 'joke about migrant deaths', 'texas migrant facility', 'texas detention', 'clint detention', 'secretary castro', 'beto v castro', 'drowned migrant and daughter', 'terrible power of u.s. border officials', 'soap, toothbrushes', 'texas border facility', 'toddlers in detention camps', 'sarah fabian', 'texas gop', '4 severely ill migrant toddlers', 'texas goes blue', 'fire at el paso church', 'an expert on concentration camps', 'jessica cisneros', 'first jd candidate', 'txdem', 'Ten cities say Trump owes them money', 'will hurd', 'This is worse than Watergate', 'will be hit hardest by trump', 'scheme to rig the 2020 census', 'texas dems', 'texas democrat', 'texas primary', 'voter Suppression Is the Expressed Policy', 'el paso rally', 'Republicans Plan to Rig Elections for a Decade', 'Beto pays his bills on time', 'citizenship question to the Census', 'plans to rig elections for white Republicans', 'tx stands with beto', 'texas judge', 'running with beto', 'botched voter purge', 'governor abbott', 'a resignation in texas', 'governor of texas', 'gop in texas', 'republicans hate governing', 'chip roy', 'Trump falls short on infrastructure', 'Campaign Is Showing Solidarity with Striking Workers Like', 'pipeline in texas', 'san antonio prosecutor', 'migrant boy who died in custody', 'muhlaysia booker', 'tx-22', 'tx-23', 'As president, I will sign into law a new Voting Rights Act', 'tx-28', 'dallas campaign', 'tx-21', 'wendy davis', 'nerds out and the crowds go crazy', 'tx-sen', 'rep. al green', 'lt. gov. patrick', 'cornyn', 'texas law', 'fastest-warming cities', 'demolished for border wall', 'texas capitol', 'turnout in Dallas', 'texas politic']
            for term in terms:
                 search(term, submission)

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Texas 2020 Election \n\n"
            "[Primary Registration Deadline](http://www.votetexas.gov/register-to-vote/): February 3, 2020 \n\n"
            "[Primary Election](https://teamrv-mvp.sos.texas.gov/MVP/mvp.do): March 3, 2020 \n\n"
            "[General Election Registration Deadline](http://www.votetexas.gov/register-to-vote/): October 4, 2020 \n\n"
            "[General Election](https://teamrv-mvp.sos.texas.gov/MVP/mvp.do): November 3, 2020 \n\n")
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