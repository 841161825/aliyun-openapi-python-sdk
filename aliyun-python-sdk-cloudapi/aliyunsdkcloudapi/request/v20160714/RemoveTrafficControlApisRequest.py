# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class RemoveTrafficControlApisRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudAPI', '2016-07-14', 'RemoveTrafficControlApis','apigateway')

	def get_TrafficControlId(self):
		return self.get_query_params().get('TrafficControlId')

	def set_TrafficControlId(self,TrafficControlId):
		self.add_query_param('TrafficControlId',TrafficControlId)

	def get_StageName(self):
		return self.get_query_params().get('StageName')

	def set_StageName(self,StageName):
		self.add_query_param('StageName',StageName)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_ApiIds(self):
		return self.get_query_params().get('ApiIds')

	def set_ApiIds(self,ApiIds):
		self.add_query_param('ApiIds',ApiIds)