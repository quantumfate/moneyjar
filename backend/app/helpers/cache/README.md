# so I store the materialized views in the database and cache them with redis?

Yes, you can store the materialized views in the database and use Redis to cache them. Materialized views can be created and refreshed in the database, and Redis can be used to store the views in cache so that they can be accessed more quickly. This can help improve the performance of your application, as accessing data from Redis is generally faster than accessing it from the database.

To implement this, you can create a Redis cache in your application and store the materialized views in it using Redis commands such as SET and GET. You can also set a time-to-live (TTL) for the views in the cache so that they expire after a certain amount of time, at which point they can be refreshed from the database. This can help ensure that the data in the cache is up to date.

It's important to consider the trade-offs between using a database and a cache, as well as the appropriate TTL for the cache. You'll need to balance the need for fresh data with the overhead of refreshing the cache. You may also want to consider using a cache invalidation strategy, such as storing a version number with each view in the cache and invalidating the cache when the version number changes.

# I could probably compute a relative value for each user accessing the database to estimate how much data I would have to query on a regular base and then I setup a schedule to refresh the data for each user

Yes, you can store the materialized views in the database and cache them with Redis. This way, you can use Redis as a cache for the materialized views, which will allow you to retrieve the data from the cache in real-time, rather than having to query the database every time you need to access the data.

To refresh the data for each user, you can set up a schedule using a task scheduler like Celery or APScheduler. This way, you can specify a time interval at which the materialized views should be refreshed, and the task scheduler will take care of refreshing the data for each user. You can also use a combination of Redis and a task scheduler to refresh the data on demand, rather than on a fixed schedule.

It's important to note that materialized views are best suited for cases where you need to access large amounts of data on a regular basis, and where the data is relatively static. If you have a lot of data that is frequently updated, you might want to consider other approaches, such as using a cache-aside pattern or a read-through cache.
