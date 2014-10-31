import twitter

from dateutil.parser import parse

from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import TwitterConfig


class TwitterCredentialsNotSupplied(Exception):
    pass


class TwitterPlugin(CMSPluginBase):
    model = TwitterConfig
    name = _("Twitter Feed")
    render_template = "cmsplugin_twitter/feed.html"

    def render(self, context, instance, placeholder):
        try:
            consumer_key = settings.TWITTER_CONSUMER_KEY
            consumer_secret = settings.TWITTER_CONSUMER_SECRET
            access_token_key = settings.TWITTER_ACCESS_TOKEN_KEY
            access_token_secret = settings.TWITTER_ACCESS_TOKEN_SECRET
        except AttributeError:
            raise TwitterCredentialsNotSupplied("""
                Twitter credentials have not been supplied in your
                settings, please provide them in the format of
                TWITTER_{credential}, such as TWITTER_CONSUMER_KEY
            """)

        api = twitter.Api(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token_key=access_token_key,
            access_token_secret=access_token_secret
        )

        feed = api.GetUserTimeline(
            screen_name='rootscamp',
            count=instance.number_of_tweets
        )

        formatted_feed = []

        for tweet in feed:
            print tweet
            tweet.created_at = parse(tweet.created_at)
            formatted_feed.append(tweet)

        context.update({
            'object': instance,
            'placeholder': placeholder,
            'feed': formatted_feed
        })

        return context

plugin_pool.register_plugin(TwitterPlugin)
