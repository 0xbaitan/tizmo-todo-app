data "aws_iam_policy_document" "tizmo_lambda_management_policy" {

  statement {
    sid    = "AllowLambdaReadAndList"
    effect = "Allow"
    actions = [
      "lambda:ListFunctions",
      "lambda:GetFunction",
      "lambda:GetFunctionConfiguration",
    ]
    resources = ["*"]
  }

  statement {
    sid    = "AllowLambdaCRUD"
    effect = "Allow"
    actions = [
      "lambda:CreateFunction",
      "lambda:UpdateFunctionCode",
      "lambda:UpdateFunctionConfiguration",
      "lambda:DeleteFunction",
      "lambda:InvokeFunction",
      "lambda:AddPermission",
      "lambda:RemovePermission",
    ]
    resources = ["arn:aws:lambda:${var.aws_region}:${var.aws_account_id}:function:tizmo/*"]
  }

  statement {
    sid    = "AllowExecutionRoleManagement"
    effect = "Allow"
    actions = [
      "iam:CreateRole",
      "iam:GetRole",
      "iam:PutRolePolicy",
      "iam:DeleteRolePolicy",
      "iam:AttachRolePolicy",
      "iam:DetachRolePolicy",
      "iam:DeleteRole",
      "iam:PassRole",
    ]
    resources = ["arn:aws:iam::${var.aws_account_id}:role/tizmo/*"]
  }

  statement {
    sid    = "AllowLogGroupManagement"
    effect = "Allow"
    actions = [
      "logs:CreateLogGroup",
      "logs:DescribeLogGroups",
    ]
    resources = ["arn:aws:logs:${var.aws_region}:${var.aws_account_id}:log-group:/aws/lambda/tizmo/*"]
  }

  statement {
    sid    = "AllowLogStreamOperations"
    effect = "Allow"
    actions = [
      "logs:CreateLogStream",
      "logs:PutLogEvents",
    ]
    resources = ["arn:aws:logs:${var.aws_region}:${var.aws_account_id}:log-group:/aws/lambda/tizmo/*:*"]
  }
}

resource "aws_iam_policy" "tizmo_lambda_developer" {
  name        = "tizmo-lambda-developer"
  description = "IAM policy for Lambda developers to create and manage tizmo functions"
  policy      = data.aws_iam_policy_document.tizmo_lambda_management_policy.json
  provider = {
    aws.iam_admin
  }
}
