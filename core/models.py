from django.db import models


class ArenaRule(models.Model):
    description = models.TextField()
    arena = models.ForeignKey("Arena", related_name="rules", on_delete=models.CASCADE)


class TopicRule(models.Model):
    description = models.TextField()
    topic = models.ForeignKey("Topic", related_name="rules", on_delete=models.CASCADE)


class Tag(models.Model):
    label = models.CharField(max_length=255)


class Arena(models.Model):
    description = models.TextField()
    token_contract_address = models.CharField(max_length=255)

    min_contribution_amount = models.IntegerField()

    fund_address = models.CharField(max_length=255)
    arena_fund_fee_percentage = models.FloatField(default=0)

    allow_topic_funds = models.BooleanField(default=False)
    allow_choice_funds = models.BooleanField(default=False)

    topic_creation_fee = models.FloatField()
    choice_creation_fee = models.FloatField()

    tags = models.ManyToManyField(Tag)


class Topic(models.Model):
    description = models.TextField()
    arena = models.ForeignKey(Arena, related_name="topics", on_delete=models.CASCADE)

    create_datetime = models.DateTimeField()
    cycle_duration = models.DurationField()

    transfer_period = models.DurationField()

    choice_min_support_threshold = models.FloatField(default=0)

    share_per_cycle_percentage = models.FloatField(default=0)
    prev_contributors_fee_percentage = models.FloatField(default=0)

    topic_fund_address = models.CharField(max_length=255, blank=True, null=True)
    topic_fund_fee_percentage = models.FloatField(default=0)

    allow_choice_funds = models.BooleanField(default=False)

    max_target_amount = models.FloatField()

    tags = models.ManyToManyField(Tag)
    # todo: how should the end of a topic be described? for example in terms of how many cycles have passed?


class Choice(models.Model):
    topic = models.ForeignKey(Topic, related_name="choices", on_delete=models.CASCADE)
    description = models.TextField()

    choice_fund_address = models.CharField(max_length=255)
    fee_percentage = models.FloatField(default=0)

    target_amount = models.FloatField()
