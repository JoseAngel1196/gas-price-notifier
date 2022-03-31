output "lambda_role_arn" {
  value = module.lambda.role_arn
}

output "sns_arn" {
  value = module.sns.sns_arn
}
