# Edit_Category

## Objective

Editing a category which is created earlier

## API

            Path: /cat-update
            Method: put

## Environment Variable

          AURORA_DB_SECRET: !Ref AuroraSecretArn
          AURORA_CLUSTER_HOST: !Ref AuroraRWEndpoint
          BUCKET_NAME: !Ref CategoryJsonBucket

## Table name

table_name = 'category'

## Flow

- in line accessing environment variable
- Using CategoryModel event body is parsed
- in Lambda handler function new badge and its property sql query built and executed. if edited successfully message will be **Category updated Successfully**. if duplicated data exists message will be **Already exists**. and also error message will be **Failed to edit Category**.
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
            message="Failed to Update Category",
            data={
                "reason": e.__str__()
            }
        )
```
