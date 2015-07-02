#!/usr/bin/env python

from __future__ import print_function

import os
import sys

from jinja2 import Template
from docker_tag_naming import get_latest_tag

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
        latest_w3af_commit = get_latest_tag('andresriancho/w3af',
                                            current_branch)

    render(latest_w3af_commit, current_branch)

    print('Using w3af commit: %s' % latest_w3af_commit)
    return 0


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


def get_latest_w3af_image_tag(current_branch):
    """
    Uses the registry API to retrieve the latest image tag for the corresponding
    branch.

    :return: The branch name, something like '<commit-id>-develop' or
             '<commit-id>-master'
    """
    raise NotImplementedError


if __name__ == '__main__':
    sys.exit(main())

