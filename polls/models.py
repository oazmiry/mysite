#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.db.models import IntegerField, CharField, ForeignKey, Model, DateTimeField
from django.utils import timezone


class Question(Model):
    question_text = CharField(max_length=200)
    pub_date = DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # noinspection PyTypeChecker
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(Model):
    question = ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = CharField(max_length=200)
    votes = IntegerField(default=0)

    def __str__(self):
        return self.choice_text
