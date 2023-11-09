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
import time
import random
import enum
from datetime import datetime
from locust import FastHttpUser, TaskSet, task




# [START locust_test_task]

class MetricsTaskSet(TaskSet):
    _deviceid = None

    def on_start(self):
        self._deviceid = random.randint(1,9999999)
        

    # @task(1)
    # def login(self):
    #     self.client.post(
    #         '/login', {"deviceid": self._deviceid})

    @task
    def post_metrics(self):
        header = {'Content-type': 'application/json'}
               # 'Authorization': 'Basic UzNYNzJWWVFDVVo1NFlLUzpiT0Q2c1FuVHlLTWI4ZDd1RWJSVUNDQzdTdStQcG9LUUhqUThvMStheGw2RUQvNlRqTGlwMU84Y01aVVNteDB5'}
        #data='{"value":{"type":"JSON","data":"mmt 514"}}';
        # self.client.post(
        #    "/kafka/v3/clusters/lkc-zpg6g7/topics/iotdemotopic/records", data=data)
        # data='{"vehicleId": self._deviceid}'
        # ts = datetime.now()
        #ts = time.Time()
        ts = round(time.time() * 1000)
        temp = random.uniform(-50.0, 90.0)
        longi =  random.uniform(0.0, 180.0)
        lat =  random.uniform(-90.0, 90.0)
        altitude =  random.uniform(-3.0, 8000.0)
        er =  random.uniform(0.0, 360.0)
        fps =  random.uniform(0.0, 30.1)
        et = random.uniform(-10.0, 90.0)
        fu = random.uniform(0.0, 60.0)
        ds = random.uniform(0.0, 150.0)

        data = '{"vehicleId":'+str(self._deviceid)+ ', "ts" : ' + str(ts) + \
        ',"temperature":' + str(temp) +', "operatingtime" : 10,"fuelusage": '+  str(fu) +',"front_linkage_position" : 1,  \
            "drivingspeed": '+ str(ds) +',"enginestate":1,"autopilot_system_state":0,"engine_load":35.7,"latitude":' + str(lat)  + ', \
            "longitude": ' + str(longi)  + ',"altitude":' + str(altitude) + ',"engine_rotation":' + str(er) + ',"front_pme_shaft":' + str(fps) + ', \
            "rear_linkage_position":3,"four_wheel_driving_state":"false","fuel_tank_level":1,"last_error_msg": "no-error" ,"engine_temperature":' + str(et) + ', \
                "connection_state":"connected","lte_connection_level":34.1,"mode":"test"}'
        print(data)
        self.client.post(
            "/api/measurement", data=data, headers=header)


class MetricsLocust(FastHttpUser):
    tasks = {MetricsTaskSet}

# [END locust_test_task]
