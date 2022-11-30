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

from restfly.session import APISession

from halosecurity.dns import DnsAPI
from halosecurity.target import TargetAPI
from halosecurity.user import UserAPI


class HaloSecurity(APISession):
    _url = 'https://api.halosecurity.com/api/v1'

    def _authenticate(self, **kwargs):
        print('Authenticate')
        api_key = kwargs.get('api_key', None)
        if api_key:
            self._session.headers.update({
                'x-apikey': api_key
            })
        else:
            self._log.warn('Starting an unauthenticated session')

    @property
    def user(self):
        return UserAPI(self)

    @property
    def target(self):
        return TargetAPI(self)

    @property
    def dns(self):
        return DnsAPI(self)
