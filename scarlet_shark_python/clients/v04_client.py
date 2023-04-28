import sys
from typing import Optional

from scarlet_shark_python.clients.abstract import ScarletSharkClient as AbstractClient


class ScarletSharkClient(AbstractClient):
    version: str = 'v0.4'
    api_actions: dict = {
        'search_dns': '/search_dns.php',
        'search_domain': '/search_domain.php',
        'search_email': '/search_email.php',
        'search_hash': '/search_hash.php',
        'search_ip': '/search_ip.php',
        'search_network': '/search_network.php',
        'search_threat_actors': '/search_threat_actors.php',
        'search_threat_tools': '/search_threat_tools.php',
        'search_url': '/search_url.php',
    }

    def search_dns(
            self,
            ip: Optional[str] = None,
            hostname: Optional[str] = None,
            nonce: Optional[int] = None) -> Optional[dict]:
        uri = self._resolve_url(sys._getframe().f_code.co_name, locals())
        return self._prepare_request(uri)

    def search_domain(
            self,
            domain: str,
            nonce: Optional[int] = None) -> Optional[dict]:
        uri = self._resolve_url(sys._getframe().f_code.co_name, locals())
        return self._prepare_request(uri)

    def search_email(
            self,
            emails: list[str],
            nonce: Optional[int] = None) -> Optional[dict]:
        uri = self._resolve_url(sys._getframe().f_code.co_name, locals())
        return self._prepare_request(uri)

    def search_hash(
            self,
            sha256: Optional[str] = None,
            md5: Optional[str] = None,
            nonce: Optional[int] = None) -> Optional[dict]:
        uri = self._resolve_url(sys._getframe().f_code.co_name, locals())
        return self._prepare_request(uri)

    def search_ip(
            self,
            ips: list[str],
            context: Optional[str] = None,
            time_period: Optional[int] = None,
            time_zone: Optional[str] = None,
            nonce: Optional[int] = None) -> Optional[dict]:
        uri = self._resolve_url(sys._getframe().f_code.co_name, locals())
        return self._prepare_request(uri)

    def search_network(
            self,
            ip: str = None,
            nonce: Optional[int] = None) -> Optional[dict]:
        uri = self._resolve_url(sys._getframe().f_code.co_name, locals())
        return self._prepare_request(uri)

    def search_threat_actors(
            self,
            query: Optional[str] = None,
            threat_actor_id: Optional[int] = None,
            vertical: Optional[str] = None,
            nonce: Optional[int] = None) -> Optional[dict]:
        uri = self._resolve_url(sys._getframe().f_code.co_name, locals())
        return self._prepare_request(uri)

    def search_threat_tools(
            self,
            query: Optional[str] = None,
            threat_actor_id: Optional[int] = None,
            nonce: Optional[int] = None) -> Optional[dict]:
        uri = self._resolve_url(sys._getframe().f_code.co_name, locals())
        return self._prepare_request(uri)

    def search_url(
            self,
            urls: list[str],
            nonce: Optional[int] = None) -> Optional[dict]:
        uri = self._resolve_url(sys._getframe().f_code.co_name, locals())
        return self._prepare_request(uri)
