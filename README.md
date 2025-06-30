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

## Tools
- Python version and env management using [uv](https://github.com/astral-sh/uv)
- Linting and formatting using [ruff](https://github.com/astral-sh/ruff)
- Type checking using [pyright](https://github.com/microsoft/pyright)
- Git hooks using [pre-commit](https://github.com/pre-commit/pre-commit)
