# dockercon-twitter
A Raspberry Pi based monitor which uses the Twitter search API to find tweets & tweeters using #DockerCon!

## Running

Create a `.env` file in the current directory with these lines, then save & close it:

```
CONSUMER_KEY=<twitter consumer key>
CONSUMER_SECRET=<twitter consumer secret>
ACCESS_TOKEN_KEY=<twitter access token key>
ACCESS_TOKEN_SECRET=<twitter access token secret>
```

`docker run -ti --privileged --device /dev/gpiomem:/dev/gpiomem --env-file=./.env --restart=always developius/dockercon-tweet-monitor:latest`

## Building (optional)

`docker build -t developius/dockercon-tweet-monitor .`
