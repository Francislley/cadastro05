from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length = 10)
    senha = models.CharField(max_length = 6)
    
    def __unicode__(self):
        return self.nome
        
    
