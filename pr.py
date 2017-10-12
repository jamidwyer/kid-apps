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
            terms = ['Puerto Ricans are drinking water from hazardous waste sites', 'FEMA dodges questions about Puerto Rico', 'Dead in Puerto Rico', 'Drinking Water From Wells at Hazardous Waste “Superfund” Sites in Puerto Rico', 'Puerto Rico city Trump visited is still without power', 'Puerto Rico city Trump visited is still without power', 'Puerto Rico Needs A Major Military Rescue Operation Now', 'Only one ship headed to Puerto Rico', 'Most of Puerto Rico has been in the dark for 21 days', 'Three Weeks After Maria'', 'Weeks After Hurricane, Puerto Rico Lacks Water, Working Hospitals, Electricity', '3 weeks after Hurricane Maria', 'I don’t give a damn', 'Playing Defense on Hurricane Maria', 'Nurses and Labor Unions Join Puerto Rico Relief', 'Three weeks after Hurricane Maria hit Puerto Rico just 10', 'San Juan Mayor Carmen Yulin Cruz on Trump exchange', 'FEMA has been deleting facts', 'deaths in Puerto Rico is at odds with the official count', 'Trump Pushes More Loans on Devastated Puerto Rico', 'Puerto Rico Relief Bill Cancels', 'US officials privately acknowledge serious food shortage', 'Residents in Puerto Rico Still Don’t Have Drinking Water', 'Not our job to distribute food and water in Puerto Rico', 'Donald Trump Pretty Proud He Invented Puerto Rico', 'FEMA is lying to us about Puerto Rico', 'Puerto Rico Is a Symptom of America', 'politics, lack of unity, hindering hurricane response', 'Trump heartlessly jacks up food costs for Puerto Rico', 'Jones Act waiver expires for Puerto Rico', 'Puerto Rico Jones Act waiver expire', 'Puerto Rican Roots Challenge Trump', 'Waiver encouraging foreign supply ships to reach Puerto Rico has expired', 'Puerto Rican Hospitals Are Still Desperate for Fuel', 'millions less in donations than the mainland', 'We filtered out the mayor a long time ago', 'done for Puerto Rico with so little appreciation', 'As Puerto Rico Still Without Electricity And Food', 'A mayor in Puerto Rico calls for FEMA help', 'Trump defends throwing paper towels', 'beautiful, soft towels', 'filtered out\' Puerto Rican mayor\'s calls for help' 'Trump makes 69th trip to a golf course while San Juan', 'desperate san juan mayor', 'the cost of a lack of political representation', 'Accent Is Impressively Bad', 'pointing fingers at Puerto Rico', 'FEMA restores deleted Puerto Rico stats', 'deleted data on puerto rico', 'particular racism towards Puerto Ricans', 'Why Did FEMA Remove Stats About Puerto Rico', 'It is inarguable that Trump hates the Puerto Ricans', 'the definition of adding insult to injury', 'Only Half of Puerto Rico Has Clean Water', 'statistics about drinking water access and electricity in Puerto Rico from website', 'Berlin Airlift', 'stats on Puerto Rico recovery', 'dead in Puerto Rico are underreported', 'in the Wealthy Suburbs', 'Could Pay to Send Puerto Rico 128 Cargo Ships With Aid', 'End Insulting Tweets and Start Rebuilding Puerto Rico', 'Great visit. Really lovely... I enjoyed it very much', 'Puerto Rican Debt Comments Have Spooked Investors', 'already paid to rebuild Puerto Rico', 'death toll in Puerto Rico is higher than official count', 'US Presidents interacting with their people in times of need', 'Minimized Our Suffering', 'following him on Twitter and watching him on cable TV when they don\'t even have electricity or potable water', 'make up Puerto Rican truck strike to absolve Trump', 'threw paper towels at Puerto Ricans', 'the dead have not been counted yet', 'Oxfam slams the Trump administration', 'example of Trump only serving his base', 'throwing relief supplies into the crowd on Puerto Rico', 'POTUS handed out flashlights to Puerto Ricans, joking ', 'Trump says Puerto Rico officials should be', 'Puerto Rico and How Trump Responds to Tragedy', 'Trump Calls Puerto Rico Recovery a', 'Did Trump Mix Up The Air Force And Coast Guard', 'Trump in Puerto Rico', 'Death toll in Puerto Rico from Hurricane Maria climbs to 34', 'Hurricane Maria Could Change the Politics of Puerto Rico', 'Throwing Paper Towels At Them', 'trump tosses paper towels', 'official death count to 34', 'death toll has risen to 34', 'Puerto Rico death toll risen to 34', 'Well, It Sounded Good When He Said It', 'Trump tells Puerto Ricans that they have been lucky', 'President Trump just set a new standard in his search for flattery', 'Trump is Not Planning to Rebuild Puerto Rico', 'Trump meme is running like crazy in my social media', 'truck drivers for refusing to ship relief supplies', 'Trump throws paper towels', 'lobs paper towel rolls', 'real catastrophe', 'trump\'s katrina', 'update on Puerto Rico', 'big water']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Charities on the ground in Puerto Rico: [Project Hope](http://www.projecthope.org/) | [ConPRmetidos](https://www.generosity.com/emergencies-fundraising/maria-puerto-rico-real-time-recovery-fund) | [Direct Relief](https://secure.directrelief.org/site/Donation2) | [Hispanic Federation](https://hispanicfederation.org/unidos/) \n\n"
        "[^(Charity Navigator)](https://www.charitynavigator.org/index.cfm?compare=4367%2C3626%2C4997&bay=search.compare) \n\n"
            "[Updated local information about Puerto Rico](http://www.univision.com/univision-news/united-states/find-updated-information-about-your-town-in-this-puerto-rico-search-engine) \n\n")
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