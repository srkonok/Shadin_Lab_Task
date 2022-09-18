# Access_management_list

## Objective

Show list acocording to groupp_id from accessmanagement DB

## API

            Path: /access-list/{group_id}/
            Method: get

## Environment Variable

          AURORA_DB_SECRET: !Ref AuroraSecretArn
          AURORA_CLUSTER_HOST: !Ref AuroraRWEndpoint

## Models

    - [AccessManagementModel](../Models/AccessManagementModel)

## Flow

- retrieve events according to the given parameters(group_id)
- left join using group_id into accessmanagement DB
- If group_id is none, message will be **"Missing required parameters or invalid request**
