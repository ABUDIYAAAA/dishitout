# ENDPOINTS

### `/random-dish`:
 - **Method:** GET 
 - **Use:** get a random dish
---

### `/dish/<course>`
- **Method:** GET
- **Categories:** [starter, main-course, dessert]
- **Use:** shows image of a randomly selected dish form user-selected course 

---

### `/all-dishes` 
- **Method:** GET ⋅
- **Use:** returns a list of all the possible dishes of all categories

---
```yaml
api:
    version: 1.0
    title: Dish Out API
    description: API for managing resources with authentication
    base_url: /api/v1

authentication:
    type: API Key
    header_name: X-API-Key
    required: true

endpoints:
    - path: /resources
        methods:
            - GET:
                    description: Retrieve all resources
                    responses:
                        200: Success
                        401: Unauthorized
            - POST:
                    description: Create a new resource
                    request_body:
                        type: application/json
                        required: true
                        schema:
                            properties:
                                name: 
                                    type: string
                                    description: Name of the resource
                                details: 
                                    type: string
                                    description: Details of the resource
                    responses:
                        201: Created
                        400: Bad Request
                        401: Unauthorized
    - path: /resources/{id}
        methods:
            - GET:
                    description: Retrieve a resource by ID
                    parameters:
                        - name: id
                            in: path
                            required: true
                            type: integer
                    responses:
                        200: Success
                        404: Not found
                        401: Unauthorized
            - PUT:
                    description: Update a resource by ID
                    parameters:
                        - name: id
                            in: path
                            required: true
                            type: integer
                    request_body:
                        type: application/json
                        required: true
                        schema:
                            properties:
                                name: 
                                    type: string
                                    description: Updated name of the resource
                                details: 
                                    type: string
                                    description: Updated details of the resource
                    responses:
                        200: Updated
                        400: Bad Request
                        404: Not found
                        401: Unauthorized
            - DELETE:
                    description: Delete a resource by ID
                    parameters:
                        - name: id
                            in: path
                            required: true
                            type: integer
                    responses:
                        204: No Content
                        404: Not found
                        401: Unauthorized
```

---
