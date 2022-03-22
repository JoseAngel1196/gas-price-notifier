resource "aws_s3_bucket" "price_fetcher_deployment" {
  bucket = "price-fetcher-serverlessdeploymentbucket"

  tags = {
    Name = "price-fetcher-serverlessdeploymentbucket"
  }
}

resource "aws_s3_bucket_public_access_block" "deployment_bucket_public_policy" {
  bucket                  = aws_s3_bucket.price_fetcher_deployment.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_iam_role" "iam_for_lambda" {
  name = "Price-Notifier-role"
  assume_role_policy = jsonencode(
    {
      Statement = [
        {
          Action = "sts:AssumeRole"
          Effect = "Allow"
          Principal = {
            Service = "lambda.amazonaws.com"
          }
        },
      ]
      Version = "2012-10-17"
    }
  )
}

resource "aws_iam_role_policy_attachment" "lambda_attach_policy" {
  role       = aws_iam_role.iam_for_lambda.name
  policy_arn = aws_iam_policy.iam_role_policy_for_lambda.arn
}