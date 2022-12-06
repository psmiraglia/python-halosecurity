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

from halosecurity.account import AccountAPI
from halosecurity.ack import AckAPI
from halosecurity.discovery import DiscoveryAPI
from halosecurity.dns import DnsAPI
from halosecurity.event import EventAPI
from halosecurity.file import FileAPI
from halosecurity.http import HttpAPI
from halosecurity.issue import IssueAPI
from halosecurity.pci import PciAPI
from halosecurity.port import PortAPI
from halosecurity.scan import ScanAPI
from halosecurity.security import SecurityAPI
from halosecurity.tag import TagAPI
from halosecurity.target import TargetAPI
from halosecurity.technology import TechnologyAPI
from halosecurity.user import UserAPI
from halosecurity.website import WebsiteAPI
from halosecurity.whois import WhoisAPI


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
    def account(self):
        return AccountAPI(self)

    @property
    def ack(self):
        return AckAPI(self)

    @property
    def discovery(self):
        return DiscoveryAPI(self)

    @property
    def dns(self):
        return DnsAPI(self)

    @property
    def event(self):
        return EventAPI(self)

    @property
    def file(self):
        return FileAPI(self)

    @property
    def http(self):
        return HttpAPI(self)

    @property
    def issue(self):
        return IssueAPI(self)

    @property
    def pci(self):
        return PciAPI(self)

    @property
    def port(self):
        return PortAPI(self)

    @property
    def scan(self):
        return ScanAPI(self)

    @property
    def security(self):
        return SecurityAPI(self)

    @property
    def tag(self):
        return TagAPI(self)

    @property
    def target(self):
        return TargetAPI(self)

    @property
    def technology(self):
        return TechnologyAPI(self)

    @property
    def user(self):
        return UserAPI(self)

    @property
    def website(self):
        return WebsiteAPI(self)

    @property
    def whois(self):
        return WhoisAPI(self)
