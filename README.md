# ProShop Ecommerce Website With FastAPI + React

## Frontend
The only thing I changed from original is incorporated fixes from the community.
They include the following PRs:
- [Reset productDetails before request](https://github.com/divanov11/proshop_django/pull/10)
- [Update ProductScreen.js](https://github.com/divanov11/proshop_django/pull/13)
- [fixed cart screen. removed item no longer get added after reloading the cartscreen](https://github.com/divanov11/proshop_django/pull/16)
- [Update Rating.js](https://github.com/divanov11/proshop_django/pull/28)
- [Update orderActions.js](https://github.com/divanov11/proshop_django/pull/29)
- [Solve payment method issue correctly](https://github.com/divanov11/proshop_django/pull/32)
- [Make user not available to placeorder with 0 items](https://github.com/divanov11/proshop_django/pull/33)
- [reset the review every time we render ProductScreen](https://github.com/divanov11/proshop_django/pull/34)

## API
### admin/

### /
index.html

### api

#### products
##### GET /
* Get all products
* If given - filter by keyword
* Limit to 5 per page
##### POST create/
Create new product and return it, only for admin
##### POST? upload/
Update image of the product, only for admin
##### POST {product_id}/reviews/
Add product review from a given user
##### GET top/
Get top 5 products by rating
##### GET {product_id}/
Get product
##### PUT update/{product_id}/
Update the product (not image?), only for admin
##### DELETE delete/{product_id}/
Delete the product, only for admin

#### users
##### GET /
Returns all users, only for admin
##### GET {user_id}/
Returns one user, only for admin
##### login/
Django REST Framework handles this, need more investigation
##### POST register/
User registration
##### GET profile/
Get current users profile
##### PUT profile/update/
Update current users profile
##### PUT update/{user_id}/
Update current user
##### DELETE delete/{user_id}/
Delete the user, only for admin

#### orders
##### GET /
All orders, only for admin
##### POST add/
Create new order, add items to the order
##### GET myorders/
Get current users orders
##### PUT {order_id}/deliver/
Mark order as delivered, only for admin
##### GET {order_id}/
Get the order, only for admin
##### PUT {order_id}/pay/
Mark order as paid
