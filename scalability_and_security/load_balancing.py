```python
import boto3

def load_balancer():
    client = boto3.client('elbv2')

    # Create a load balancer
    response = client.create_load_balancer(
        Name='InfluenceAI-LoadBalancer',
        Subnets=[
            'subnet-0d3a3a3a3',
            'subnet-0d3a3a3b3',
            'subnet-0d3a3a3c3',
        ],
        SecurityGroups=[
            'sg-0d3a3a3a3',
        ],
        Scheme='internet-facing',
        Tags=[
            {
                'Key': 'Project',
                'Value': 'InfluenceAI'
            },
        ],
        Type='application',
        IpAddressType='ipv4'
    )

    # Create a target group
    response = client.create_target_group(
        Name='InfluenceAI-TargetGroup',
        Protocol='HTTP',
        Port=80,
        VpcId='vpc-0d3a3a3a3',
        HealthCheckProtocol='HTTP',
        HealthCheckPort='traffic-port',
        HealthCheckEnabled=True,
        HealthCheckIntervalSeconds=30,
        HealthCheckTimeoutSeconds=5,
        HealthyThresholdCount=5,
        UnhealthyThresholdCount=2,
        Matcher={
            'HttpCode': '200'
        },
        TargetType='instance'
    )

    # Register targets
    response = client.register_targets(
        TargetGroupArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/InfluenceAI-TargetGroup/6d0ecf831eec9f09',
        Targets=[
            {
                'Id': 'i-0d3a3a3a3',
                'Port': 80,
            },
        ]
    )

    # Create a listener
    response = client.create_listener(
        LoadBalancerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/InfluenceAI-LoadBalancer/50dc6c495c0c9188',
        Protocol='HTTP',
        Port=80,
        DefaultActions=[
            {
                'Type': 'forward',
                'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/InfluenceAI-TargetGroup/6d0ecf831eec9f09',
            },
        ]
    )

if __name__ == "__main__":
    load_balancer()
```