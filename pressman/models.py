# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
 
class PressMan(models.Model):
    pr_name = models.CharField(max_length=255, verbose_name='Nombre', help_text="Nombre de Autor")
    pr_email = models.EmailField(verbose_name='e-mail', help_text="Correo eletronico Autor")
    pr_url = models.URLField(verbose_name='URL', help_text="URL del Autor")
    
    def __unicode__(self):
       return u'%s %s %s' %(self.pr_name, self.pr_email, self.pr_url)
    class Meta:
        ordering = ['pr_name']
        verbose_name = "Autore"
        
    
class PressRelease(models.Model):
       pr_title = models.CharField(max_length=100)
       pr_body = models.TextField(max_length=255, verbose_name='Nombre', help_text="Nombre de Autor")
       pr_author = models.ForeignKey(PressMan)
       pr_date_created = models.DateTimeField(default=datetime.now, auto_now = False, editable=False, verbose_name='Fecha de creación del articulo')
       
       def __unicode__(self):
        return u'%s %s %s' %(self.pr_title, self.pr_body, self.pr_date_created)
    
       class Meta:
        ordering = ['pr_title']
        verbose_name = "Publicacione"