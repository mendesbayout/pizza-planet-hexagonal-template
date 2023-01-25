variable "pizza_table_name" {
    type = string
    description = "DynamoDB table name"
}

variable "partition_key_name" {
    type = string
    default = "PK"
    description = "table partition key name"
}

variable "sorting_key_name" {
    type = string
    default = "SK"
    description = "table sorting key name"
}
