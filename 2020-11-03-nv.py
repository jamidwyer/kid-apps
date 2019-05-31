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

local_subs = open("nevada.dat", "r")
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
            terms = ['sanders in reno', 'sisolak veto', 'nevada\'s women lawmak', 'las vegas cannabis', 'nuclear waste to yucca mountain', 'sad as it is necessary', 'Nevada, elect', 'candidate in nevada', 'hillary schieve', 'nevada\'s rosen', 'Las Vegas festival mass shooting', 'congressperson in nevada', 'nevada ballot', 'picket in las vegas', 'las vegans protest', 'brothel owner hof', 'cortez masto', 'trump in Vegas', 'nevada gop', 'las vegas union', 'nevada primary', 'Nevada 4th Congressional District', 'pat spearman', 'washoe county sheriff', 'nevada voter', 'Vegas shooter', 'John Anzalone', 'Clark County DA', 'nv assembly', 'living wage in nv', 'nevada assembly', 'Las Vegas massacre', 'banning bump stocks', 'nevada politic', 'nv04', 'nv-03', 'nv-02', 'NV GOP wants to', 'kate marshall', 'Las Vegas shooting', 'Nevada House, Senate races', 'jay craddock', 'nevada legislat', 'amodei', 'Nicole Cannizzaro', 'Nevada\'s 4th District Race', 'laxalt', 'kihuen', 'oscarson', 'Nevada Supreme Court justice', 'amy vilela', 'State Senate Recall', 'michael roberson', 'Richard McArthur', 'tony smith', 'sisolak', '^(?!.*hellerweather).*heller.*$', 'sbaih', 'Nevada GOP', 'jared fisher', 'governor sandoval', 'nevada governor', 'NV\'s next governor ', 'governor of nevada', 'nv gov', 'nv governor\'s']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        # Early voting ended
        text = ("Nevada 2020 Election \n\n"
            "[Register to Vote](https://www.registertovotenv.gov/SOSVoterServices/Registration/Step1.aspx) \n\n"
            "[Primary Election](https://www.nvsos.gov/sos/home/showdocument?id=2394): June 9, 2020 \n\n"
            "[General Election](https://www.nvsos.gov/sos/home/showdocument?id=2394): November 3, 2020 \n\n")
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