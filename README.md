# dockercon-twitter
A Raspberry Pi based monitor which uses the Twitter search API to find tweets & tweeters using #DockerCon!

## Running

`docker run -ti --privileged --device /dev/gpiomem:/dev/gpiomem --env-file=./.env --restart=on-failure developius/dockercon-tweet-monitor:latest`

## Building (optional)

`docker build -t developius/dockercon-tweet-monitor .`
