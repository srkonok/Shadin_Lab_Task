# Edit_badge

## Objective

Get the list of all badge that are created or edited

## API

            Path: /get-badge-list
            Method: post

## Environment Variable

          PrimaryTable: !Ref PrimaryTable
          SecondaryTable: !Ref SecondaryTable
          AURORA_DB_SECRET: !Ref AuroraSecretArn
          AURORA_CLUSTER_HOST: !Ref AuroraRWEndpoint
          SQS_URL: !Ref NotificationQueueUrl

## Flow

- In params event body is parsed and passed it to get_badge_wise_property_list
- In get_badge_wise_property_list SQL query is built and pagination is done
