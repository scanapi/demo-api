# ScanAPI Report



## Request: GET http://demo.scanapi.dev/api/health/

HEADERS:
<details><summary></summary><p>
            
```
{'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '2', 'Content-Type': 'application/json'}
```
</p></details>

### Response: 200 

Is redirect? False

HEADERS:
<details><summary></summary><p>
            
```
{'Date': 'Sat, 14 Dec 2019 12:19:25 GMT', 'Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Set-Cookie': '__cfduid=d3dbbdfab20f1d81ffd0d50dbc2c5e5551576325965; expires=Mon, 13-Jan-20 12:19:25 GMT; path=/; domain=.scanapi.dev; HttpOnly', 'X-Frame-Options': 'DENY', 'X-Content-Type-Options': 'nosniff', 'Via': '1.1 vegur', 'CF-Cache-Status': 'DYNAMIC', 'Server': 'cloudflare', 'CF-RAY': '54502043eeeff603-GRU', 'Content-Encoding': 'gzip'}
```
</p></details>

Content:
<details><summary></summary><p>
            
```

OK!

```
</p></details>



## Request: GET http://demo.scanapi.dev/api/languages/

HEADERS:
<details><summary></summary><p>
            
```
{'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '2', 'Content-Type': 'application/json'}
```
</p></details>

### Response: 200 

Is redirect? False

HEADERS:
<details><summary></summary><p>
            
```
{'Date': 'Sat, 14 Dec 2019 12:19:26 GMT', 'Content-Type': 'application/json', 'Content-Length': '37', 'Connection': 'keep-alive', 'Set-Cookie': '__cfduid=dac6bf103576b82c638c3294a3bcf02e21576325965; expires=Mon, 13-Jan-20 12:19:25 GMT; path=/; domain=.scanapi.dev; HttpOnly', 'X-Frame-Options': 'DENY', 'X-Content-Type-Options': 'nosniff', 'Via': '1.1 vegur', 'CF-Cache-Status': 'DYNAMIC', 'Server': 'cloudflare', 'CF-RAY': '5450204678a1f5db-GRU'}
```
</p></details>

Content:
<details><summary></summary><p>
            
```

["c", "go", "java", "python", "ruby"]

```
</p></details>



## Request: GET http://demo.scanapi.dev/api/devs/

HEADERS:
<details><summary></summary><p>
            
```
{'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '2', 'Content-Type': 'application/json'}
```
</p></details>

### Response: 200 

Is redirect? False

HEADERS:
<details><summary></summary><p>
            
```
{'Date': 'Sat, 14 Dec 2019 12:19:26 GMT', 'Content-Type': 'application/json', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Set-Cookie': '__cfduid=d0760e69bd3c5961eea9f3bbb1ca8504a1576325966; expires=Mon, 13-Jan-20 12:19:26 GMT; path=/; domain=.scanapi.dev; HttpOnly', 'X-Frame-Options': 'DENY', 'X-Content-Type-Options': 'nosniff', 'Via': '1.1 vegur', 'CF-Cache-Status': 'DYNAMIC', 'Server': 'cloudflare', 'CF-RAY': '54502048bb424b61-GRU', 'Content-Encoding': 'gzip'}
```
</p></details>

Content:
<details><summary></summary><p>
            
```

[{"uuid": "68af402f-1084-40a4-b9b2-6bb5c2d11559", "name": "Anna", "yearsOfExperience": 5, "languages": ["python", "c"], "newOpportunities": true}, {"uuid": "0d1bd106-c585-4d6b-b3a4-d72dedf7190e", "name": "Louis", "yearsOfExperience": 3, "languages": ["java"], "newOpportunities": true}, {"uuid": "129e8cb2-d19c-41ad-9921-cea329bed7f0", "name": "Marcus", "yearsOfExperience": 4, "languages": ["c"], "newOpportunities": false}]

```
</p></details>



## Request: GET http://demo.scanapi.dev/api/devs/?newOpportunities=True

HEADERS:
<details><summary></summary><p>
            
```
{'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '2', 'Content-Type': 'application/json'}
```
</p></details>

### Response: 200 

Is redirect? False

HEADERS:
<details><summary></summary><p>
            
```
{'Date': 'Sat, 14 Dec 2019 12:19:26 GMT', 'Content-Type': 'application/json', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Set-Cookie': '__cfduid=d73d2577d3ad7d4aa2f2e2e6c5bed40ea1576325966; expires=Mon, 13-Jan-20 12:19:26 GMT; path=/; domain=.scanapi.dev; HttpOnly', 'X-Frame-Options': 'DENY', 'X-Content-Type-Options': 'nosniff', 'Via': '1.1 vegur', 'CF-Cache-Status': 'DYNAMIC', 'Server': 'cloudflare', 'CF-RAY': '5450204b691ff5e7-GRU', 'Content-Encoding': 'gzip'}
```
</p></details>

Content:
<details><summary></summary><p>
            
```

[{"uuid": "68af402f-1084-40a4-b9b2-6bb5c2d11559", "name": "Anna", "yearsOfExperience": 5, "languages": ["python", "c"], "newOpportunities": true}, {"uuid": "0d1bd106-c585-4d6b-b3a4-d72dedf7190e", "name": "Louis", "yearsOfExperience": 3, "languages": ["java"], "newOpportunities": true}]

```
</p></details>



## Request: GET http://demo.scanapi.dev/api/devs/?newOpportunities=False

HEADERS:
<details><summary></summary><p>
            
```
{'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '2', 'Content-Type': 'application/json'}
```
</p></details>

### Response: 200 

Is redirect? False

HEADERS:
<details><summary></summary><p>
            
```
{'Date': 'Sat, 14 Dec 2019 12:19:27 GMT', 'Content-Type': 'application/json', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Set-Cookie': '__cfduid=d74bea60a49246f52228b3f89494bb9d41576325966; expires=Mon, 13-Jan-20 12:19:26 GMT; path=/; domain=.scanapi.dev; HttpOnly', 'X-Frame-Options': 'DENY', 'X-Content-Type-Options': 'nosniff', 'Via': '1.1 vegur', 'CF-Cache-Status': 'DYNAMIC', 'Server': 'cloudflare', 'CF-RAY': '5450204dabe5f3d3-GRU', 'Content-Encoding': 'gzip'}
```
</p></details>

Content:
<details><summary></summary><p>
            
```

[{"uuid": "129e8cb2-d19c-41ad-9921-cea329bed7f0", "name": "Marcus", "yearsOfExperience": 4, "languages": ["c"], "newOpportunities": false}]

```
</p></details>



## Request: POST http://demo.scanapi.dev/api/devs/

HEADERS:
<details><summary></summary><p>
            
```
{'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'x-api-key': 'demoKEY123', 'Content-Length': '138', 'Content-Type': 'application/json'}
```
</p></details>

### Response: 201 

Is redirect? False

HEADERS:
<details><summary></summary><p>
            
```
{'Date': 'Sat, 14 Dec 2019 12:19:27 GMT', 'Content-Type': 'application/json', 'Content-Length': '138', 'Connection': 'keep-alive', 'Set-Cookie': '__cfduid=d33b380746b3852ba71f284505108ca221576325967; expires=Mon, 13-Jan-20 12:19:27 GMT; path=/; domain=.scanapi.dev; HttpOnly', 'X-Frame-Options': 'DENY', 'X-Content-Type-Options': 'nosniff', 'Via': '1.1 vegur', 'CF-Cache-Status': 'DYNAMIC', 'Server': 'cloudflare', 'CF-RAY': '5450204fe8a7f6f8-GRU'}
```
</p></details>

Content:
<details><summary></summary><p>
            
```

{"uuid": "b8f3d23e69ec444c9d33d3be5ac12d2f", "name": "Tarik", "yearsOfExperience": 2, "languages": ["ruby go"], "newOpportunities": false}

```
</p></details>



## Request: GET http://demo.scanapi.dev/api/devs/129e8cb2-d19c-51ad-9921-cea329bed7fa

HEADERS:
<details><summary></summary><p>
            
```
{'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '2', 'Content-Type': 'application/json'}
```
</p></details>

### Response: 404 

Is redirect? False

HEADERS:
<details><summary></summary><p>
            
```
{'Date': 'Sat, 14 Dec 2019 12:19:28 GMT', 'Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Set-Cookie': '__cfduid=dfd788d9969c38d42633c08d56982623e1576325967; expires=Mon, 13-Jan-20 12:19:27 GMT; path=/; domain=.scanapi.dev; HttpOnly', 'X-Frame-Options': 'DENY', 'X-Content-Type-Options': 'nosniff', 'Via': '1.1 vegur', 'CF-Cache-Status': 'DYNAMIC', 'Server': 'cloudflare', 'CF-RAY': '545020527a58f728-GRU', 'Content-Encoding': 'gzip'}
```
</p></details>

Content:
<details><summary></summary><p>
            
```

uuid 129e8cb2-d19c-51ad-9921-cea329bed7fa not found

```
</p></details>



## Request: GET http://demo.scanapi.dev/api/devs/129e8cb2-d19c-41ad-9921-cea329bed7f0

HEADERS:
<details><summary></summary><p>
            
```
{'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '2', 'Content-Type': 'application/json'}
```
</p></details>

### Response: 200 

Is redirect? False

HEADERS:
<details><summary></summary><p>
            
```
{'Date': 'Sat, 14 Dec 2019 12:19:28 GMT', 'Content-Type': 'application/json', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Set-Cookie': '__cfduid=d9a640acad93528f9f33175ce307ae7901576325968; expires=Mon, 13-Jan-20 12:19:28 GMT; path=/; domain=.scanapi.dev; HttpOnly', 'X-Frame-Options': 'DENY', 'X-Content-Type-Options': 'nosniff', 'Via': '1.1 vegur', 'CF-Cache-Status': 'DYNAMIC', 'Server': 'cloudflare', 'CF-RAY': '545020550d7bf60b-GRU', 'Content-Encoding': 'gzip'}
```
</p></details>

Content:
<details><summary></summary><p>
            
```

{"uuid": "129e8cb2-d19c-41ad-9921-cea329bed7f0", "name": "Marcus", "yearsOfExperience": 4, "languages": ["c"], "newOpportunities": false}

```
</p></details>



## Request: DELETE http://demo.scanapi.dev/api/devs/129e8cb2-d19c-41ad-9921-cea329bed7f0

HEADERS:
<details><summary></summary><p>
            
```
{'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'x-api-key': 'demoKEY123', 'Content-Length': '2', 'Content-Type': 'application/json'}
```
</p></details>

### Response: 200 

Is redirect? False

HEADERS:
<details><summary></summary><p>
            
```
{'Date': 'Sat, 14 Dec 2019 12:19:28 GMT', 'Content-Type': 'application/json', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Set-Cookie': '__cfduid=d4039b770d53764c72b9d3f5cccd57ef31576325968; expires=Mon, 13-Jan-20 12:19:28 GMT; path=/; domain=.scanapi.dev; HttpOnly', 'X-Frame-Options': 'DENY', 'X-Content-Type-Options': 'nosniff', 'Via': '1.1 vegur', 'CF-Cache-Status': 'DYNAMIC', 'Server': 'cloudflare', 'CF-RAY': '545020584f15f6e8-GRU', 'Content-Encoding': 'gzip'}
```
</p></details>

Content:
<details><summary></summary><p>
            
```

{"deleted": "129e8cb2-d19c-41ad-9921-cea329bed7f0"}

```
</p></details>



## Request: GET http://demo.scanapi.dev/api/devs/129e8cb2-d19c-41ad-9921-cea329bed7f0/languages

HEADERS:
<details><summary></summary><p>
            
```
{'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '2', 'Content-Type': 'application/json'}
```
</p></details>

### Response: 200 

Is redirect? False

HEADERS:
<details><summary></summary><p>
            
```
{'Date': 'Sat, 14 Dec 2019 12:19:29 GMT', 'Content-Type': 'application/json', 'Content-Length': '5', 'Connection': 'keep-alive', 'Set-Cookie': '__cfduid=d6a48c6a7410bff333fa6a51ae019db351576325969; expires=Mon, 13-Jan-20 12:19:29 GMT; path=/; domain=.scanapi.dev; HttpOnly', 'X-Frame-Options': 'DENY', 'X-Content-Type-Options': 'nosniff', 'Via': '1.1 vegur', 'CF-Cache-Status': 'DYNAMIC', 'Server': 'cloudflare', 'CF-RAY': '5450205a795bf6cb-GRU'}
```
</p></details>

Content:
<details><summary></summary><p>
            
```

["c"]

```
</p></details>

