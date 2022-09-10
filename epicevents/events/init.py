

def event_status_init():
    from events.models import EventStatus
    eventstatus = EventStatus.Status
    for name in eventstatus:
        EventStatus.objects.get_or_create(status=name)
    for event in list(EventStatus.objects.all()):
        try:
            event.Status(event.status)
        except ValueError:
            EventStatus.objects.get(status=event).delete()
