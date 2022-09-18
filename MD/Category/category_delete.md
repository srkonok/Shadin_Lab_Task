#Delete_Category

## Objective

Deleting a category which is created earlier

## API
            Path: /cat-delete/{cat_id}
            Method: delete

## Environment Variable

          AURORA_DB_SECRET: !Ref AuroraSecretArn
          AURORA_CLUSTER_HOST: !Ref AuroraRWEndpoint 
          BUCKET_NAME: !Ref CategoryJsonBucket
## Table name

table_name = 'category'

## Flow

- in line accessing environment variable
- Using CategoryModel event body is parsed
- in Lambda handler function new badge and its property sql query built and executed. if created successfully message will be **Category Created Successfully**. if duplicated data exists message will be **Already exists**. and also error message will be **Failed to create Category**.
- Exception is handled (reverting changes because of exception)

> exception and error handle code

```
    except Exception as e:
        print(e)
        dict_connection.rollback()
        return get_response(
            status=400,
            error=True,
            message="Failed to Delete Category",
        )
```
