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
            terms = ['deleted data on puerto rico', 'particular racism towards Puerto Ricans', 'Why Did FEMA Remove Stats About Puerto Rico', 'It is inarguable that Trump hates the Puerto Ricans', 'the definition of adding insult to injury', 'Only Half of Puerto Rico Has Clean Water', 'statistics about drinking water access and electricity in Puerto Rico from website', 'FEMA restores deleted Puerto Rico stats', 'Berlin Airlift', 'stats on Puerto Rico recovery', 'dead in Puerto Rico are underreported', 'in the Wealthy Suburbs', 'Could Pay to Send Puerto Rico 128 Cargo Ships With Aid', 'End Insulting Tweets and Start Rebuilding Puerto Rico', 'Great visit. Really lovely... I enjoyed it very much', 'Puerto Rican Debt Comments Have Spooked Investors', 'already paid to rebuild Puerto Rico', 'death toll in Puerto Rico is higher than official count', 'US Presidents interacting with their people in times of need', 'Minimized Our Suffering', 'following him on Twitter and watching him on cable TV when they don\'t even have electricity or potable water', 'make up Puerto Rican truck strike to absolve Trump', 'threw paper towels at Puerto Ricans', 'the dead have not been counted yet', 'Oxfam slams the Trump administration', 'example of Trump only serving his base', 'throwing relief supplies into the crowd on Puerto Rico', 'POTUS handed out flashlights to Puerto Ricans, joking ', 'Trump says Puerto Rico officials should be', 'Puerto Rico and How Trump Responds to Tragedy', 'Trump Calls Puerto Rico Recovery a', 'Did Trump Mix Up The Air Force And Coast Guard', 'Trump in Puerto Rico', 'Death toll in Puerto Rico from Hurricane Maria climbs to 34', 'Hurricane Maria Could Change the Politics of Puerto Rico', 'Throwing Paper Towels At Them', 'trump tosses paper towels', 'official death count to 34', 'death toll has risen to 34', 'Puerto Rico death toll risen to 34', 'Well, It Sounded Good When He Said It', 'Trump tells Puerto Ricans that they have been lucky', 'President Trump just set a new standard in his search for flattery', 'Trump is Not Planning to Rebuild Puerto Rico', 'Trump meme is running like crazy in my social media', 'truck drivers for refusing to ship relief supplies', 'Trump throws paper towels', 'lobs paper towel rolls', 'so presidential', 'Puerto Rico event was way worse than his tweets', 'Trump Lands in Puerto Rico After Complaining About Residents', 'Denounce Militarization Amid Lack of Aid Distribution', 'Plea for Puerto Rico Hurricane Relief', 'real catastrophe', 'Puerto Rico oversight board asks Washington for more aid for island', 'criticizes US government response in Puerto Rico', 'Mayor of San Juan shows what True Patriotism means', 'Trapped in the mountains, Puerto Ricans', 'Donald Trump saves Puerto Rico', 'whiplash weekend heightens questions over leadership', 'Puerto Rico and health care magnify Trump', 'Trump spat with San Juan mayor escalates as all sides double down', 'trump\'s katrina', 'Puerto Rico potshots make his racism morally impossible to ignore', 'another clearly calculated, yet graceful gesture to Americans in need', 'Call Out President Trump on His Response to Puerto Rico Crisis', 'Trump attacks San Juan mayor over hurricane response', 'Dedicating Golf Trophy To Hurricane Victims', 'Trump Dedicates a Golf Trophy to Hurricane Victims', 'Mulvaney criticizes San Juan', 'Trump dedicates golf trophy', 'Trump congratulates himself on Puerto Rico response, heads to golf course', '600 billion a year can do so much', '600 billion a year on the military if we can', 'Good-at-Words-Talking Describes Puerto Rico Death Toll as', 'Appreciates The Congrats On Tremendous Job He', 'puerto rico tweets are unspeakable', 'update on Puerto Rico', 'even fucking mobilize 50 helicopters, rescue forces, and a bunch of military aid', 'struggles with basics of being POTUS', 'everyone that was in the Intensive Care Unit, died', 'Puerto Rican Troops Are Still Waiting for Orders While Residents Cry for Help', 'travels to New Jersey to watch a golf tournament', 'half of Puerto Ricans without access to drinking water', 'Who would attack London mayor in midst of terror attack, San Juan mayor during disaster', 'Tweets on Puerto Rico Are a National Disgrace', 'big water', 'Politically Motivated Ingrate']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Charities on the ground in Puerto Rico: [Project Hope](http://www.projecthope.org/) | [ConPRmetidos](https://www.generosity.com/emergencies-fundraising/maria-puerto-rico-real-time-recovery-fund) | [Direct Relief](https://secure.directrelief.org/site/Donation2) | [Hispanic Federation](https://hispanicfederation.org/unidos/) \n\n"
        "[^(Charity Navigator)](https://www.charitynavigator.org/index.cfm?compare=4367%2C3626%2C4997&bay=search.compare) \n\n"
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