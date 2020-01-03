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
            terms = [
                'texas school district', \
                'texas wants to curb college students', \
                'plan to criminalize homelessness', \
                'false addresses on migrant papers', 'Horrible Death in US Immigration Detention Center', \
                't care do u', 'Barron has been violated', 'super tuesday', \
                'texas homecoming shooting', 'beto', 'flip the senate', 'Turning Away Pregnant Asylum-Seekers', \
                'thornberry retirement', 'hate crime in dallas', 'bravery in crenshaw', 'third democratic debate', 'gina ortiz jones', 'baby prison bus', 'Waqar Hasan', 'plano rally', 'texas state rep', 'supporters at austin event', 'nervous republicans', 'rep. dan crenshaw', 'el paso mayor', 'marches in el paso', 'trumpsbodycount', 'el paso grieve', 'texas in 2020', 'white nationalist killers', 'texas cops beat', 'texas hit with lawsuit', 'trump is a white nationalist', 'senate has voted', 'transport technique', 'texas elect', 'el paso shoot', 'texas in play', 'shooter in el paso', 'shooting in el paso', 'gohmert', 'el paso gunman', 'el paso mall shooter', 'texas house gop', 'john zerwas', 'christian enough for texas', 'tony timpa', 'texas from trump', 'gop senate', 'texas poll', 'texas republican', 'texas racially discriminated', 'Carlos Gregorio Hernandez Vasquez', 'federal child abuse at our border', 'donations to senate republicans', 'jodey arrington', 'deadly houston drug raid', 'house impeachment resolution', 'border city of mcallen', 'texasgop', 'texas legislat', 'el paso court', 'texas a battleground', 'kids in cages', 'FBI and ICE use DMV photos', 'texas young voter', 'march in clint', 'joaquin castro', 'concentration camps at its border', '2020 generic congressional ballot', 'tx border patrol', 'texas migrant facility', 'texas detention', 'clint detention', 'secretary castro', 'drowned migrant and daughter', 'soap, toothbrushes', 'texas border facility', 'toddlers in detention camps', 'sarah fabian', 'texas gov', 'texas gop', 'texas goes blue', 'fire at el paso church', 'Pompeo Laments Cruelty', 'jessica cisneros', 'txdem', 'will hurd', 'patriot front', 'vichy republicans', 'texas for border wall', 'private land for border wall', 'rig the 2020 census', 'texas dems', 'texas democrat', 'texas primary', 'el paso rally', 'texas judge', 'governor abbott', 'a resignation in texas', 'governor of texas', 'gop in texas', 'chip roy', 'pipeline in texas', 'san antonio prosecutor', 'migrant boy who died in custody', 'tx-32', 'muhlaysia booker', 'tx-22', 'tx-23', 'tx-28', 'dallas campaign', 'tx-21', 'wendy davis', 'tx-sen', 'rep. al green', 'lt. gov. patrick', 'cornyn', 'texas law', 'fastest-warming cities', 'demolished for border wall', 'texas capitol', 'turnout in Dallas', 'texas police officers', 'texas politic']
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