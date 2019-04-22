# Tweepy Twitter Stream Example

This is my attempt at creating a well documented example of streaming Twitter using the Python package called Tweepy. I have searched high and low and most examples are either outdated or are very small and don't showcase enough or explain anything.

# What this does

With FollowerMode set to True, this will stream tweets from a user-defined list of Twitter accounts. With FollowerMode set to False, you can stream from all accounts with user-defined keyword filters. This contains an optional JSON storage feature inside of it that is commented out.

Curious on if it it can faster? Although it already streams fairly fast, some people might want access to a higher rate for special use cases. It is possible using something called Firehose made by Twitter, but it is only meant for large enterprise use and must be specially applied for by contacting their sales team. No idea on how much it costs. It's also not supported by Tweepy.

# Requirement

You will need a twitter API access key. It's not hard to get. 
Sign up for one at https://developer.twitter.com/en/apply-for-access.html
Once you have your API keys, scroll 1/3 of the way down the script and look for 'AUTHENTICATION' and add your API key there.

----------------------------------------------



Tidbit - I most definitely enjoy sharing code with others and helping people for free without EVER asking anything in return, but if you found this example useful and would like to buy me a cup of coffee or something, feel free to send a dollar or two to paypal.me/jhayes88 if you'd like. Tips are always appreciated <3 
