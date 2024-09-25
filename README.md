# Finance-Api
## Approach
#### This approach to bulid Finance API using python,django and django rest framework(DRF),The api will provide endpoints for managing financial transactions, users, and generating financial reports.

## Limitations
#### - The Endpoint 4 and 5 after doing a lot of search we can not reach the accurate result to implement the endpoints,
### but we make a comments have the code of each endpoint but not accurate you can read and dsicover that.
#### Endpoint 4: `/api/users/<user_id>/transactions/` (GET)
#### - Allow users to retrieve their own transactions based on user ID
#### Endpoint 5: `/api/reports/` (GET)
#### - Implement an endpoint that generates financial reports, such as monthly or yearly
#### summaries of transactions, for a given user


## Test Cases With Postman
#### Endpoint 1: `/api/transactions/` (GET and POST)
#### Each transaction should have fields like `transaction_date`, `description`, `amount`, and `user_id`.

#### Expected Outcoumes
#### - This endpoint should allow users to list and create financial transactions
![Endpoint 1](https://github.com/user-attachments/assets/91970607-86e3-4e26-af1b-cd0527317388 )



#### Endpoint 2: `/api/transactions/<transaction_id>/` (GET, PUT, and DELETE)
#### Expected Outcomes
#### - This endpoint should allow users to retrieve, update, and delete individual financial transactions
#### based on their unique IDs.
![Endpoint 2](https://github.com/user-attachments/assets/f77484c1-9198-4321-83d2-f74e78c1b3c0)



####  Endpoint 3: `/api/users/` (GET)
#### Expected Outcomes
#### - Create an endpoint to list all registered users.
![Endpoint 3](https://github.com/user-attachments/assets/2dbda35e-b6e9-4c3f-99ab-2b52eb7c9508)


