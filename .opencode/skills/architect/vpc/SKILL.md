# VPC Skill

## Overview
Design VPC architecture with public/private subnets, NAT gateways, and VPC endpoints.

## VPC Structure

```
VPC CIDR: 10.0.0.0/16

Public Subnets (2 AZs):
- 10.0.1.0/24  (eu-west-2a)
- 10.0.2.0/24  (eu-west-2b)

Private Subnets (2 AZs):
- 10.0.10.0/24 (eu-west-2a)
- 10.0.11.0/24 (eu-west-2b)

Database Subnets (2 AZs):
- 10.0.20.0/24 (eu-west-2a)
- 10.0.21.0/24 (eu-west-2b)
```

## Components

| Component | Purpose |
|-----------|---------|
| aws_vpc | Main VPC container |
| aws_subnet | Subnet divisions |
| aws_internet_gateway | Outbound internet |
| aws_nat_gateway | Private subnet outbound |
| aws_route_table | Routing rules |
| aws_vpc_endpoint | S3/DynamoDB access |

## NAT Gateway

- Place in public subnet
- Enable auto-assign public IP on instances
- One NAT per AZ for HA

## VPC Endpoints

Required endpoints for private Lambda:
- `aws_vpc_endpoint.s3` (gateway type)
- `aws_vpc_endpoint.dynamodb` (gateway type)

## Security Groups

- Default deny all inbound
- Allow outbound as needed
- Security group for Lambda, RDS, ElastiCache
