resource "azurerm_storage_account" "my_storage" {
  name                     = "mystorage${random_string.suffix.result}"
  account_tier             = "Standard"
  location                 = var.location
  resource_group_name      = azurerm_resource_group.storage_rg.name
  account_replication_type = "LRS"

  tags = { enviroment = "staging" }
}

resource "azurerm_storage_container" "csv_container" {
  name                  = "youtube-analytics-csv"
  storage_account_id    = azurerm_storage_account.my_storage.id
  container_access_type = "private"

}

# resource "azurerm_storage_blob" "example" {
#   name                 = "Totalt.csv"
#   storage_container_id = azurerm_storage_container.csv_container.id
#   type                 = "Block"
#   source               = "data/Totalt.csv"
# }

resource "azurerm_storage_blob" "example" {
  for_each             = fileset("data", "*.csv")
  name                 = each.value
  storage_container_id = azurerm_storage_container.csv_container.id
  type                 = "Block"
  source               = "data/${each.value}"
}
