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


class APIResult:
    def __init__(self, api, **kwargs):
        self._api = api
        self._query = kwargs.get('_query')
        self._path = kwargs.get('_path')

    def get_data(self):
        # init data
        data = {}

        # make the API call
        resp = self._api.get(self._path, params=self._query)

        # check the response
        if ((resp.status_code >= 200)
                and (resp.status_code < 300)
                and (resp.headers.get('Content-Type') == 'application/json')):
            data = resp.json()

        return data


class APIResultsIterator:
    # The current number of records that have been returned
    count = 0
    # The current page of data being walked through
    page = []
    # The number of record returned from the current page
    page_count = 0
    # The total number of records that exist for the current request
    total = 1
    # The api to be used
    _api = None
    # The record to begin at
    _start = 0
    # Number of records to be returned per page
    _limit = 100

    _pages_requested = 0

    def __init__(self, api, **kwargs):
        self._api = api
        self._query = kwargs.get('_query')
        self._path = kwargs.get('_path')

    def _get_page(self):
        # make the API call
        resp = self._get_data()

        # get info about pagination
        pagination = resp.get('pagination')
        self.total = pagination.get('total')

        # reset the page counter
        self.page_count = 0

        # set the page
        self.page = resp.get('list', [])
        self._pages_requested += 1

        # debug info
        print('--- DEBUG ---')
        print(f'Requested pages: {self._pages_requested}')
        print(f'Records in current page: {len(self.page)}')
        print(f'Total records: {self.total}')
        print('-------------')

    def _get_data(self):
        # set query
        query = self._query
        query['start'] = self._start
        query['limit'] = self._limit

        # get page
        resp = self._api.get(self._path, params=query).json()

        # increase the starting point for the next call (if any)
        self._start += self._limit

        return resp

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.count >= self.total:
            raise StopIteration()

        if self.page_count >= len(self.page) and self.count <= self.total:
            self._get_page()
            if len(self.page) == 0:
                raise StopIteration()

        item = self.page[self.page_count]
        self.count += 1
        self.page_count += 1

        print(f'    Consumed {self.count}/{self.total}...')
        return item
