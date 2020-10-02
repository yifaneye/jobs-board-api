# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import csv

from flask import request, g

from . import Resource
from .. import schemas


class Job(Resource):
    DB = 'jobs.csv'

    def get(self):
        with open(self.DB, 'r') as csvFile:
            csvReader = csv.DictReader(csvFile)
            response = [line for line in csvReader]
        return response, 200, None

    def post(self):
        row = list(g.json.values())  # or [*g.json.values()]
        with open(self.DB, 'a') as csvFile:
            csvWriter = csv.writer(csvFile)
            csvWriter.writerow(row)
        return row, 201, None
