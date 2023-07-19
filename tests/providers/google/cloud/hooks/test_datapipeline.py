#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from __future__ import annotations

import copy
import re
import shlex
from asyncio import Future
from typing import Any
from unittest import mock
from unittest.mock import MagicMock
from uuid import UUID

import pytest

from airflow.exceptions import AirflowException, AirflowProviderDeprecationWarning
from airflow.providers.google.cloud.hooks.datapipeline import DataPipelineHook

TASK_ID = "test-data_pipeline-operator"
TEST_BODY = {
    "name": "projects/dataflow-interns/locations/us-central1/pipelines/dp-create-1642676351302-mp--1675461000",
            "type": "PIPELINE_TYPE_BATCH",
            "workload": {
                "dataflowFlexTemplateRequest": {
                "launchParameter": {
                    "containerSpecGcsPath": "gs://intern-bucket-1/templates/word-count.json",
                    "jobName": "word-count-test-intern1",
                    "environment": {
                    "tempLocation": "gs://intern-bucket-1/temp"
                    },
                    "parameters": {
                    "inputFile": "gs://intern-bucket-1/examples/kinglear.txt",
                    "output": "gs://intern-bucket-1/results/hello"
                    }
                },
                "projectId": "dataflow-interns",
                "location": "us-central1"
                }
            }
}
TEST_LOCATION = "test-location"
TEST_PROJECTID = "test-project-id"
TEST_GCP_CONN_ID = "test_gcp_conn_id"
TEST_DATA_PIPELINE_NAME = "test_data_pipeline_name"

class TestDataPipelineHook:
    def setup_method(self):
        self.data_pipeline_hook = DataPipelineHook(gcp_conn_id="google-cloud-default")