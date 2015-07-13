#!/usr/bin/env python

from __future__ import print_function

import os
import sys

from jinja2 import Template
from docker_tag_naming.utils import get_latest_version

OUTPUT_FILE = 'Dockerfile'
INPUT_FILE = 'Dockerfile.jinja'


def main():
    """
    Renders the Dockerfile.jinja file using some environment variables.

    :return: None, Dockerfile is created.
    """
    current_branch = os.environ.get('CIRCLE_BRANCH')
    latest_tag = os.environ.get('W3AF_REGISTRY_TAG', None)

    if current_branch is None:
        print('CIRCLE_BRANCH environment variable is not set.')
        return 1

    if latest_tag is None:
        try:
            latest_tag = get_latest_version('andresriancho/w3af',
                                            current_branch)
        except Exception, e:
            print('Failed to get the latest tag version: "%s"' % e)
            return 1
        else:
            print('Latest tag in the %s branch is %s' % (current_branch,
                                                         latest_tag))

    if latest_tag is None:
        print('Retrieved latest version is None')
        return 1

    # Get the version as a string
    latest_tag = str(latest_tag)
    print('Using latest w3af registry tag %s to render Dockerfile' % latest_tag)

    # Render the dockerfile
    render(latest_tag, current_branch)

    return 0


def render(latest_tag, current_branch):
    """
    Render the file using the provided args, saves output to Dockerfile

    :param latest_tag: The latest w3af commit
    :param current_branch: The latest w3af branch
    :return: None
    """
    template = Template(file(INPUT_FILE).read())
    rendered_dockerfile = template.render(latest_w3af_tag=latest_tag,
                                          environment=current_branch)
    file(OUTPUT_FILE, 'w').write(rendered_dockerfile)


if __name__ == '__main__':
    sys.exit(main())

