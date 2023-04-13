
status = ['NUEVO', 'EN_PROCESO', 'FINALIZADO', 'CANCELADO', 'NECESITA_INFORMACION', 'LISTA_PARA_TESTEAR']

status_order = {'NUEVO': 0,
                'EN_PROCESO': 1,
                'FINALIZADO': 2,
                'CANCELADO': 3,
                'NECESITA_INFORMACION': 4,
                'LISTA_PARA_TESTEAR': 5}

prioridades = ["baja", "media", "alta", "ninguna"]

STATUS_CHOICES = (
        ('NUEVO', 'Nuevo'),
        ('EN_PROCESO', 'En proceso'),
        ('FINALIZADO', 'Finalizado'),
        ('CANCELADO', 'Cancelado'),
        ('NECESITA_INFORMACION', 'Necesita información'),
        ('LISTA_PARA_TESTEAR', 'Lista para testear'),
    )