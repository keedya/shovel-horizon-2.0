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
import logging
import json
import requests 


from django.utils.translation import ugettext_lazy as _

from horizon import exceptions

LOG = logging.getLogger(__name__)

SHOVEL_BASE_API = '/api/2.0'
URI = "http://10.240.19.163:9005" + SHOVEL_BASE_API

def get_driver_list():
    r = requests.get(URI + '/Ironic/drivers')
    return r.json()

def get_images_list():
    r = requests.get(URI + '/Glance/images')
    return r.json()

def get_ironic_nodes():
    r = requests.get(URI + '/Ironic/nodes')
    return r.json()

def get_ironic_node(id):
    r = requests.get(URI + '/Ironic/nodes/' + id)
    return r.json()

def request_node_get(id):
    r = requests.get(URI + '/RackHD/nodes/' + id)
    return r.json()

def request_nodes_get():
    r = requests.get(URI + '/RackHD/nodes')
    return r.json()

def register_node_post(data):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(URI + '/Shovel/register',
            data=json.dumps(data), headers=headers)
    return r.json()

def unregister_node_del(name):
    r = requests.delete(URI + '/Shovel/unregister/' + name)
    if r.status_code == 204:
        return '' , r.status_code
    else:
        return r.json(), r.status_code 

def request_catalog_get(uuid):
    r = requests.get(URI+ '/RackHD/catalogs/' + uuid)
    return r.json()

def get_catalog_data_by_source(id,source):
    r = requests.get(URI+ '/RackHD/nodes/' + id + '/catalogs/' + source)
    return r.json()['data']

def get_current_sel_data(id):
    r = requests.get(URI+ '/RackHD/nodes/' + id + '/sel')
    return r.json()

def node_patch(uuid, data):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.patch(URI + '/Ironic/node/' + uuid,
            data=json.dumps(data), headers=headers)
    return r.json()
