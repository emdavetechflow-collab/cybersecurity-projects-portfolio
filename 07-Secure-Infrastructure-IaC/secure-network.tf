provider "aws" {
  region = "us-east-1"
}

# Create a network
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  
  tags = {
    Name      = "Secure-Network"
    Environment = "Production"
  }
}

# Create a secure subnet
resource "aws_subnet" "good_subnet" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = false # SAFE: No public internet IPs!
  
  tags = {
    Name      = "Secure-Private-Subnet"
    Environment = "Production"
  }
}