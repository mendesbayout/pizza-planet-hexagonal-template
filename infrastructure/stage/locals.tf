locals {
  stage            = "stage"
  region           = "us-east-1"
  ecr_name         = "${local.stage}-clients-ecr"
  lambda_role_name = "${local.stage}-api-lambda-role"
  lambda_func_name = "${local.stage}-api-lambda-function"
}
