#!/usr/bin/env python

import sys
import requests
import argparse


def parse_arguments():
    """
    Parses the command line arguments
    :return: The parse result from argparse
    """
    parser = argparse.ArgumentParser(description='Launch a new w3af-api-docker'
                                                 ' build using CI REST API')

    parser.add_argument('--circle-auth-token',
                        required=True,
                        dest='auth_token',
                        help='The CircleCI authentication token for the'
                             ' w3af-api-docker build')

    parser.add_argument('--branch',
                        required=True,
                        dest='branch',
                        help='The branch to build (develop|master)')

    parser.add_argument('--w3af-commit',
                        required=True,
                        dest='w3af_commit',
                        help='The w3af commit to use in the Dockerfile FROM'
                             ' a strong requirement for this setting is to'
                             ' have a tag named <w3af-commit>-<branch> in'
                             ' https://registry.hub.docker.com/u/andresriancho/'
                             'w3af/tags/manage/')

    args = parser.parse_args()
    return args


def main(auth_token, branch, w3af_commit):
    url = 'https://circleci.com/api/v1/project/andresriancho/' \
          'w3af-api-docker/tree/%s?circle-token=%s' % (branch, auth_token)
    headers = {'Content-Type': 'application/json'}
    data = '{"build_parameters": {"W3AF_COMMIT": "%s"}}' % w3af_commit

    requests.post(url, headers=headers, data=data)

    return 0

if __name__ == '__main__':
    args = parse_arguments()
    sys.exit(main(args.auth_token, args.branch, args.w3af_commit))
