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

local_subs = open("california.dat", "r")
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
            terms = ['devin nunes', 'rep. nunes', 'congressman nunes', 'House Intel chief', '20 percent of our uranium', 'Journalist nails GOP\'s fake patriotism', 'Fake news Clinton story revived', 'desperately trying to shift blame to Clinton', 'The Evolution of a Right Wing Distraction', 'House panel says it will get bank records from firm behind Trump dossier', 'RUSSIA URANIUM ONE CONSPIRACY THEORY', 'Alt-Collusion to Defend Trump From Mueller', 'Russian uranium efforts', 'Someone Is Really Worried About the Trump', 'Republicans Leaking Confidential Info Like Crazy', 'Republicans look past Trump scandals, zero in on Hillary Clinton', 'Blowing Goats Instead Of Investigating', 'How Republicans Are Jumping on the New ', 'fund the Trump golden shower dossier', 'Republicans seize on dossier revelations to counter Russia probes', 'House Republicans investigating Obama', 'Russia Probe Just Blew Up', 'Russia Probe Not That Interested in Trump or Russia', 'GOP launches probes into Clinton, Obama controversies', 'era uranium deal', 'partisan split widening over Russia probe', 'Trump Singes Fingers Trying to Torch Dossier', 'House Intel Committee Have Enough Staff', 'Republican House intelligence committee members are coaching witnesses', 'Partisan feud undercuts Trump-Russia probe', 'Flat Earth" Report', 'clear abuse of power', 'Russia dossier balks at House subpoena', 'Firm behind Trump-Russia dossier subpoenaed', 'Nunes lunges back into Russia', 'dossier subpoenaed by House intelligence committee', 'Nunes Subpoenaed', 'Nunes signs off on new subpoenas', 'The Secrecy Undermining the Senate Intelligence Committee', 'House intel Democrat on Russia probe', 'California could flip the House, and these 13 races will make the difference', 'More smoking guns than Bonnie and Clyde', 'Republican attempt to deflect Trump-Russia probes', 'Republicans Trying to Discredit Mueller Investigation', 'rep nunes', 'House panel subpoenas Justice Dept. and FBI']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("California 2018 Election \n\n"
            "[Voter Registration Deadline](http://registertovote.ca.gov/): May 16, 2018 \n\n"
            "[Primary Election](http://www.sos.ca.gov/elections/voter-registration/vote-mail/#apply): June 5, 2018 \n\n"
            "[General Election](http://www.sos.ca.gov/elections/voter-registration/vote-mail/#apply): November 6, 2018 \n\n")
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