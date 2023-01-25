terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.9.0"
    }
  }
  # backend "s3" {
  #   bucket  = "stage-tfstate-clients"
  #   key     = "terraform/state/clients.tfstate"
  #   region  = "us-east-1"
  #   encrypt = true
  # }
}

provider "aws" {
  region = "us-east-1"
}

################################################
#                    S3                        #
################################################

module "s3_tfstate" {
  source      = "../common/s3"
  bucket_name = "${local.stage}-tfstate-clients"
}

module "s3_frontend" {
  source      = "../common/s3-static"
  bucket_name = "${local.stage}-frontend-clients"
}

################################################
#                    ECR                       #
################################################
module "ecr_clients" {
  source   = "../common/ecr"
  ecr_name = local.ecr_name
}

################################################
#               DYNAMODB                       #
################################################
module "dynamodb" {
  source                   = "../common/dynamodb"
  clients_table_name       = "${local.stage}-clients-app"
}

################################################
#                 LAMBDA                       #
################################################

module "lambda_clients" {
  source                = "../common/lambda"
  ecr_uri               = module.ecr_clients.ecr.repository_url
  tag                   = var.image_tag # tbd not existing
  timeout               = 15
  memory_size           = 512
  role_name             = local.lambda_role_name
  func_name             = local.lambda_func_name
  source_arn            = "arn:aws:iam::123456789012:user/johndoe" #module.api_gw.execution-arn
  stage_name            = local.stage
  concurrent_executions = 12
  permissions = [
    {
      "Effect" : "Allow",
      "Action" : [
        "dynamodb:*"
      ],
      "Resource" : "*"
    }
  ]
  env_variables = [{
    "SUPER_SECRET1"   = 5432
    "DATABASE_REGION" = local.region
    "ENV"             = local.stage
    "HOSTNAME"        = "google.com"
    }
  ]
}
