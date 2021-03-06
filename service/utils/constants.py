# ----------------------------------------------------------------------------------------------------
# (C) Copyright IBM Corp. 2020.  All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
# ----------------------------------------------------------------------------------------------------

from enum import Enum

LIVY_JOB_FINISHED_STATE = 'success'
LIVY_JOB_FAILED_STATE = 'error'
LIVY_JOB_DEAD_STATE = 'dead'
LIVY_JOB_KILLED_STATE = 'killed'
SYNC_JOB_MAX_WAIT_TIME = 300


class RecordType(Enum):
    PAYLOAD_LOGGING = "payload_logging"
    EXPLANATIONS = "explanations"
