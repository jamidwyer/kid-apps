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

local_subs = open("newjersey.dat", "r")
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
            terms = ['analilia mejia', 'new human rights commission', 'wilda diaz', 'Immigrant Workers Fired From President Trump', 'Jewish Woman for protesting concentration Camps', '30 jewish protesters arrested', 'beronica ruiz', 'nj attny general', 'with l of these goddamn', 'spotted in middletown nj', 'Bedminster', 'nj-11', 'seth grossman', 'new jersey passed sweeping', 'murphy set to sign law', 'nj state legislat', 'nj Representative', 'new jersey lawmaker', 'NJ marijuana legalization', 'nj assembly', 'new jersey voters', 'josh gottheimer', 'Representative Chris Smith', 'NJ GOP Candidate', 'Republican Hugin', 'NJ\'s 7th District', 'nj cd-7', 'N.J. congressman', 'keady', 'New Jersey Senate', 'Congressman Chris Smith', 'NJ State Senator Ron Rice', 'NJ congressmen', 'NJ GOP rep', 'thomas macarthur', 'tom macarthur', 'rep. macarthur', 'rep macarthur', 'representative macarthur', 'congressman macarthur', 'lobiondo', 'leonard lance', 'nj-7', 'nj-07', 'frelinghuysen']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("New Jersey 2020 Election \n\n"
            "[Register to Vote](https://www.state.nj.us/state/elections/voter-registration.shtml) \n\n"
            "[General Election](https://www.state.nj.us/state/elections/vote-by-mail.shtml): November 3, 2020 \n\n")
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