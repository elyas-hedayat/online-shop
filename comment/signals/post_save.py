from django.db.models import signals
from django.dispatch import receiver

from comment.conf import settings
from comment.models import (
    Comment,
    Flag,
    FlagInstance,
    Follower,
    Reaction,
    ReactionInstance,
)


@receiver(signals.post_save, sender=Comment)
def add_initial_instances(
    sender, instance, created, raw, using, update_fields, **kwargs
):
    if created:
        Reaction.objects.create(comment=instance)
        Flag.objects.create(comment=instance)
        if settings.COMMENT_ALLOW_SUBSCRIPTION:
            Follower.objects.follow_parent_thread_for_comment(comment=instance)


@receiver(signals.post_save, sender=FlagInstance)
def increase_count(sender, instance, created, raw, using, update_fields, **kwargs):
    if created:
        instance.flag.increase_count()
        instance.flag.toggle_flagged_state()


@receiver(signals.post_save, sender=ReactionInstance)
def add_count(sender, instance, created, raw, using, update_fields, **kwargs):
    if created:
        instance.reaction.increase_reaction_count(instance.reaction_type)
