resource "aws_dynamodb_table" "gasoline_prices_table" {
  name           = "GasolinePrices"
  hash_key       = "publishedAt"
  read_capacity  = 20
  write_capacity = 20

  attribute {
    name = "publishedAt"
    type = "S"
  }
}
