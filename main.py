# -*- coding: utf-8 -*-
import twitter, pytz, time, math, os
from dateutil import parser
from datetime import datetime, timedelta
from gpiozero import AngularServo

left = AngularServo(18, min_angle = 180, max_angle = 0, min_pulse_width=0.7/1000, max_pulse_width=2.3/1000)
right = AngularServo(15, min_angle = 180, max_angle = 0, min_pulse_width=0.7/1000, max_pulse_width=2.3/1000)

left.mid()
right.mid()
time.sleep(0.25)
left.detach()
right.detach()
time.sleep(10)

# adapted from http://stackoverflow.com/a/1969274/2822450
def translate(value, leftMin, leftMax, rightMin, rightMax):
	# Figure out how 'wide' each range is
	leftSpan = leftMax - leftMin
	rightSpan = rightMax - rightMin

	# Convert the left range into a 0-1 range (float)
	valueScaled = float(value - leftMin) / float(leftSpan)

	# Convert the 0-1 range into a value in the right range.
	output = rightMin + (valueScaled * rightSpan)

	# stop servos clashing
	if output > 180: return 180
	if output < 45: return 45

	if output > rightMax: return rightMax
	elif output < rightMin: return rightMin
	else: return output

api = twitter.Api(
	consumer_key=os.environ['CONSUMER_KEY'],
	consumer_secret=os.environ['CONSUMER_SECRET'],
	access_token_key=os.environ['ACCESS_TOKEN_KEY'],
	access_token_secret=os.environ['ACCESS_TOKEN_SECRET']
)

while True:
	tweets = api.GetSearch(raw_query='q=%23dockercon&result_type=recent&count=200')
	new_tweets = []
	tweeters = []

	# the result set is ordered by created_at so we can loop & break
	for tweet in tweets:
		if parser.parse(tweet.created_at) > pytz.utc.localize(datetime.now()) - timedelta(hours=1): new_tweets.append(tweet) # in last hour
		else: break # stale tweets

	for tweet in new_tweets:
		#print('[{}] {} - "{}"'.format(tweet.created_at.encode('utf-8'), tweet.user.name.encode('utf-8'), tweet.text.encode('utf-8')))
		if tweet.user.id not in tweeters: tweeters.append(tweet.user.id)

	left.angle = round(translate(len(tweeters), 0, 50, 0, 180))
	right.angle = round(translate(len(new_tweets), 0, 50, 0, 180))
	print('{} unique tweeters ({})º, {} #DockerCon tweets ({})º'.format(len(tweeters), left.angle, len(new_tweets), right.angle))

	time.sleep(0.4) # allow servos to move into position
	left.detach()
	right.detach()
	time.sleep(5 - 0.4)
