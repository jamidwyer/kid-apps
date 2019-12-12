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

local_subs = open("illinois.dat", "r")
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
            terms = ['chicagoyanggang', 'Jan Schakowsky', 'better president than lincoln', 'illinois becomes first state', 'sanders getting arrested', 'chicago teachers union', 'illinois leadership team', 'soybean purchase pledge', 'chicago prosecut', 'sanders arrested while protesting segregation', 'agriculture disaster throughout illinois', 'black preteen who is shot by police', 'Bill To Reschedule And Research Marijuana', 'Deported Veterans Say They', 'pritzker signs bill', 'i watched my patients die of poverty', 's homeless in 2017 had jobs', 'illinois becomes first state', 'illinois for legal', 'Warren restates support for busing', 'weed cafes in illinois', 'illinois is expunging marijuana', 'Trump Says Employee At Chicago', 'ICE shows up at your door', '16 shots', 'illinois expands gambling', 'welfare queen of chicago', 'governor visits grafton', 'convictions for 770,000', 'U.S. laws protect cops while endangering civilians.', 'marijuana goes on sale Jan. 1 in Illinois', 'legal in illinois', 'illinois legaliz', 'university of chicago graduate students', 'kash jackson', 'illinois prison', 'mike quigley', ' il bill', 'teenage girl for sex in exchange for impounded car', 'illinois video gambling', 'Trump falls short on infrastructure', 'illinois marijuana legaliz', 'chicago to protest', 'perceived threat of gun violence', 'Progressives Scored Big Wins in Chicago', 'biggest Midwestern state to legalize recreational marijuana', '1,000 per year to own an electric vehicle', 'dick durbin', 'haymarket affair', 'chicago impounds', 'trump tower chicago', 'illinois state capitol', 'ILLINOIS STATE LAWMAKER', 'abe lincoln', 'dirksen londrigan', 'sean casten', 'illinois law', '37th state to ratify Equal Rights Amendment', 'illinois house', 'illinois rep.', 'illinois progressive network', 'haymarket riot', 'hb 4819', 'congress in illinois', 'aaron ortiz', 'il-03', 'illinoisprimary', 'chicago registered voters', 'illinois legislat', 'illinois primary', 'demonstrations in chicago', '^(?!.*tara lipinski).*lipinski.*$', 'Democrat in Illinois', 'illinois vot', 'illinoispolitics', 'Illinois Primar', 'flip illinois', 'marie newman', 'chuy garcia', '#ilgov', 'Illinois\'s 3rd Congressional District', 'illinois republican', 'Republican congressional primary in Illinois', 'arthur jones', 'Illinois Congress', 'Illinois GOP', 'illinois green Party', 'Illinois Democratic Gubernatorial', 'Illinois 13th\'s Congressman', '2018 illinois election', 'Illinois Dem gubernatorial candidate', 'rotering', 'Illinois attorney general', 'Illinois Senate', 'Chicago Congressional Primary', 'rep lahood', 'hultgren', 'il-14', 'shimkus', '\'chuy\' garcia', 'Rep. Gutierrez', 'anthony clark', '@cdrosa', 'Carlos Ramirez-Rosa', 'Rep. LaHood', 'mike bost', 'rep. bost', 'congressman bost', 'rep bost', 'representative bost', 'rodney davis', 'davis\'s seat', 'roskam', 'il-6', 'il-06', 'chicago transit', 'chris kennedy', '^(?!.*trauner).*rauner.*$', 'IL gubernatorial', '@govrauner', '^(?!.*bissexual).*biss.*$', 'illinois governor', 'governor of illinois', 'il gov', 'jeanne ives', 'pritzker', 'il governor\'s']
            for term in terms:
                 search(term, submission)

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Illinois 2020 Election \n\n"
            "[Register to Vote](https://ova.elections.il.gov/Step0.aspx) \n\n"
            "[Primary Election](https://ova.elections.il.gov/PollingPlaceLookup.aspx): March 17, 2020 \n\n"
            "[General Election](https://ova.elections.il.gov/PollingPlaceLookup.aspx): November 3, 2020 \n\n")
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