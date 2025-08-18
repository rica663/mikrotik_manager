from django.db import models

class MikrotikDevice(models.Model):
    STATUS_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('unknown', 'Unknown'),
    ]

    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    api_port = models.IntegerField(default=8728)
    secret_ref = models.CharField(max_length=255)  # Ref para Vault
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unknown')

    def __str__(self):
        return self.name

    def test_connection(self):
        # Implementar usando librouteros ou Netmiko
        # Por enquanto, apenas um placeholder
        return self.status == 'online'


