'''
Copyright 2022 Paolo Smiraglia <paolo.smiraglia@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from halosecurity.base import HaloSecurityAPIEndpoint


class AckAPI(HaloSecurityAPIEndpoint):
    _path = 'ack'

    # host

    def host_list(self, **kwargs):
        ep = 'host-list.json'
        query = {}
        return self._list(ep, query, **kwargs)

    # element

    def element_get(self, element_id, **kwargs):
        ep = 'element-get.json'
        query = {'id': element_id}
        return self._get(ep, query, **kwargs)

    def element_list(self, element_type, **kwargs):
        ep = 'element-list.json'
        query = {'type': element_type}
        return self._list(ep, query, **kwargs)

    # issue

    def issue_get(self, issue_id, **kwargs):
        ep = 'issue-get.json'
        query = {'id': issue_id}
        return self._get(ep, query, **kwargs)

    def issue_list(self, **kwargs):
        ep = 'issue-list.json'
        query = {}
        return self._list(ep, query, **kwargs)
