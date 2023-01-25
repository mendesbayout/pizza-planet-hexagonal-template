variable "bucket_name" {
  type        = string
  description = "The name for the bucket where the website will allocate"
}

variable "index_page" {
  type        = string
  default     = "index.html"
  description = "This is the name of the index page of your static website"
}

variable "error_page" {
  type        = string
  default     = "error.html"
  description = "This is the name of the error page of your static website"
}
