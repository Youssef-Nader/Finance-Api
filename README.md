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
#### - This endpoint should allow users to list and create financial transactions. Each transaction should
#### have fields like `transaction_date`, `description`, `amount`, and `user_id`.

#### Expected Outcoumes
#### DRF show all transactions created
![Endpoint 1](https://github.com/user-attachments/assets/91970607-86e3-4e26-af1b-cd0527317388)
