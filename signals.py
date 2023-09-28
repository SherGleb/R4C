from django.dispatch import receiver
from django.db.models.signals import post_save
from orders.models import *
from customers.models import *
from robots.models import *
from utils import EmailSender


@receiver(post_save, sender=Robot)
def send_notification(sender, instance, created, **kwargs):
    if created:
        new_robots = Robot.objects.filter(serial=instance.serial)
        if len(new_robots) == 1:
            waiting_order = Order.objects.filter(robot_serial=instance.serial)
            if len(waiting_order) != 0:
                email_sender = EmailSender()
                for ords in waiting_order:
                    email = Customer.objects.filter(id=ords.customer.id)[0].email
                    email_sender.send_email(email, new_robots[0].model, new_robots[0].version)

