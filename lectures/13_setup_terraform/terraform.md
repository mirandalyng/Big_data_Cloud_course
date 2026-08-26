## Step by step terraform

- terraform init
- terraform plan
  (what are the things that we want to create)
- terraform apply
- terraform destroy

  "listOfAllowedLocations":
  "value": - "germanywestcentral", - "austriaeast", - "denmarkeast", - "norwayeast", - "polandcentral"

**Run in terminal to see countries**

    ````
    az policy assignment list --query "[?displayName=='Allowed resource deployment regions'].{Name:name}" --output table
    ````

    ````
    az policy assignment show --name <NAMN> --query "parameters"
    ````
