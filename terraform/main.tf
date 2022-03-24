module "lambda" {
  source                    = "./lambda"
  gasoline_prices_table_arn = module.dynamodb.gasoline_prices_table_arn
}

module "dynamodb" {
  source = "./dynamodb"
}
