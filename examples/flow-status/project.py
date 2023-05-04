#!/usr/bin/env python3
# Copyright (c) 2019 The Regents of the University of Michigan
# All rights reserved.
# This software is licensed under the BSD 3-Clause License.
from flow import FlowProject


class Project(FlowProject):
    pass


@Project.label()
def current_step(job):
    return f'Current step: {job.doc["step"]}'


@Project.label()
def is_even(job):
    if job.doc["step"] % 2 == 0:
        return True


@Project.label()
def is_odd(job):
    if job.doc["step"] % 2 == 1:
        return True


if __name__ == "__main__":
    Project().main()
