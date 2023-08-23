provider "aws" {
  region = "us-east-1"
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

resource "aws_s3_bucket" "trigger_check" {
  bucket = "my-trigger-check-bucket"
  acl    = "private"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        kms_master_key_id = "some-key"  # Master Key is defined
        sse_algorithm     = "AES256"    # Algorithm is AES256
      }
    }
  }

  versioning {
    mfa_delete = true
  }
}
