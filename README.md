# ENDPOINTS

```yaml
api:
    version: 1.0
    title: DISHITOUT API
    description: API for selecting a random dish and displaying its image.

endpoints:
    - path: /random-dish
        methods:
            - GET:
                    description: Retrieves a random dish from a set of dishes of different categories.
                    responses:
                        200: Success
                        401: Unauthorized
    - path: /dish/<course>
        methods:
            - GET:
                    description: Retrieve a random dish from a user-provided course.
                    parameters:
                        - starters
                        - main-course
                        - dessert
    - path: /all-dishes
        methods:
            - GET:
                    description: Retrieves all the dishes from all the courses.
```

---


