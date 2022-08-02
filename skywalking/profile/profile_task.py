#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from skywalking.utils.lang import tostring


@tostring
class ProfileTask:

    def __init__(self,
                 task_id: str = "",
                 first_span_op_name: str = "",
                 duration: int = -1,
                 min_duration_threshold: int = -1,
                 thread_dump_period: int = -1,
                 max_sampling_count: int = -1,
                 start_time: int = -1,
                 create_time: int = -1):
        self.task_id = task_id
        self.first_span_op_name = first_span_op_name
        self.duration = duration
        # when can start profile after span context created
        self.min_duration_threshold = min_duration_threshold
        # profile interval
        self.thread_dump_period = thread_dump_period
        self.max_sampling_count = max_sampling_count
        self.start_time = start_time
        self.create_time = create_time
