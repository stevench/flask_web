# -*- encoding: utf-8 -*-
import uuid


def create_uuid(name):
    return str(uuid.uuid3(uuid. NAMESPACE_DNS, name))
