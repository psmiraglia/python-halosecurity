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

from halosecurity.base import APIResultsIterator


class TargetAPI(APIEndpoint):
    _path = 'target'

    def list(self, **kwargs):
        query = {}

        sort = kwargs.get('sort', None)
        if sort:
            query['sort'] = sort

        sort_desc = kwargs.get('sort_desc', 0)
        if sort_desc:
            query['sort_desc'] = sort_desc

        return APIResultsIterator(
            self._api,
            _query=query,
            _path=f'{self._path}/list.json'
        )
