resource "aws_sns_topic" "price_updates" {
  name = "price-updates-topic"
}

resource "aws_sns_topic_subscription" "topic_email_subscription" {
  topic_arn = aws_sns_topic.price_updates.arn
  protocol  = "email"
  endpoint  = var.email
}
