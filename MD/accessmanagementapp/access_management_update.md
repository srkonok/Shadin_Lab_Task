# Access_management_update

## Objective

Updated accessmanagement DB

## API

            Path: /access-update
            Method: put

## Environment Variable

          AURORA_DB_SECRET: !Ref AuroraSecretArn
          AURORA_CLUSTER_HOST: !Ref AuroraRWEndpoint

## Models

    - [AccessManagementModel](../Models/AccessManagementModel)

## Flow

- Using AccessManagementModel event body is parsed
- update ID and CRUD status into accessmanagement DB
- Exception is handled (reverting changes because of exception)
- If updated successfully the message will be **Permission Updated Successfully"** and not **Failed to Update Permission**
