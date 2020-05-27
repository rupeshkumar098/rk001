provider "aws" {
  profile    = "default"
  region     = "eu-central-1"
}

#creating_IAM_user
resource "aws_iam_user" "user" {
  name = "test-user"
}





#Creating_policy
resource "aws_iam_policy" "policy" {
 name = "test-policy"
 policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {  "Action": [

        "lambda:*",

		
		"s3:Get*",
        "s3:List*",
		
	    "cloudwatch:Get*",
        "cloudwatch:List*"
        
      ],

      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
EOF
}

#Attaching_Policy_to_our_IAM_user
resource "aws_iam_user_policy_attachment" "test-attach" {
  user       = "${aws_iam_user.user.name}"
  policy_arn = "${aws_iam_policy.policy.arn}"
}



