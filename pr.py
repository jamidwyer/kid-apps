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

text_file = open("standardsubs.dat", "r")
subs = text_file.read().split('\n')

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['whiplash weekend heightens questions over leadership', 'Puerto Rico and health care magnify Trump', 'Trump spat with San Juan mayor escalates as all sides double down', 'trump\'s katrina', 'Puerto Rico potshots make his racism morally impossible to ignore', 'another clearly calculated, yet graceful gesture to Americans in need', 'Call Out President Trump on His Response to Puerto Rico Crisis', 'Trump attacks San Juan mayor over hurricane response', 'Dedicating Golf Trophy To Hurricane Victims', 'Trump Dedicates a Golf Trophy to Hurricane Victims', 'Mulvaney criticizes San Juan', 'Trump dedicates golf trophy', 'Trump congratulates himself on Puerto Rico response, heads to golf course', '600 billion a year can do so much', 'Good-at-Words-Talking Describes Puerto Rico Death Toll as', 'Appreciates The Congrats On Tremendous Job He', 'puerto rico tweets are unspeakable', 'update on Puerto Rico', 'even fucking mobilize 50 helicopters, rescue forces, and a bunch of military aid', 'struggles with basics of being POTUS', 'everyone that was in the Intensive Care Unit, died', 'Puerto Rican Troops Are Still Waiting for Orders While Residents Cry for Help', 'travels to New Jersey to watch a golf tournament', 'half of Puerto Ricans without access to drinking water', 'Who would attack London mayor in midst of terror attack, San Juan mayor during disaster', 'Puerto Rico is all our worst fears about Trump coming real', 'White House Memo Details Puerto Rico Spin', 'Trump attends Presidents Cup golf tourney', 'new spin on puerto rico', 'She attacked, he attacked back', 'Disses Puerto Rico From the Golf Course', 'Stop Rationalizing President Trump', 'Tweets on Puerto Rico Are a National Disgrace', 'last 7 days are just mind-bogglingly bad', 'I hope Puerto Ricans never forget nor forgive how they have been treated by Trump and the Republicans', 'Trump\'s Puerto Rico rhetoric', 'golfing while Americans die', 'big water', 'Donald Trump criticises mayor of Puerto Rican capital', 'Trump calls his Puerto Rico critics', 'Trump has spent his morning insulting the mayor of San Juan', 'Obama disaster relief chief accuses Trump of', 'everything done for them', 'They want everything to be done for them', 'thinks there\'s no problem in Puerto Rico', '18 tweets on Puerto Rico on Saturday', 'Politically Motivated Ingrate', 'tweeting and golfing while people in Puerto Rico are dying', 'gaudy, gold-inlaid golf course']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Charities on the ground in Puerto Rico: [Red Cross](https://www.redcross.org/donate/donation) | [Save the Children](https://secure.savethechildren.org/site/c.8rKLIXMGIpI4E/b.9535647/k.A2B9/Hurricane_Maria_Childrens_Relief_Fund/apps/ka/sd/donor.asp) \n\n"
            "[Updated local information about Puerto Rico](http://www.univision.com/univision-news/united-states/find-updated-information-about-your-town-in-this-puerto-rico-search-engine) \n\n")
        print("Bot replying to : ", submission.title)
        submission.reply(text)
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