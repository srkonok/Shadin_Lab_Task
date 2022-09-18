#Add_Category

## Objective

Creating a new category

## API

            Path: /cat-add
            Method: post

## Environment Variable

          AURORA_DB_SECRET: !Ref AuroraSecretArn
          AURORA_CLUSTER_HOST: !Ref AuroraRWEndpoint
          BUCKET_NAME: !Ref CategoryJsonBucket

## Models

    - [CategoryModel](../Models/CategoryModel)

## Flow

- in line accessing environment variable
- Using CategoryModel event body is parsed
- in Lambda handler function new badge and its property sql query built and executed. if created successfully message will be **Category Created Successfully**. if duplicated data exists message will be **Already exists**. and also error message will be **Failed to create Category**.
- Exception is handled (reverting changes because of exception)

> exception and error handle code

```
    except pymysql.IntegrityError as e:
        print(e.args)
        if e.args[0] == 1062:
            return get_response(
                status=409,
                error=True,
                message="Already exists",
            )
    except Exception as e:
        print(e)
        dict_connection.rollback()
        return get_response(
            status=400,
            error=True,
            message="Failed to create Category",
            data={
                "reason": e.__str__()
            }
        )
```
