terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.9.0"
    }
  }
}

provider "aws" {
  region     = var.REGION
  access_key = var.TF_AWS_ACCESS_KEY
  secret_key = var.TF_AWS_SECRET_KEY
  token      = var.TF_AWS_SESSION_TOKEN
}


module "dynamodb" {
  source                   = "../common/dynamodb"
  clients_table_name    = "${local.stage}-pizzaplanet-app"

}
