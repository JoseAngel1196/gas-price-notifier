resource "aws_dynamodb_table" "gasoline_prices_table" {
  name           = "GasolinePrices"
  hash_key       = "gasolinePriceId"
  range_key      = "createdAt"
  read_capacity  = 20
  write_capacity = 20

  attribute {
    name = "towns"
    type = "S"
  }

  attribute {
    name = "price"
    type = "S"
  }
}
