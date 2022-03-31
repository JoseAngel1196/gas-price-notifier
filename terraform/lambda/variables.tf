variable "gasoline_prices_table_arn" {
  type = string
}

variable "price_publisher_arn" {
  type    = string
  default = "arn:aws:lambda:us-east-1:008735640664:function:aws-price-fetcher-dev-price_publisher"
}

variable "gasoline_price_table_stream_arn" {
  type = string
}

variable "sns_arn" {
  type = string
}
