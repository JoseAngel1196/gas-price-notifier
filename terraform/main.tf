module "lambda" {
  source                          = "./lambda"
  gasoline_prices_table_arn       = module.dynamodb.gasoline_prices_table_arn
  gasoline_price_table_stream_arn = module.dynamodb.dynamodb_stream_arn
  sns_arn                         = module.sns.sns_arn
}

module "dynamodb" {
  source = "./dynamodb"
}

module "sns" {
  source = "./sns"
  email  = var.email
}
