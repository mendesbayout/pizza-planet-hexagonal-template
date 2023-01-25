variable "server_name" {
  type = string
}

variable "server_description" {
  type = string
}

variable "proxy" {
  type = string
  default = "{proxy+}"
}

variable "http_method" {
  type = string
  default = "ANY"
}

variable "authorization" {
  type = string
  default = "NONE"
}

variable "integration_http_method" {
  type = string
  default = "POST"
}

variable "type" {
  type = string
  default = "AWS_PROXY"
}

variable "stage_name" {
  type = string
  description = "stage deployment name"
}
