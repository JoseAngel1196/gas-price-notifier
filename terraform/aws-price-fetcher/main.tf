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
