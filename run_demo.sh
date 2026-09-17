#!/usr/bin/env sh
set -e
python -m campusflow seed
python -m campusflow task-list
python -m campusflow task-plan
python -m campusflow course-plan
python -m campusflow analytics
