resource "aws_api_gateway_rest_api" "func" {
  name        = var.server_name
  description = var.server_description
}

resource "aws_api_gateway_resource" "proxy" {
  rest_api_id = aws_api_gateway_rest_api.func.id
  parent_id   = aws_api_gateway_rest_api.func.root_resource_id
  path_part   = var.proxy
}

resource "aws_api_gateway_method" "proxy" {
  rest_api_id   = aws_api_gateway_rest_api.func.id
  resource_id   = aws_api_gateway_resource.proxy.id
  http_method   = var.http_method
  authorization = var.authorization
}

resource "aws_api_gateway_integration" "lambda" {
  rest_api_id = aws_api_gateway_rest_api.func.id
  resource_id = aws_api_gateway_method.proxy.resource_id
  http_method = aws_api_gateway_method.proxy.http_method

  integration_http_method = var.integration_http_method
  type                    = var.type
  uri                     = aws_lambda_function.func.invoke_arn
}

resource "aws_api_gateway_method" "proxy_root" {
  rest_api_id   = aws_api_gateway_rest_api.func.id
  resource_id   = aws_api_gateway_rest_api.func.root_resource_id
  http_method   = var.http_method
  authorization = var.authorization
}

resource "aws_api_gateway_integration" "lambda_root" {
  rest_api_id = aws_api_gateway_rest_api.func.id
  resource_id = aws_api_gateway_method.proxy_root.resource_id
  http_method = aws_api_gateway_method.proxy_root.http_method

  integration_http_method = var.integration_http_method
  type                    = var.type
  uri                     = aws_lambda_function.func.invoke_arn
}

resource "aws_api_gateway_deployment" "func" {
  depends_on = [
    "aws_api_gateway_integration.lambda",
    "aws_api_gateway_integration.lambda_root",
  ]

  rest_api_id = aws_api_gateway_rest_api.func.id
  stage_name  = var.stage_name
}
