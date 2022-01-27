from django.db import models


class ArenaRule(models.Model):
    description = models.TextField()
    arena = models.ForeignKey("Arena", related_name="rules", on_delete=models.CASCADE)


class TopicRule(models.Model):
    description = models.TextField()
    topic = models.ForeignKey("Topic", related_name="rules", on_delete=models.CASCADE)


class Token(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)


class Tag(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)


class Arena(models.Model):
    description = models.TextField()
    token = models.ForeignKey(Token, related_name="arenas", on_delete=models.CASCADE)
    min_contribution_amount = models.IntegerField()

    fund_address = models.CharField(max_length=255)
    percent_fee = models.FloatField(default=0)

    allow_topic_funds = models.BooleanField(default=False)
    allow_choice_funds = models.BooleanField(default=False)

    tags = models.ManyToManyField(Tag)


class Topic(models.Model):
    description = models.TextField()
    arena = models.ForeignKey(Arena, related_name="topics", on_delete=models.CASCADE)
    cycle_duration = models.DurationField()

    topic_duration_in_cycles = models.IntegerField()

    share_per_cycle_percentage = models.FloatField(default=0)

    choice_min_support_threshold = models.FloatField(default=0)
    choice_min_support_duration = models.DurationField()

    prev_contributors_fee_percentage = models.FloatField(default=0)

    topic_fund_address = models.CharField(max_length=255, blank=True, null=True)
    topic_fund_fee_percentage = models.FloatField(default=0)

    allow_choice_funds = models.BooleanField(default=False)

    tags = models.ManyToManyField(Tag)
    # todo: how should the end of a topic be described? for example in terms of how many cycles have passed?


class Choice(models.Model):
    topic = models.ForeignKey(Topic, related_name="choices", on_delete=models.CASCADE)
    description = models.TextField()

    conflicts_with = models.ManyToManyField("Choice")

    choice_fund_address = models.CharField(max_length=255)
    fee_percentage = models.FloatField(default=0)

    target_amount = models.IntegerField(default=10000000000)
