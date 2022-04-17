"""An Azure RM Python Pulumi program"""

import pulumi
from pulumi_azure_native import storage
from pulumi_azure_native import resources
from pulumi import automation as auto
import pulumi_azure_native as azure_native

org_code = 'TGT'
org_name = 'Turagit'
loc_code = 'SYD'

app_type = 'ARG'
owner = 'Peter M'
stack_name = pulumi.get_stack()
project_name = pulumi.get_project()


'TGT-DEV-SYD-ARG-Networks-001'
# stack_name = auto.fully_qualified_stack_name("turagittech", project_name, stack_name)
resource_group_network_name = org_code + '-' + loc_code + '-' + stack_name.upper() + '-' + app_type + '-' + 'Network'

resource_group_data_name = org_code + '-' + loc_code + '-' + stack_name.upper() + '-' + app_type + '-' + 'Data'

resource_group_admin_name = org_code + '-' + loc_code + '-' + stack_name.upper() + '-' + app_type + '-' + 'Admin'

resource_group_apps_name =  org_code + '-' + loc_code + '-' + stack_name.upper() + '-' + app_type + '-' + 'Apps'

resource_group_data = azure_native.resource_group.ResourceGroup(resource_group_data_name)

resource_group_network = azure_native.resource_group.ResourceGroup(resource_group_network_name)

resource_group_admin = azure_native.resource_group.ResourceGroup(resource_group_admin_name)

resource_group_apps = azure_native.resource_group.ResourceGroup(resource_group_apps_name)


stack_name = auto.fully_qualified_stack_name("turagittech2", project_name, stack_name)
print(stack_name)


