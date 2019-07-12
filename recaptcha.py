# -*- coding: utf-8 -*-

from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask


def resolve(url, api_key, site_key):
    client = AnticaptchaClient(api_key)
    task = NoCaptchaTaskProxylessTask(url, site_key)

    job = client.createTask(task)
    job.join()

    return job.get_solution_response()
