#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Last modified: <2013-02-26 17:01:44 Tuesday by richard>

# @version 0.1
# @author : Richard
# Email: chao787@gmail.com
"""
Demo for segmentation.
Tests:
"""
import json
import logging

import requests
requests_log = logging.getLogger("requests")
requests_log.setLevel(logging.WARNING)


def word_segment(text):
    """
    SUCCESS: return segmentation list.
    OTHERWISE:return None and log server messages.
    """
    assert isinstance(text, unicode)
    
    ip_addr = "116.213.213.84"
    uri = u'http://%s/segment/seg' % ip_addr
    data_dict = {u'text': text}
    try:
        r = requests.post(uri, data=json.dumps(data_dict).encode('utf-8'))
    except requests.ConnectionError:
        logging.error('Connection server may down here.')
        return None

    body_dict = json.loads(r.text)
    if r.status_code == 201:
        return body_dict.get('word_list')
    else:
        logging.error(body_dict.get('message'))
        return None


def index_segment_for_search_engine(ip_addr, text):
    """
    SUCCESS: return segmentation list.
    OTHERWISE:return None and log server messages.
    """

    assert isinstance(ip_addr, unicode)
    assert isinstance(text, unicode)

    uri = u'http://%s/segment/index_seg' % ip_addr
    data_dict = {u'text': text}
    try:
        r = requests.post(uri, data=json.dumps(data_dict).encode('utf-8'))
    except requests.ConnectionError:
        logging.error('Connection server may down here.')
        return None

    body_dict = json.loads(r.text)
    if r.status_code == 201:
        return body_dict.get('word_list')
    else:
        logging.error(body_dict.get('message'))
        return None

# segment.py ended here
