import boto3

client = boto3.client('ssm')

filename = 'aut_ssm_params_staging.txt'

key = ''
value = ''
type = 'String'
tier = 'Standard'

with open(filename, "r") as param_list:
    contents = param_list.readlines()

    for line in contents:
      kv = line.split(" ", 1)
      key = kv[0]
      value = kv[1].strip()
     
      response = client.put_parameter(
        Name=key,
        Value=value,
        Overwrite=True,
        Type=type,
        Tier=tier
      )