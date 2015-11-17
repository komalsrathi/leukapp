# -*- coding: utf-8 -*-

# third party
from rest_framework import serializers

# local
from .models import Participant
from . import constants


class ParticipantCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = constants.PARTICIPANT_CREATE_FIELDS
