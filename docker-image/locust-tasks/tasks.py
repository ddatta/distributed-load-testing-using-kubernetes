#!/usr/bin/env python

# Copyright 2022 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import uuid
import requests
from datetime import datetime
from locust import FastHttpUser, TaskSet, task


# [START locust_test_task]

class MetricsTaskSet(TaskSet):
    _deviceid = None

    def on_start(self):
        self._deviceid = str(uuid.uuid4())

    # @task(1)
    # def login(self):
    #     self.client.post(
    #         '/login', {"deviceid": self._deviceid})

    @task
    def post_metrics(self):
        auth_header = {'Content-type': 'application/json',
               'Authorization': 'Basic UzNYNzJWWVFDVVo1NFlLUzpiT0Q2c1FuVHlLTWI4ZDd1RWJSVUNDQzdTdStQcG9LUUhqUThvMStheGw2RUQvNlRqTGlwMU84Y01aVVNteDB5'}
        #data='{"value":{"type":"JSON","data":"mmt 514"}}';
        # self.client.post(
        #    "/kafka/v3/clusters/lkc-zpg6g7/topics/iotdemotopic/records", data=data)
        # data='{"vehicleId": self._deviceid}'
        data = '{"vehicleId":"Hello World!"}'
        self.client.post(
            "/api/measurement", data=data, headers=auth_header)


class MetricsLocust(FastHttpUser):
    tasks = {MetricsTaskSet}

# [END locust_test_task]
