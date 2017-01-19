# linode-ddns

A service for using a Linode DNS entry as a home dynamic DNS. It's meant to be pushed to something like [Heroku](https://heroku.com) or
a [Dokku](http://dokku.viewdocs.io/dokku/) server (what I do). It's a simple API that will grab the IP from the request
and update a DNS entry with said IP if it differs from the current value using the [Linode API](https://www.linode.com/api).

It requires a few environment variables to run:

```bash
# ID of the domain in Linode
LINODE_DOMAIN_ID=000000
# ID of the resource (record) to update
LINODE_RESOURCE_ID=0000000
# Your Linode API key (can be generated in your profile)
LINODE_API_KEY=sssshhhh-itsa-sekrit
# The key required to use your service
API_KEY=whatever-you-want
```

Then you simply setup a cron on a box on your network to run the following:

```bash
$ curl -d "api_key=the-api-key-you-set-above" https://your-ddns-app.herokuapp.com
```

The values will be different obviously, and you'll host it where you want. 
To work it just needs to be outside of your home network.

Enjoy
