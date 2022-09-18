# Add_badge

## Objective

Try to creating a new badge

## API

            Path: /add-badge
            Method: post

## Environment Variable

          PrimaryTable: !Ref PrimaryTable
          SecondaryTable: !Ref SecondaryTable
          AURORA_DB_SECRET: !Ref AuroraSecretArn
          AURORA_CLUSTER_HOST: !Ref AuroraRWEndpoint
          SQS_URL: !Ref NotificationQueueUrl

## Models

    - [BadgeModel](../Models/BadgeModel)

## Flow

- Using BadgeModel event body is parsed
- if "badge_properties" in badge_obj, it will popped and included into badge property and pass it to add_badge_into_db function.
- from add_badge_into_db function will get code, error, message, data
- in add_badge_into_db function new badge and its property sql query built and executed. if created successfully message will be **Badge and it's property Created Successfully**. if duplicated data exists message will be **Badge name already exists**. and also error message will be shown.
- Exception is handled (reverting changes because of exception)

> exception and error handle code

```
    except pymysql.IntegrityError as e:
        print("mysql error ", e.args)
        code = 'DB_ERROR'
        error = True

        if e.args[0] == 1062:
            code = 'DUPLICATE_DATA'
            message = f"Badge name already exists"
        else:
            message = str(e.args[1])

    except Exception as e:
        print(str(e))
        code = 'GENERIC'
        error = True
        message = str(e)
```
