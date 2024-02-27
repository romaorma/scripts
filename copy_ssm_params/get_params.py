import boto3

client = boto3.client('ssm')

filename = 'aut_ssm_params_staging.txt'
prefix = '/aut/'
params = []

def p_names (params, response):
  if response['Parameters']:
    for p in response['Parameters']:
      params.append(p['Name'])

response = client.describe_parameters(ParameterFilters=[
        {
            'Key': 'Name',
            'Option': 'BeginsWith',
            'Values': [
                prefix,
            ]
        },
    ], MaxResults=50)

p_names(params, response)

while len(response['Parameters']) != 0:
  response = client.describe_parameters(ParameterFilters=[
        {
            'Key': 'Name',
            'Option': 'BeginsWith',
            'Values': [
                '/aut/',
            ]
        },
    ], NextToken = response['NextToken'], MaxResults=50)
  p_names(params, response)

print("Total parameters found: {}".format(len(params)))

with open(filename, "w") as results:
  results.write('')

with open(filename, "a") as results:
  for p in params:
    response = client.get_parameter(
      Name=p
    )
    results.write("{0} {1}\n".format(p, response['Parameter']['Value']))