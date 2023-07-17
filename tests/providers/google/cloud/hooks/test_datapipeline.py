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

TASK_ID = "test-datapipeline-operator"
DATA_PIPELINE_NAME = "" # TODO add data pipeline name to be tested
BODY = "" # TODO add data pipeline body
PROJECT_ID = "dataflow-interns"
LOCATION = "DEFAULT_DATAPIPELINE_LOCATION"
GCP_CONN_ID ="google_cloud_default"