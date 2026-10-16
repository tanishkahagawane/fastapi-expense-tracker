# FastAPI interview questions roadmap

Level 1 — FastAPI basics, HTTP, Pydantic, routing, CRUD, databases
Level 2 — Core backend -Authentication, dependencies, async, error handling, testing
Level 3 — Security, performance, deployment, architecture, system design

## 1. FastAPI fundamentals

## FastAPI basics

1. What is FastAPI, and what problems does it solve?
2. How is FastAPI different from Flask and Django?
3. Why is FastAPI considered fast?
4. What are ASGI and WSGI? Which one does FastAPI use?
5. What are Starlette and Pydantic, and what role does each play?
6. What happens when you start a FastAPI application?
7. What is Uvicorn, and how is it different from FastAPI?
8. What is the difference between an API and a REST API?
9. What are OpenAPI and Swagger UI?
10. How do you run a FastAPI app locally?

## Routing and HTTP methods

1. What is a path operation in FastAPI?
2. What is the difference between @app.get(), @app.post(), @app.put(), @app.patch(), and @app.delete()?
3. What is the difference between a path parameter and a query parameter?
4. How do you make a query parameter optional?
5. How do you set default values and validate query parameters?
6. What is APIRouter, and why should you use it?
7. How do you add a prefix and tags to a router?
8. What is the difference between returning a dictionary and returning a Response object?
9. What is a response_model, and why is it useful?
10. How do you set a custom HTTP status code for an endpoint?

## Request data and Pydantic

1. What is a Pydantic model?
2. How does FastAPI validate a JSON request body?
3. What happens when a request contains invalid data?
4. What is the difference between a Pydantic model and a database model?
5. What is the difference between required, optional, and nullable fields?
6. What are Field(), Query(), Path(), and Body() used for?
7. What is the difference between a list, a nested model, and a list of nested models?
8. How do you validate that an amount is positive or that a string has a minimum length?
9. What are model validators in Pydantic?
10. How do you prevent internal fields, such as password hashes, from appearing in API responses?

## HTTP and REST concepts

11. What are HTTP request and response headers?
12. What are the common HTTP status codes: 200, 201, 204, 400, 401, 403, 404, 409, and 422?
13. What is the difference between 401 Unauthorized and 403 Forbidden?
14. What does idempotency mean? Which HTTP methods are typically idempotent?
15. What is the difference between PUT and PATCH?
16. What are request headers, cookies, and query parameters?
17. What is JSON serialization?
18. What is pagination, and why is it important?
19. What is the difference between client-side and server-side validation?
20. What makes an API RESTful?

## 2. Dependencies and application structure

Priority 1 · One of the most important FastAPI-specific topics.

FastAPI's dependency injection system lets endpoints reuse logic for database sessions, authentication, and shared request requirements.

1. What is dependency injection?
2. What does `Depends()` do?
3. How do you create a custom dependency?
4. How do you share one dependency between multiple endpoints?
5. What is the difference between middleware and dependencies?
6. What are sub-dependencies?
7. What is `Annotated`, and why is it commonly used with `Depends()`?
8. How does a dependency using `yield` work?
9. How would you create a database session dependency?
10. How would you restrict certain endpoints to authenticated users?
11. What is the difference between `app.state` and dependency injection?
12. How do you organize a growing application using routers, schemas, models, services, and repositories?

## 3. CRUD operations and databases

Priority 1 · Especially important for your expense tracker.

13. What is CRUD? Explain create, read, update, and delete with HTTP methods.
14. What is the difference between SQL and NoSQL databases?
15. What are tables, rows, columns, primary keys, and foreign keys?
16. What is an ORM? Why use SQLAlchemy or SQLModel?
17. What is the difference between a database model and a Pydantic schema?
18. What are `engine`, `Session`, `commit()`, `refresh()`, and `rollback()`?
19. Why should you avoid creating a new database connection for every individual query?
20. Why should each request have an appropriately scoped database session?
21. How do you handle a record that does not exist?
22. How do you implement filtering, sorting, and pagination?
23. What are database indexes, and when should you use them?
24. What is a database transaction? Why is it important?
25. What is the difference between `flush()` and `commit()` in SQLAlchemy?
26. What are database migrations, and what does Alembic do?
27. What is the N+1 query problem?
28. How would you associate each expense with its owner?
29. How do you prevent one user from reading or modifying another user's expenses?
30. How would you handle two requests updating the same record at the same time?

## 4. Authentication and authorization

Priority 1–2 · Know the concepts and the basic implementation.

31. What is the difference between authentication and authorization?
32. How does a registration endpoint work?
33. Why should passwords never be stored as plain text?
34. What is password hashing? How do bcrypt and Argon2 fit into password security?
35. What is a JWT, and what are its header, payload, and signature?
36. What is the difference between access tokens and refresh tokens?
37. How does a client send a bearer token to an API?
38. How do you protect an endpoint using `Depends()`?
39. What is OAuth2, and how does it relate to bearer-token authentication?
40. How do you implement role-based access control, such as admin and regular users?
41. Where can tokens be stored, and what are the security trade-offs between cookies and browser storage?
42. What are CORS and CSRF? Are they the same thing?
43. How do you prevent users from accessing another user's private data?
44. Why should JWT payloads not contain secrets?
45. How would you handle an expired, invalid, or revoked token?

## 5. Async programming and concurrency

Priority 2 · A common point of confusion for Python developers.

FastAPI supports both `def` and `async def`. Choosing between them depends partly on whether the libraries you call support asynchronous operations.

46. What are `async` and `await` in Python?
47. What is the difference between synchronous and asynchronous programming?
48. What is blocking I/O?
49. What is the difference between concurrency and parallelism?
50. When should you use `async def` instead of `def` in a route?
51. What happens if you call a blocking function inside an `async def` endpoint?
52. Can an asynchronous endpoint call a synchronous database library?
53. Does using `async def` automatically make your API faster?
54. What is an event loop?
55. What happens when an endpoint awaits a slow external API?
56. How would you make several independent HTTP requests concurrently?
57. What is the difference between CPU-bound and I/O-bound work?
58. When would you use a thread pool, a process pool, or a task queue?

## 6. Error handling, middleware, and lifecycle

Priority 2

59. How do you raise an `HTTPException`?
60. What is the difference between raising an exception and returning an error dictionary?
61. How do you create a custom exception handler?
62. How do you handle unexpected server errors?
63. What is middleware, and when should you use it?
64. What are common middleware use cases, such as request logging and timing?
65. What is the difference between middleware and exception handlers?
66. What are application startup and shutdown events?
67. What is FastAPI's lifespan mechanism, and when would you use it?
68. How would you log errors without exposing sensitive information?
69. How would you add a request ID to logs to trace a failed request?
70. What are background tasks in FastAPI, and when are they appropriate?
71. When should you use Celery, RQ, or another task queue instead of a background task?

## 7. Testing and debugging

72. Why is automated API testing important?
73. What is `TestClient` in FastAPI?
74. How do you test a GET endpoint and a POST endpoint?
75. How do you assert response status codes and JSON data?
76. What is the difference between unit, integration, and end-to-end testing?
77. How do you test an endpoint that requires authentication?
78. How do you override dependencies during testing?
79. How would you test an endpoint without connecting to your production database?
80. What are fixtures in pytest?
81. How do you test validation failures and missing records?
82. What is mocking, and when is it useful?
83. How do you reproduce and debug an intermittent API failure?

## 8. Security and production readiness

84. What is the difference between validation and sanitization?
85. How do parameterized SQL queries help prevent SQL injection?
86. How do you prevent mass assignment or users modifying protected fields?
87. What is rate limiting, and why is it important?
88. How should you store secrets such as database URLs and signing keys?
89. Why should you use environment variables or a secrets manager?
90. How do you configure CORS safely?
91. Why should you avoid returning stack traces to clients in production?
92. How do you upload and validate files safely?
93. What is HTTPS, and why is it necessary?
94. How do you prevent insecure direct object references (IDOR)?
95. What are health checks, and what should a health endpoint verify?
96. What is the difference between development and production configuration?

## 9. Deployment, performance, and scaling

97. How would you deploy a FastAPI application?
98. What is Docker, and why would you containerize an API?
99. What are workers in Uvicorn or a production ASGI server?
100.  What is the difference between a process and a thread?
101.  What is a reverse proxy, and where do Nginx or a cloud load balancer fit?
102.  How do environment variables work in deployment?
103.  How would you connect a deployed API to a managed PostgreSQL database?
104.  What is connection pooling?
105.  How would you investigate a slow API endpoint?
106.  How can caching improve performance? What is Redis used for?
107.  What is a database connection limit, and how can multiple workers affect it?
108.  What are logs, metrics, and distributed traces?
109.  How do you handle database migrations during deployment?
110.  How would you scale an API that receives ten times more traffic?

## 10. Advanced FastAPI topics

These are good follow-up questions after you understand the essentials.

111. What are WebSockets, and when would you use them?
112. What is the difference between a WebSocket and HTTP polling?
113. What are streaming responses?
114. What is the difference between a `BackgroundTasks` job and a durable queued job?
115. What are API versioning strategies?
116. What are idempotency keys, and how could they prevent duplicate expense creation?
117. What is optimistic concurrency control?
118. What is the difference between offset and cursor pagination?
119. What are database isolation levels?
120. How would you design a webhook endpoint that safely handles retries?
121. What is graceful shutdown, and why does it matter?
122. How would you handle secrets and configuration across development, testing, and production?
123. How would you document a public API for other developers?
124. How would you make an API backward-compatible when changing a response schema?

## 11. Project-based questions about your expense tracker

These are particularly valuable because interviewers often use your own project to assess whether you understand the code you wrote.

125. Explain your project architecture. How does a request travel from the endpoint to the database and back?
126. Why did you choose FastAPI for this project?
127. What are the main API endpoints in your expense tracker?
128. How are expenses represented in your request schemas, database models, and response schemas?
129. How do you validate an expense amount, category, and date?
130. How do you handle invalid input and nonexistent expense IDs?
131. How would you implement filtering expenses by date range and category?
132. How would you calculate total expenses per month?
133. How would you implement pagination if a user had thousands of expenses?
134. How would you add user registration and login?
135. How would you ensure users can access only their own expenses?
136. How would you prevent a client from changing an expense's owner ID?
137. How would you handle two simultaneous requests updating an expense?
138. How would you write tests for creating, retrieving, updating, and deleting expenses?
139. How would you move your project from local development to a production deployment?
140. If your API suddenly became slow, how would you identify the bottleneck?
141. What would you improve in your current implementation if you had another week?
142. What technical challenge did you face, and how did you solve it?

## 12. Practical coding questions

Knowing the theory is not enough. Practice implementing these small tasks without copying a tutorial.

### Hands-on practice tracker

1. Build a CRUD API - Create, list, retrieve, update, and delete expenses.
2. Validate request bodies -Use Pydantic to validate amounts, dates, and categories.
3. Add pagination -Support skip/limit or page/page-size query parameters.
4. Filter expenses -Filter by category and date range.
5. Handle errors -Return correct status codes for missing records and invalid requests.
6. database persistence - Use SQLAlchemy or SQLModel with a relational database.
7. Add authentication- Register users, hash passwords, and protect endpoints.
8. Enforce ownership - Prevent a user from reading or modifying another user's expenses.
9. Write tests - Test successful requests, invalid inputs, and authentication failures.
10. Refactor the project - Separate routers, schemas, database models, and business logic.
