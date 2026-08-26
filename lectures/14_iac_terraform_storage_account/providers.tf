terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 5.0" #5.0 ≤ x < 6.0
    }
  }
  # pessimistic operator 
  # 1.1.0 ≤ x < 2.0.0
  required_version = "~> 1.1"
}

provider "azurerm" {
  features {

  }
}
