import json
import tweepy
def main():
    # TODO implement

    client = tweepy.Client(consumer_key='BzH4m1dbb7g9l0q706gbwZxc5',
                       consumer_secret='x0ABUm2L2ZGAvPeccC2N3k6cGujb1Vzp1BLicQerlgjmuLepbJ',
                       access_token='1471481605785108480-8yhsNAAfQkA918EoUS5pHdrrNxXnfm',
                       access_token_secret='IqM4eM9wcYGHyIqpXZ069dYdtHs3Fh7sw4yFT1LVt07LV')



     # Standard tweet
    tweet = "Test Tweet"

    ## Tweet with media (multiple images)
    client.create_tweet(text=tweet)

    response = client.create_tweet(text=tweet)

    print("Hello World")

















    return {
        "statusCode": 200,
        "body": json.dumps({
            "abc": ip.status_code,
            "message": os.environ.get('MyParam')
        }),
    }

main()