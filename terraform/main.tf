provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "app_server" {
  ami           = "ami-0e9bbd70d26d7cf4f" # Amazon Linux 2
  instance_type = "t2.medium"
  key_name      = var.key_name

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install docker -y
              service docker start
              usermod -a -G docker ec2-user
              chkconfig docker on
              curl -sL https://rpm.nodesource.com/setup_16.x | bash -
              yum install -y nodejs git
              EOF

  tags = {
    Name = "SpeechAnalyticsApp"
  }
}

output "instance_ip" {
  value = aws_instance.app_server.public_ip
}
