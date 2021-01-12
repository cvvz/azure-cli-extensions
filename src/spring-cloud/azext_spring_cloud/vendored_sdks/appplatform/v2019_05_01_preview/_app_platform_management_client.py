# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import AppPlatformManagementClientConfiguration
from .operations import ServicesOperations
from .operations import AppsOperations
from .operations import BindingsOperations
from .operations import CertificatesOperations
from .operations import CustomDomainsOperations
from .operations import DeploymentsOperations
from .operations import Operations
from .operations import RuntimeVersionsOperations
from .operations import SkuOperations
from . import models


class AppPlatformManagementClient(SDKClient):
    """REST API for Azure Spring Cloud

    :ivar config: Configuration for client.
    :vartype config: AppPlatformManagementClientConfiguration

    :ivar services: Services operations
    :vartype services: azure.mgmt.appplatform.v2019_05_01_preview.operations.ServicesOperations
    :ivar apps: Apps operations
    :vartype apps: azure.mgmt.appplatform.v2019_05_01_preview.operations.AppsOperations
    :ivar bindings: Bindings operations
    :vartype bindings: azure.mgmt.appplatform.v2019_05_01_preview.operations.BindingsOperations
    :ivar certificates: Certificates operations
    :vartype certificates: azure.mgmt.appplatform.v2019_05_01_preview.operations.CertificatesOperations
    :ivar custom_domains: CustomDomains operations
    :vartype custom_domains: azure.mgmt.appplatform.v2019_05_01_preview.operations.CustomDomainsOperations
    :ivar deployments: Deployments operations
    :vartype deployments: azure.mgmt.appplatform.v2019_05_01_preview.operations.DeploymentsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.appplatform.v2019_05_01_preview.operations.Operations
    :ivar runtime_versions: RuntimeVersions operations
    :vartype runtime_versions: azure.mgmt.appplatform.v2019_05_01_preview.operations.RuntimeVersionsOperations
    :ivar sku: Sku operations
    :vartype sku: azure.mgmt.appplatform.v2019_05_01_preview.operations.SkuOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription ID which uniquely identify the
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = AppPlatformManagementClientConfiguration(credentials, subscription_id, base_url)
        super(AppPlatformManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-05-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.services = ServicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.apps = AppsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.bindings = BindingsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.certificates = CertificatesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.custom_domains = CustomDomainsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.deployments = DeploymentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.runtime_versions = RuntimeVersionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sku = SkuOperations(
            self._client, self.config, self._serialize, self._deserialize)