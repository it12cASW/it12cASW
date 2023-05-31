
status = ['new', 'progress', 'closed', 'rejected', 'info', 'test']

status_order = {'new': 0,
                'progress': 1,
                'closed': 2,
                'rejected': 3,
                'info': 4,
                'test': 5,
                'posponed': 6,}

prioridades = ["baja", "media", "alta", "ninguna"]


STATUS_CHOICES = (
        ('new', 'new'),
        ('progress', 'progress'),
        ('closed', 'closed'),
        ('rejected', 'rejected'),
        ('info', 'info'),
        ('test', 'test'),
        ('posponed', 'posponed'),
    )