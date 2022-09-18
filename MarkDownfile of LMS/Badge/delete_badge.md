# Delete_badge

## Objective

Try to delete created badge

## API

            Path: /delete-badge
            Method: post

## Environment Variable

          PrimaryTable: !Ref PrimaryTable
          SecondaryTable: !Ref SecondaryTable
          AURORA_DB_SECRET: !Ref AuroraSecretArn
          AURORA_CLUSTER_HOST: !Ref AuroraRWEndpoint
          SQS_URL: !Ref NotificationQueueUrl

## Models

    - [DeleteBadgeModel](../Models/DeleteBadgeModel)

## Flow

- Using DeleteBadgeModel event body is parsed
- if "badge_id" in badge_obj, it will pass it to delete_badge_from_db .
- from delete_badge_from_db function will get code, error, message
- in delete_badge_from_db function new badge and its property sql query built and executed. if deleted successfully message will be **Badge Deleted Successfully**. if can't delete the badge **Warning! Badge not deleted**. and also error message will be shown.
- Exception is handled (reverting changes because of exception)

> exception/error handle code

```
    except pymysql.IntegrityError as e:
        print("mysql error ",e.args)
        code = 'DB_ERROR'
        error = True
        message = str(e.args[1])

    except Exception as e:
        code = 'GENERIC'
        error = True
        message = str(e)
```
