from abc import ABC, abstractmethod
from typing import Optional
from urllib.parse import urlencode

import requests


class ScarletSharkClient(ABC):
    version: str
    api_actions: dict = {}
    api_key: str
    print_json = False

    def __init__(
            self, api_key: str, print_json: bool = False):
        self.api_key = api_key
        self.print_json = print_json

    def _resolve_url(self, action_name: str, params) -> str:
        if action_name not in self.api_actions:
            raise Exception(f'The action [{action_name}] is not supported')
        query_parameters: dict = {}
        for k, v in params.items():
            if k != 'self' and v:
                query_parameters[k] = v
        if not query_parameters:
            raise Exception(f'At least query parameter has to be specified in [{params}]')
        endpoint = self.api_actions[action_name]
        query_string = urlencode(query_parameters)
        return f'{self.version}{endpoint}?{query_string}'

    def _prepare_request(self, uri: str):
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        base_url = 'https://api.scarletshark.com/'
        url = f'{base_url}{uri}'
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            r = response.json()
            if int(r.get('result_code', -1)) < 0:
                raise Exception(r.get('result').get('message'))
            result = r.get('result')
            if self.print_json:
                import json
                print(json.dumps(result, indent=2, sort_keys=True))
            return result
        return None

    @abstractmethod
    def search_dns(
            self,
            ip: Optional[str] = None,
            hostname: Optional[str] = None,
            nonce: Optional[int] = None) -> Optional[dict]:
        """
        Returns known hostname and IP associations from the Scarlet Shark database. These associations are mostly active IP lookups.
        :param ip: String [optional] - IP address to find hostnames for
        :param hostname: String [optional] - hostname to find IPs for
        :param nonce: Integer [optional] - A nonce that is returned, if provided in the request
        :return: Returns known hostname and IP associations from the Scarlet Shark database
        """
        pass

    @abstractmethod
    def search_domain(
            self,
            domain: str,
            nonce: Optional[int] = None) -> Optional[dict]:
        """
        Returns information on the given domain.
        :param domain: String - The domain to search for. The domain will automatically be changed from Unicode to an IDNA ASCII-compatible format
        :param nonce: Integer [optional] - A nonce that is returned, if provided in the request
        :return: Returns information on the given domain.
        """
        pass

    @abstractmethod
    def search_email(
            self,
            emails: list[str],
            nonce: Optional[int] = None) -> Optional[dict]:
        """
        Returns threat information for the given email addresses.
        :param emails: String Array - Email addresses to search for threat data on
        :param nonce: Integer [optional] - A nonce that is returned, if provided in the request
        :return: Returns threat information for the given email addresses.
        """
        pass

    @abstractmethod
    def search_hash(
            self,
            sha256: Optional[str] = None,
            md5: Optional[str] = None,
            nonce: Optional[int] = None) -> Optional[dict]:
        """
        Returns information on either a SHA256 or a MD5 hash.
        :param sha256: String [optional] - The SHA256 hash to search for
        :param md5: String [optional] - The MD5 hash to search for
        :param nonce: Integer [optional] - A nonce that is returned, if provided in the request
        :return: Returns information on either a SHA256 or a MD5 hash.
        """
        pass

    @abstractmethod
    def search_ip(
            self,
            ips: list[str],
            context: Optional[str] = None,
            time_period: Optional[int] = None,
            time_zone: Optional[str] = None,
            nonce: Optional[int] = None) -> Optional[dict]:
        """
        Looks up information for an IP and any threat intel information about that IP.
        :param ips: String array - v4 or v6 IP address
        :param context: String [optional] – Possible values: [user_activity, none] - The context of the IP look up. This helps give a more accurate threat classification.
        :param time_period: Integer - The number of days to show security issues for.
        :param time_zone: String [optional] - PHP Time Zone Strings. Results will be returned in the given time zone. UTC is the default. See: https://www.php.net/manual/en/timezones.php
        :param nonce: Integer [optional] - A nonce that is returned, if provided in the request
        :return: Looks up information for an IP and any threat intel information about that IP
        """
        pass

    @abstractmethod
    def search_network(
            self,
            ip: str = None,
            nonce: Optional[int] = None) -> Optional[dict]:
        """
        Looks up information network information about a given IP.
        :param ip: String - v4 or v6 IP address
        :param nonce: Integer [optional] - A nonce that is returned, if provided in the request
        :return: Looks up information network information about a given IP
        """
        pass

    @abstractmethod
    def search_threat_actors(
            self,
            query: Optional[str] = None,
            threat_actor_id: Optional[int] = None,
            vertical: Optional[str] = None,
            nonce: Optional[int] = None) -> Optional[dict]:
        """
        Returns information about a given threat actor or threat actors targeting a given vertical.
        :param query: String [optional] - Search string to match against threat actor aliases
        :param threat_actor_id: Integer [optional] - The Scarlet Shark threat_actor_id to search by
        :param vertical: String [optional] - The vertical to search by
        :param nonce: Integer [optional] - A nonce that is returned, if provided in the request
        :return: Information about a given threat actor or threat actors targeting a given vertical
        """
        pass

    @abstractmethod
    def search_threat_tools(
            self,
            query: Optional[str] = None,
            threat_actor_id: Optional[int] = None,
            nonce: Optional[int] = None) -> Optional[dict]:
        """
        Returns information about a given threat tool. The threat tool can be malware or a legitimate tool.
        :param query: String [optional] - Search string to match against threat tool aliases
        :param threat_actor_id: Integer [optional] - The Scarlet Shark threat_tool_id to search by
        :param nonce: Integer [optional] - A nonce that is returned, if provided in the request
        :return: Information about a given threat tool. The threat tool can be malware or a legitimate tool.
        """
        pass

    @abstractmethod
    def search_url(
            self,
            urls: list[str],
            nonce: Optional[int] = None) -> Optional[dict]:
        """
        Looks up threat information for the given URLs.
        :param urls: String Array - URLs to search for threat data on. The domain of each URL will automatically be changed from Unicode to an IDNA ASCII-compatible format
        :param nonce: Integer [optional] - A nonce that is returned, if provided in the request
        :return: Looks up threat information for the given URLs
        """
        pass
