from huawei_lte_api.ApiGroup import ApiGroup
from huawei_lte_api.Session import GetResponseType


class Dhcp(ApiGroup):
    def settings(self) -> GetResponseType:
        return self._session.get('dhcp/settings')

    def feature_switch(self) -> GetResponseType:
        return self._session.get('dhcp/feature-switch')

    def dhcp_host_info(self) -> GetResponseType:
        """
        Endpoint found by reverse engineering B310s-22 firmware, unknown usage
        :return:
        """
        return self._session.get('dhcp/dhcp-host-info')

    def static_addr_info(self) -> GetResponseType:
        """
        Endpoint found by reverse engineering B310s-22 firmware, unknown usage
        :return:
        """
        return self._session.get('dhcp/static-addr-info')
