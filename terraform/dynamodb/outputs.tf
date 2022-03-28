output "gasoline_prices_table_arn" {
  value = aws_dynamodb_table.gasoline_prices_table.arn
}

output "dynamodb_stream_arn" {
  value = aws_dynamodb_table.gasoline_prices_table.stream_arn
}
