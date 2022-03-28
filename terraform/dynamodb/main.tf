resource "aws_dynamodb_table" "gasoline_prices_table" {
  name             = "GasolinePrices"
  hash_key         = "publishedAt"
  read_capacity    = 20
  write_capacity   = 20
  stream_enabled   = true
  stream_view_type = "NEW_AND_OLD_IMAGES"

  attribute {
    name = "publishedAt"
    type = "S"
  }
}

resource "aws_lambda_event_source_mapping" "gasoline_prices_stream" {
  event_source_arn  = aws_dynamodb_table.gasoline_prices_table.stream_arn
  function_name     = var.price_publisher_arn
  starting_position = "LATEST"
}
