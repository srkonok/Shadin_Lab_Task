# Access_management_delete

## Objective

Delete from accessmanagement DB

## API

            Path: /access-delete/{access_id}/
            Method: delete

## Environment Variable

          AURORA_DB_SECRET: !Ref AuroraSecretArn
          AURORA_CLUSTER_HOST: !Ref AuroraRWEndpoint

## Models

    - [AccessManagementModel](../Models/AccessManagementModel)

## Flow

- retrieve events according to the given parameters(access_id)
- delete from accessmanagement DB where access_id is matched
- Exception is handled (reverting changes because of exception)
- If deleted successfully the message will be **Permission Deleted Successfully"** and not **Failed to Delete Permission**
- If access_id is none then message will be **Missing parameters**
