
resource "aws_dynamodb_table" "dynamodb_pizzaplanet_table" {
  name           = var.clients_table_name
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = var.partition_key_name
  range_key      = var.sorting_key_name

  attribute {
    name = var.partition_key_name
    type = "S"
  }

  attribute {
    name = var.sorting_key_name
    type = "S"
  }

}
