# dockercon-twitter
A Raspberry Pi based monitor which uses the Twitter search API to find tweets & tweeters using #DockerCon!

## Running

`docker run -ti --rm --privileged --device /dev/gpiomem:/dev/gpiomem --env-file=./.env --restart=failure developius/dockercon-tweet-monitor`

## Building

`docker build -t developius/dockercon-tweet-monitor .`
