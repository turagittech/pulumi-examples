"""An Azure RM Python Pulumi program"""

import pulumi
from pulumi_azure_native import storage
from pulumi_azure_native import resources

import pulumi_azure_native as azure_native
from pulumi import automation as auto

config = pulumi.Config("azure-native");

location = config.require("location")
org_code = 'TGT'
org_name = 'Turagit'
loc_code = 'SYD'
print(location)
app_type = 'AVN'
owner = 'Peter M'
stack_name = pulumi.get_stack()
project_name = pulumi.get_project()

resource_group_network_name = org_code + '-' + loc_code + '-' + stack_name.upper() + '-' + app_type + '-' + 'Network'

vnet_name_001 = org_code + '-' + loc_code + '-' + stack_name.upper() + '-' + app_type + '-' + 'Vnet-001'
vnet_name_002 = org_code + '-' + loc_code + '-' + stack_name.upper() + '-' + app_type + '-' + 'Vnet-002'
print(vnet_name_001)

vnet_001 = azure_native.network.VirtualNetwork(vnet_name_001,
    address_space=azure_native.network.AddressSpaceArgs(
        address_prefixes=["10.0.0.0/20"],
    ),
    location=location,
    resource_group_name=resource_group_network_name,
    virtual_network_name=vnet_name_001)

vnet_002 = azure_native.network.VirtualNetwork(vnet_name_002,
    address_space=azure_native.network.AddressSpaceArgs(
        address_prefixes=["10.0.16.0/20"],
    ),
    location=location,
    resource_group_name=resource_group_network_name,
    virtual_network_name=vnet_name_002)



# Create an Azure Resource Group
resource_group = resources.ResourceGroup('resource_group')

# Create an Azure resource (Storage Account)
account = storage.StorageAccount('sa',
    resource_group_name=resource_group.name,
    sku=storage.SkuArgs(
        name=storage.SkuName.STANDARD_LRS,
    ),
    kind=storage.Kind.STORAGE_V2)

# Export the primary key of the Storage Account
primary_key = pulumi.Output.all(resource_group.name, account.name) \
    .apply(lambda args: storage.list_storage_account_keys(
        resource_group_name=args[0],
        account_name=args[1]
    )).apply(lambda accountKeys: accountKeys.keys[0].value)

pulumi.export("primary_storage_key", primary_key)
