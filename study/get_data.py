#coding=utf-8

from mitmproxy import http

def request(flow):
    request_data = flow.request
    request_url = request_data.url
    request_pr = request_data.query
    request_form = request_data.urlencoded_form
    print("url:---------->",request_url)
    print("request_pr:---------->",request_pr)
    print("request_form:---------->",request_form)
