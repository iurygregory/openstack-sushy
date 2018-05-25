# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from sushy.resources import base


class ActionField(base.CompositeField):
    target_uri = base.Field('target', required=True)


class ResetActionField(ActionField):
    allowed_values = base.Field('ResetType@Redfish.AllowableValues',
                                adapter=list)


class IdRefField(base.CompositeField):
    """Reference to the resource for updating settings"""

    resource_uri = base.Field('@odata.id')
    """The unique identifier for a resource"""
