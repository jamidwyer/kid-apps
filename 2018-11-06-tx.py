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
        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['changing Democratic politics in Texas', 'Optimistic About Climate Change in 2018', 'As U.S. women go to jail in record numbers, who', 'txgov', 'larry kilgore', 'Democrats Leave Few Seats Unchallenged', 'Thousands Of Layoffs, Firings Just In Time For Christmas', 'Attorneys general who aren\'t suing to protect net neutrality', 'political action committee aimed at unseating anti-marijuana lawmakers', '6, killed by police days before Christmas', 'Like where do we draw the line', 'Jan. 7th at source gaming lounge', 'driving American women to vote', 'Republicans have finally repealed a crucial piece of Obamacare', 'overtly political and satirical yard display', 'Actually Simplify The Tax Code', 'get our city to create a local broadband', 'Battleground Texas: 2018 Edition', 'Texas House of Representatives and State Senate, 2018', 'michael c. burgess', 'Dems hold biggest lead in congressional preference', 'smarmsplaining', 'smarm-splaining', 'smarm-spaining', 'Hurricane Harvey roughly 3 times more likely', 'Federal protections for state medical marijuana laws hang in the balance', 'most insulting thing y\'all have ever seen', 'Brady says final tax bill', 'Sick of All The Health Care Freeloaders', 'Members of Congress Who Just Told Ajit Pai to Repeal Net Neutrality', 'Letter Supporting the End of Net Neutrality', 'climate change and Hurricane Harvey', 'texas gop congressman', '2018 House district polling so far', 'Warming made Harvey', 'Democrats Must Compete Everywhere', 'Texas Democrats Are Running', 'randy weber', 'rep. weber', 'Representative weber', 'congressman weber', 'rep weber', 'Congressman prays for forgiveness for allowing gay marriage and abortion', 'GOP congressman Wept As He Begged God To Forgive', 'take all groundwater from Texas community', 'What happens when libertarians run a city', 'swamped by ideology, lobbying, math', '\'dark money\' political contributions tax deductible', 'so shocked Nd so happy about 13 people showed up', 'resigned due to sexual harassment allegations', 'Texas Democrats prepare', 'tax plan riddled with glitches', 'tx31', 'vanessa adia', 'kevin brady', 'Radical Provisions In The GOP Tax Bill', 'roger williams', 'beto is in town', 'college from endowment tax. It is owned by Betsy DeVos', 'benefit DeVos-linked conservative college', 'cruz amendment', 'sold me, my fellow Houstonians, and this nation to the telecom lobby', 'House Republicans agree to select speaker candidate in caucus', 'Congressmen and Senators representing the Austin area', 'fellow Texans to the telecom lobby', 'Texas Politicians Spun a Tale', 'Cruz on whether Senate should expel Moore', 'lupe valdez', 'Dallas County sheriff says she hasn', 'The Founders would have opposed seizing land for Trump', 'train 50k candidates in 2018', 'reason for the uptick in earthquakes in DFW', 'Democratic challenger officially files for Senate', 'The House GOP tax bill is bad for Texas teachers', 'Drilling Reawakens Sleeping Faults in Texas', 'Senators Sanders and Cruz', 'medrick yhap', 'joe barton', 'Texas Congressman on tape tells woman he would report her to Capitol Police', 'rep. roger williams', 'Justice Democrats Just Endorsed Five New Progressive Candidates', 'ted cruz', 'sen. cruz', 'senator cruz', 'ted. cruz', '35 and 12th', '5 Republicans who could challenge Trump in 2020', 'Trump feuds endangering tax reform', 'middle-class Americans, including Texans, will see a tax increase', 't Work So Well for F.D.R.', 'Republicans Are Unsure What Trump Wants on Health Care', 'Texas Voters Familiar With Cruz', 'Cruz claims repealing the estate tax', 'Bernie calls GOP tax plan a \'Robin Hood proposal in reverse', 'Sanders, Cruz spar', 'Ted Lies Again', 'tedcruz', 'sanders vs. cruz', 'Bernie Sanders Tax Reform debate MegaThread', 'tries to sell tax reform to Democrats', 'for at Least 3rd Time in Two Months', 'Republicans Worry They\'ll Lose Congress', 'Republicans fear a \'bloodbath\' in midterm elections', 'Cruz: GOP could face', 'Watergate-level blowout', 'Cruz warns Koch donors re', 'CRUZ: MAYBE NEXT YEAR', 'Sanders, Cruz to Square Off Over in a Debate Over GOP', 'except Cruz', 'Cruz, Sanders to debate Trump', 'Cruz town hall debate on taxes', 'Where GOP senators stand on President Trump', 'Austin political consultant worked for Germany', 'Favorite Meme-Maker is Now Helping the Far-Right in Germany', 'Cruz grapples with GOP inaction under Trump', 'what democrats must do', 'morally repugnant and bad economic policy', 'collapse escalates Republican infighting', 'Republicans look to next year for Obamacare repeal', 'GOP already eyeing next chance', 'guts Obamacare even more', 'But They Just Might, Anyway', 'Al Franken keeps jabbing at Ted Cruz', 'outlines four-step plan to Medicare for all', 'pass this final test before it can come to a vote', 'GOP takes heavy fire over pre-existing conditions', 'insurer bailout could turn Texas blue', 'PolitiFact: Cruz and O', 'dis cruz', 'Cruz Bill Eases Revocations of U.S. Citizenship Without Due Process', 'states like Texas to request federal assistance after Harvey', 'Texas Congressmen voted against Sandy relief, now are begging for Harvey relief', 'hypocrisy on Harvey aid', 'Texas Lawmakers Who Voted Against Relief for Hurricane Sandy', 'Texas Republicans voted against aid', 'Her New Sticker Says FUCK the Sheriff', 'discourage women from getting abortions. Republicans claim they don', 'Congressional Republicans block vote on amendment to let marijuana businesses use banks', 'texas district 07', 'hitting fire code limits, running out of parking spaces, and spilling out of living rooms and into yards', 'Can Democrats retake Southern legislatures', 'The Good Old Boys in the Texas Legislature', 'pete sessions', 'rep. sessions', 'rep sessions', 'representative sessions', 'congressman sessions', '13 polls in GOP-held House districts conducted', 'john culberson', 'rep. culberson', '@congculberson', 'culberson\'s texas', 'congressman culberson', 'rep culberson', 'GOP strategists worry incumbents aren', 'kenny marchant', 'rep. marchant', 'Rep (Marchant)', 'congressman marchant', 'rep marchant', 'letitia plummer', 'pete olson', 'rep. olson', 'rep olson', 'representative olson', 'congressman olson', 'tx-22', 'tx22', 'ted poe', 'H.R. 620', 'hr 620', 'Republicans are deciding they want no part of the 2018 elections', 'tx-02', 'rep poe', 'representative poe', 'congressman poe', 'rep. poe', '^(?!.*anthony lamar smith).*lamar smith.*$', 'Where All 533 Members of Congress Stand on Bump Stocks', 'house science committee chair', 'tx-21', 'tx21', 'john carter', 'disaster funds cut to finance wall', 'tx-31', 'House DACA deal won\'t need Democratic votes', 'farenthold', 'tx-27', 'Congress plays by different rules on sexual harassment and misconduct', 'hensarling', 'gohmert', 'tx-01', 'brian babin', 'rep. babin', 'rep babin', 'representative babin', 'congressman babin', 'greg abbott', 'texas governor', 'TX\'s next governor ', 'Texans are more open to legalizing marijuana', 'Harvey Relief Program Nixes Requirement to Not Boycott Israel', 'caveat is the result of a strange new state law', 'Abbott Plan to Amend Constitution', 'Texas Is No Longer Feeling Miraculous', 'The Racist Map Wins', 'Democrats Must Take a Shot at Texas', 'Federal Judge Blocks Texas', 'rolando pablos', 'Texas Republican turns down donated blankets', 'Judge blocks provisions in Texas law punishing \'sanctuary cities\'', 'bill restricting insurance coverage of abortion', 'governor of texas', 'tx gov', 'runs for governor in Texas', '@gregabbott_tx', 'Texas crackdown on sanctuary cities', 'sb-4', 'sb4', 'sb 4', 'Senate Bill 4', 'rape insurance', 'Texas\' redistricting fight', 'tx governor\'s', 'ken paxton', 'texas attorney general', 'Another reason AG\'s are important in 2018.', 'future of DACA suddenly looks very shaky', 'immigrants in Houston brace for a DACA decision', 'distract from his own felony trial', 'Courts repeatedly chastise Texas for voting-rights violations', 'Fix Its Discriminatory Voting Laws', 'michael burgess', 'rep. burgess', 'rep burgess', 'representative burgess', 'congressman burgess', 'tx-26', 'tx26', 'will fisher', 'Michael McCaul', 'rep. mccaul', 'Representative mccaul', 'congressman mccaul', 'rep mccaul', 'mike mccaul']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Texas 2018 Election \n\n"
            "[Primary Election Registration Deadline](http://www.votetexas.gov/register-to-vote/): February 5, 2018 \n\n"
            "[Primary Election](https://teamrv-mvp.sos.texas.gov/MVP/mvp.do): March 6, 2018 \n\n"
            "[General Election Registration Deadline](http://www.votetexas.gov/register-to-vote/): October 9, 2018 \n\n"
            "[General Election](https://teamrv-mvp.sos.texas.gov/MVP/mvp.do): November 6, 2018 \n\n")
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