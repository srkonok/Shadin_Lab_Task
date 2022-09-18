# Access_management_add

## Objective

Insert into accessmanagement DB

## API

        Path: /access-add
        Method: post

## Environment Variable

        AURORA_DB_SECRET: !Ref AuroraSecretArn
        AURORA_CLUSTER_HOST: !Ref AuroraRWEndpoint

## Models

    - [AccessManagementModel](../Models/AccessManagementModel)

## Flow

- Using AccessManagementModel event body is parsed
- Insert module_id, group_id, CRUD status into accessmanagement DB
- Exception is handled
- If created successfully the message will be **Permission Created Successfully"** and not **Failed to create Permission**
