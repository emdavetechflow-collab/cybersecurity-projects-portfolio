provider "aws" {
  region = "us-east-1"
}

# Create a network
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "Insecure-Network"
  }
}

# Create a subnet (A smaller piece of the network)
resource "aws_subnet" "bad_subnet" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true # DANGER: This gives everything a public internet IP!
}