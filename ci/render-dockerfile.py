#!/usr/bin/env python

from __future__ import print_function

import os
import sys
import requests

from jinja2 import Template


OUTPUT_FILE = 'Dockerfile'
INPUT_FILE = 'Dockerfile.jinja'


def main():
    """
    Renders the Dockerfile.jinja file using some environment variables.

    :return: None, Dockerfile is created.
    """
    current_branch = os.environ.get('CIRCLE_BRANCH')
    latest_w3af_commit = os.environ.get('W3AF_COMMIT', None)

    if latest_w3af_commit is None:
        print('No W3AF_COMMIT environment variable was specified! When we'
              ' build in this scenario there is a (big) chance of us'
              ' trying to use a Dockerfile FROM which will NOT EXIST!')
        latest_w3af_commit = get_latest_commit(current_branch)

    render(latest_w3af_commit, current_branch)

    print('Using w3af commit: %s' % latest_w3af_commit)


def render(w3af_commit, current_branch):
    """
    Render the file using the provided args, saves output to Dockerfile

    :param w3af_commit: The latest w3af commit
    :param current_branch: The latest w3af branch
    :return: None
    """
    template = Template(file(INPUT_FILE).read())
    rendered_dockerfile = template.render(w3af_commit=w3af_commit,
                                          environment=current_branch)
    file(OUTPUT_FILE, 'w').write(rendered_dockerfile)


def get_latest_commit(current_branch):
    """
    Uses the github API to retrieve the latest commit from the w3af repository

    :return: The commit it
    """
    #GET /repos/:owner/:repo/commits
    url = 'https://api.github.com/repos/andresriancho/w3af/commits?sha=%s'
    return requests.get(url % current_branch).json()[0]['sha'][:7]


if __name__ == '__main__':
    sys.exit(main())

