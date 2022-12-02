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

from restfly.endpoint import APIEndpoint

from halosecurity.base.exceptions import EndpointDoesNotExist
from halosecurity.base.results import APIResult, APIResultsIterator


class HaloSecurityAPIEndpoint(APIEndpoint):
    # the API path (e.g. /target/)
    _path = ''

    # parameters for the "/list.json" endpoint
    _query_args_list = []

    # parameters for the "/get.json" endpoint
    _query_args_get = []

    def list(self, **kwargs):
        ep = 'list'

        # check if endpoint exists
        query_args = self._query_args_list
        if not query_args:
            raise EndpointDoesNotExist(self._path, ep)

        # build query
        query = {}
        for k in query_args:
            v = kwargs.get(k, None)
            if v:
                query[k] = v

        # get the API result
        return APIResultsIterator(
            self._api,
            _query=query,
            _path=f'{self._path}/{ep}.json'
        )

    def get(self, resource_id):
        ep = 'get'

        # check if endpoint exists
        query_args = self._query_args_get
        if not query_args:
            raise EndpointDoesNotExist(self._path, ep)

        # build the query
        query = {}
        for k in query_args:
            query[k] = resource_id

        # get the API result
        return APIResult(
            self._api,
            _query=query,
            _path=f'{self._path}/{ep}.json'
        )
