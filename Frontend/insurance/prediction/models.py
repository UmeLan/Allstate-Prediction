from django.db import models
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib import admin

# Create your models here.
class Customer(models.Model):
    customer_ID=models.CharField(max_length=500)
    state_group=models.IntegerField(default=1)
    group_size=models.IntegerField(default=1)
    homeowner=models.IntegerField(default=0)
    car_age=models.IntegerField(default=1)
    car_value=models.IntegerField(default=1)
    risk_factor=models.IntegerField(default=1)
    married_couple=models.IntegerField(default=0)
    C_previous=models.IntegerField(default=1)
    duration_previous=models.IntegerField(default=1)
    cost=models.IntegerField(default=600)
    timeofday=models.IntegerField(default=1)
    weekend=models.IntegerField(default=1)
    family=models.IntegerField(default=1)
    agedif=models.IntegerField(default=1)
    individual=models.IntegerField(default=1)
    def __str__(self):
        return self.customer_ID
    def get_absolute_url(self):
        return reverse('customerList')

    @property
    def A(self):
        if self.car_age <= 11:
            if self.cost <= 568 :
                if self.cost <= 554:
                    a=0
                else:
                    a=0
            else:
                if self.car_age <= 8:
                    a=1
                else:
                    a=1
        else:
            if self.cost <=595:
                if self.risk_factor <=1:
                    a=0
                else:
                    a=0
            else:
                if self.car_age <=14:
                    a=1
                else:
                    a=0
        return a

    @property
    def B(self):
        if self.cost <= 584:
            if self.cost <= 567:
                if self.state_group <=3:
                    b = 0
                else:
                    b=0
            else:
                b=0
        else:
            if self.state_group <= 3:
                if self.car_age <= 12:
                    b=0
                else:
                    b=0
            else:
                if self.car_age <= 13:
                    b=1
                else:
                    b=0
        return b

    @property
    def C(self):
        if self.C_previous<=2:
            if self.C_previous <=1:
                if self.C_previous <=0:
                    if self.state_group <=3:
                        c=0
                    else:
                        c=0
                else:
                    c=0
            else:
                if self.C_previous >3:
                    if self.homeowner<=0:
                        if self.risk_factor <=2:
                            c=3
                        else:
                            c=2
                    else:
                        c=3
                else:
                    if self.C_previous >2:
                        if self.homeowner <=0:
                            if self.risk_factor <=2:
                                c=2
                            else:
                                c=2
                        else:
                            if self.cost <= 554:
                                c=2
                            else:
                                c=2
                    else:
                        if self.C_previous >1:
                            if self.state_group <=3:
                                if self.state_group <=1:
                                    c=1
                                else:
                                    c=1
                            else:
                                if self.homeowner <=0:
                                    c=1
                                else:
                                    c=1
                        else:c=2
        else:
            c=3
        return c

    @property
    def D(self):
        if self.C_previous<=2:
            if self.C_previous<=1:
                if self.risk_factor<=1:
                    if self.state_group<=4:
                        d=3
                    else:
                        d=1
                else:
                    if self.cost<=584:
                        d=1
                    else:
                        d=1
            else:
                if self.state_group<=3:
                    d=1
                else:
                    if self.risk_factor<=1:
                        d=3
                    else:
                        d=2
        else:
            if self.C_previous<=3:
                if self.state_group<=3:
                    if self.homeowner<=0:
                        d=3
                    else:
                        d=3
                else:
                    if self.cost<=567:
                        d=3
                    else:
                        d=3
            else:
                if self.cost<=552:
                    if self.car_age<=5:
                        d=1
                    else:
                        d=3
                else:
                    d=3
        return d

    @property
    def E(self):
        if self.car_age<=10:
            if self.cost<=595:
                if self.cost<=568:
                    e=0
                else:
                    e=0
            else:
                if self.state_group<=4:
                    e=1
                else:
                    e=0
        else:
            e=0
        return e

    @property
    def F(self):
        if self.state_group <=3:
            if self.state_group <=2:
                if self.cost<=584:
                    if self.car_age<=11:
                        if self.cost<=553:
                            if self.state_group<=1:
                                f=0
                            else:
                                f=0
                        else:
                            if self.C_previous<=2:
                                if self.duration_previous<=4:
                                    if self.state_group<=1:
                                        f=0
                                    else:
                                        f=0
                                else:
                                    if self.cost<=568:
                                        f=0
                                    else:
                                        f=2
                            else:
                                if self.homeowner<=0:
                                    if self.state_group<=1:
                                        f=0
                                    else:
                                        f=2
                                else:
                                    f=2
                    else:
                        if self.C_previous<=2:
                            if self.risk_factor<=1:
                                if self.duration_previous<=4:
                                    if self.cost<=577:
                                        f=0
                                    else:
                                        f=2
                                else:
                                    if self.homeowner<=0:
                                        f=0
                                    else:
                                        f=2
                            else:
                                f=0
                        else:
                            if self.cost<=553:
                                f=0
                            else:
                                if self.cost>568:
                                    f=2
                                else:
                                    f=0
                else:
                    if self.car_age<=11:
                        if self.C_previous<=2:
                            if self.cost<=613:
                                if self.duration_previous<=3:
                                    if self.car_age<=8:
                                        f=2
                                    else:
                                        f=0
                                else:
                                    f=2
                            else:
                                f=2
                        else:
                            if self.state_group<=1:
                                if self.duration_previous<=5:
                                    if self.car_age<=8:
                                        f=2
                                    else:
                                        f=2
                                else:
                                    if self.car_age<=10:
                                        f=2
                                    else:
                                        f=1
                            else:
                                f=2
                    else:
                        if self.cost<=617:
                            if self.C_previous<=2:
                                if self.duration_previous<=2:
                                    if self.risk_factor<=1:
                                        f=2
                                    else:
                                        f=0
                                else:
                                    if self.homeowner<=0:
                                        f=0
                                    else:
                                        f=2
                            else:
                                if self.duration_previous<=4:
                                    if self.homeowner<=0:
                                        f=0
                                    else:
                                        f=2
                                else:
                                    if self.agedif<=24:
                                        f=2
                                    else:
                                        f=0
                        else:
                            if self.car_age<=15:
                                f=2
                            else:
                                if self.duration_previous<=4:
                                    if self.cost<=635:
                                        f=0
                                    else:
                                        f=2
                                else:
                                    f=2
            else:
                if self.risk_factor<=2:
                    if self.risk_factor<=1:
                        if self.cost<=646:
                            f=0
                        else:
                            if self.agedif<=0:
                                if self.cost<=680:
                                    f=0
                                else:
                                    if self.car_age<=24:
                                        f=0
                                    else:
                                        f=2
                            else:
                                f=0
                    else:
                        f=0
                else:
                    if self.car_age<=12:
                        if self.cost<=675:
                            if self.car_age<=8:
                                if self.cost<=638:
                                    if self.cost<=553:
                                        f=0
                                    else:
                                        f=1
                                else:
                                    f=0
                            else:
                                f=0
                        else:
                            if self.risk_factor<=3:
                                if self.C_previous<=2:
                                    if self.homeowner<=0:
                                        f=0
                                    else:
                                        f=2
                                else:
                                    f=0
                            else:
                                f=0
                    else:
                        if self.duration_previous<=12:
                            f=0
                        else:
                            if self.car_age<=18:
                                if self.cost<=646:
                                    f=0
                                else:
                                    if self.C_previous<=2:
                                        f=2
                                    else:
                                        f=0
                            else:
                                if self.car_value<=8:
                                    if self.agedif<=28:
                                        f=0
                                    else:f=2
                                else:
                                    if self.car_age<=23:
                                        f=3
                                    else:f=2
        else:
            if self.car_age<=12:
                if self.cost<=568:
                    if self.risk_factor<=1:
                        if self.cost<=553:
                            if self.state_group<=4:
                                if self.agedif<=0:
                                    if self.car_age<=0:
                                        f=2
                                    else:
                                        f=0
                                else:
                                    if self.homeowner<=0:
                                        f=0
                                    else:
                                        f=2
                            else:
                                if self.C_previous<=3:
                                    f=0
                                else:
                                    if self.homeowner<=0:
                                        f=0
                                    else:f=2
                        else:
                            if self.state_group<=4:
                                if self.duration_previous<=2:
                                    if self.homeowner<=0:
                                        f=1
                                    else:f=0
                                else:
                                    if self.homeowner<=0:
                                        f=0
                                    else:f=2
                            else:
                                if self.agedif<=2:
                                    if self.car_age<=4:
                                        f=2
                                    else:
                                        f=1
                                else:
                                    if self.agedif<=10:
                                        f=2
                                    else:f=0
                    else:
                        if self.cost<=553:
                            f=0
                        else:
                            if self.risk_factor<=2:
                                if self.C_previous<=2:
                                    f=0
                                else:
                                    if self.state_group<=4:
                                        f=0
                                    else:
                                        f=1
                            else:
                                if self.duration_previous<=10:
                                    f=0
                                else:
                                    if self.state_group<=4:
                                        f=0
                                    else:
                                        f=2
                else:
                    if self.state_group<=4:
                        if self.car_age<=9:
                            f=2
                        else:
                            if self.cost<=646:
                                if self.risk_factor<=2:
                                    f=2
                                else:
                                    if self.homeowner<=0:
                                        f=0
                                    else:
                                        f=2
                            else:
                                f=2
                    else:
                        if self.C_previous<=1:
                            if self.cost<=617:
                                if self.duration_previous<=7:
                                    if self.car_age<=9:
                                        f=2
                                    else:f=0
                                else:
                                    f=1
                            else:
                                if self.duration_previous<=11:
                                    f=2
                                else:
                                    if self.agedif<=2:
                                        f=1
                                    else:f=2
                        else:
                            if self.duration_previous<=5:
                                f=2
                            else:
                                if self.duration_previous<=10:
                                    f=1
                                else:f=1
            else:
                if self.cost<=590:
                    if self.risk_factor<=1:
                        if self.cost<=552:
                            if self.car_value<=3:
                                if self.state_group<=4:
                                    f=2
                                else:
                                    if self.duration_previous<=2:
                                        f=0
                                    else:f=1
                            else:
                                if self.car_age<=18:
                                    f=0
                                else:
                                    f=0
                        else:
                            if self.state_group<=4:
                                if self.C_previous<=1:
                                    if self.duration_previous<=6:
                                        f=0
                                    else:f=2
                                else:
                                    f=2
                            else:
                                if self.car_age<=20:
                                    if self.cost<=577:
                                        f=0
                                    else:
                                        f=1
                                else:
                                    if self.duration_previous<=10:
                                        f=0
                                    else:f=2
                    else:
                        if self.cost<=567:
                            if self.C_previous<=1:
                                if self.car_value<=2:
                                    if self.homeowner<=0:
                                        f=0
                                    else:
                                        f=3
                                else:
                                    f=0
                            else:
                                if self.cost<=552:
                                    if self.car_value<=1:
                                        f=1
                                    else:f=0
                                else:
                                    f=2
                        else:
                            f=0
                else:
                    if self.car_age<=15:
                        if self.cost<=653:
                            if self.duration_previous<=6:
                                if self.homeowner<=0:
                                    f=0
                                else:
                                    if self.C_previous<=1:
                                        f=0
                                    else:f=2
                            else:
                                if self.agedif<=20:
                                    if self.state_group<=4:
                                        f=2
                                    else:f=1
                                else:f=0
                        else:
                            if self.car_value<=6:
                                if self.duration_previous<=10:
                                    f=2
                                else:
                                    if self.agedif<=0:
                                        f=2
                                    else:f=1
                            else:
                                f=2
                    else:
                        if self.duration_previous<=6:
                            if self.cost<=645:
                                if self.risk_factor<=1:
                                    if self.state_group<=4:
                                        f=2
                                    else:f=1
                                else:f=0
                            else:
                                if self.cost<=686:
                                    if self.risk_factor<=2:
                                        f=2
                                    else:
                                        f=0
                                else:
                                    if self.car_age<=17:
                                        f=2
                                    else:f=0
                        else:
                            if self.cost<=631:
                                if self.risk_factor<=2:
                                    if self.agedif<=10:
                                        f=2
                                    else:f=0
                                else:
                                    f=0
                            else:
                                if self.state_group<=4:
                                    f=2
                                else:f=1
        return f

    @property
    def G(self):
        if self.state_group<=3:
            if self.state_group<=1:
                if self.C_previous<=2:
                    if self.C_previous<=0:
                        g=1
                    else:
                        if self.cost<=653:
                            g=2
                        else:g=1
                else:
                    if self.cost<=665:
                        g=2
                    else:
                        if self.homeowner<=0:
                            g=2
                        else:g=1
            else:
                if self.risk_factor<=2:
                    if self.state_group<=2:
                        if self.risk_factor<=1:
                            g=0
                        else:g=1
                    else:
                        g=1
                else:
                    g=1
        else:
            if self.risk_factor<=1:
                if self.state_group<=4:
                    if self.C_previous<=0:
                        g=1
                    else:
                        if self.cost<=721:
                            g=2
                        else:g=1
                else:
                    if self.cost<=568:
                        g=1
                    else:
                        if self.C_previous<=0:
                            g=1
                        else:g=2
            else:
                if self.state_group<=4:
                    if self.risk_factor<=2:
                        if self.car_age<=11:
                            g=2
                        else:
                            g=1
                    else:
                        if self.duration_previous<=4:
                            g=1
                        else:g=2
                else:
                    g=1
        return g



