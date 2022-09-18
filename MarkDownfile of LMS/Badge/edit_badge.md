# Edit_badge

## Objective

Try to edit created badge

## API

            Path: /edit-badge
            Method: post

## Environment Variable

          PrimaryTable: !Ref PrimaryTable
          SecondaryTable: !Ref SecondaryTable
          AURORA_DB_SECRET: !Ref AuroraSecretArn
          AURORA_CLUSTER_HOST: !Ref AuroraRWEndpoint
          SQS_URL: !Ref NotificationQueueUrl

## Models

    - [UpdateBadgeModel](../Models/UpdateBadgeModel)

## Flow

- Using UpdateBadgeModel event body is parsed
- if "badge_properties" in badge_obj, it will be popped and included into badge property and pass it to edit_badge_into_db function.
- from edit_badge_into_db function will get code, error, message
- in edit_badge_into_db function new badge and its property sql query built and executed. if edited successfully message will be **'Badge edited successfully'**. if already badge exists **Badge name already exists**. and also error message will be shown.
- Exception is handled (reverting changes because of exception)

> exception/error handle code

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
        code = 'GENERIC'
        error = True
        print(str(e))
        message = str(e)
    return code, error, message

```
