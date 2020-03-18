# ScanAPI Report



## GET `/api/health/`

### Request

Full URL: http://demo.scanapi.dev/api/health/

#### Headers


| Header    | Value       |
|-----------|-------------|
| User-Agent | python-requests/2.23.0 |
| Accept-Encoding | gzip, deflate |
| Accept | */* |
| Connection | keep-alive |
| Content-Length | 2 |
| Content-Type | application/json |





</p></details>

#### cURL

<details><summary></summary><p>

```
curl -X GET -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 2' -H 'Content-Type: application/json' -H 'User-Agent: python-requests/2.23.0' -d '{}' http://demo.scanapi.dev/api/health/
```

</p></details>

### Response

#### Metadata

|               |                                          |
|---------------|------------------------------------------|
| response time | 0.512668 s |
| status code   | 200               |
| redirect      | False               |

#### Headers


| Header    | Value       |
|-----------|-------------|
| Date | Wed, 22 Apr 2020 22:42:01 GMT |
| Content-Type | text/html; charset=utf-8 |
| Transfer-Encoding | chunked |
| Connection | keep-alive |
| Set-Cookie | __cfduid=d77207030bb22c389870a02e159ce03301587595321; expires=Fri, 22-May-20 22:42:01 GMT; path=/; domain=.scanapi.dev; HttpOnly; SameSite=Lax |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Via | 1.1 vegur |
| CF-Cache-Status | DYNAMIC |
| Server | cloudflare |
| CF-RAY | 5882db062cc4f774-GRU |
| Content-Encoding | gzip |
| cf-request-id | 0245a737d40000f774f42b0200000001 |



#### Content
<details><summary></summary><p>


```
OK!
```


</p></details>



## GET `/api/languages/`

### Request

Full URL: http://demo.scanapi.dev/api/languages/

#### Headers


| Header    | Value       |
|-----------|-------------|
| User-Agent | python-requests/2.23.0 |
| Accept-Encoding | gzip, deflate |
| Accept | */* |
| Connection | keep-alive |
| Content-Length | 2 |
| Content-Type | application/json |





</p></details>

#### cURL

<details><summary></summary><p>

```
curl -X GET -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 2' -H 'Content-Type: application/json' -H 'User-Agent: python-requests/2.23.0' -d '{}' http://demo.scanapi.dev/api/languages/
```

</p></details>

### Response

#### Metadata

|               |                                          |
|---------------|------------------------------------------|
| response time | 0.403967 s |
| status code   | 200               |
| redirect      | False               |

#### Headers


| Header    | Value       |
|-----------|-------------|
| Date | Wed, 22 Apr 2020 22:42:02 GMT |
| Content-Type | application/json |
| Content-Length | 37 |
| Connection | keep-alive |
| Set-Cookie | __cfduid=de1f3b9aaa9f57a63a098be20d922194d1587595321; expires=Fri, 22-May-20 22:42:01 GMT; path=/; domain=.scanapi.dev; HttpOnly; SameSite=Lax |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Via | 1.1 vegur |
| CF-Cache-Status | DYNAMIC |
| Server | cloudflare |
| CF-RAY | 5882db092e87f75c-GRU |
| cf-request-id | 0245a739b80000f75c0e254200000001 |



#### Content
<details><summary></summary><p>


```
["c", "go", "java", "python", "ruby"]
```


</p></details>



## GET `/api/devs/`

### Request

Full URL: http://demo.scanapi.dev/api/devs/

#### Headers


| Header    | Value       |
|-----------|-------------|
| User-Agent | python-requests/2.23.0 |
| Accept-Encoding | gzip, deflate |
| Accept | */* |
| Connection | keep-alive |
| Content-Length | 2 |
| Content-Type | application/json |





</p></details>

#### cURL

<details><summary></summary><p>

```
curl -X GET -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 2' -H 'Content-Type: application/json' -H 'User-Agent: python-requests/2.23.0' -d '{}' http://demo.scanapi.dev/api/devs/
```

</p></details>

### Response

#### Metadata

|               |                                          |
|---------------|------------------------------------------|
| response time | 0.499885 s |
| status code   | 200               |
| redirect      | False               |

#### Headers


| Header    | Value       |
|-----------|-------------|
| Date | Wed, 22 Apr 2020 22:42:02 GMT |
| Content-Type | application/json |
| Transfer-Encoding | chunked |
| Connection | keep-alive |
| Set-Cookie | __cfduid=d44b22341a0c3b81307eef0a22e154d0f1587595322; expires=Fri, 22-May-20 22:42:02 GMT; path=/; domain=.scanapi.dev; HttpOnly; SameSite=Lax |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Via | 1.1 vegur |
| CF-Cache-Status | DYNAMIC |
| Server | cloudflare |
| CF-RAY | 5882db0bfe8df724-GRU |
| Content-Encoding | gzip |
| cf-request-id | 0245a73b7a0000f72426bda200000001 |



#### Content
<details><summary></summary><p>


```
[{"uuid": "68af402f-1084-40a4-b9b2-6bb5c2d11559", "name": "Anna", "yearsOfExperience": 5, "languages": ["python", "c"], "newOpportunities": true}, {"uuid": "0d1bd106-c585-4d6b-b3a4-d72dedf7190e", "name": "Louis", "yearsOfExperience": 3, "languages": ["java"], "newOpportunities": true}, {"uuid": "129e8cb2-d19c-41ad-9921-cea329bed7f0", "name": "Marcus", "yearsOfExperience": 4, "languages": ["c"], "newOpportunities": false}]
```


</p></details>



## GET `/api/devs/?newOpportunities=True`

### Request

Full URL: http://demo.scanapi.dev/api/devs/?newOpportunities=True

#### Headers


| Header    | Value       |
|-----------|-------------|
| User-Agent | python-requests/2.23.0 |
| Accept-Encoding | gzip, deflate |
| Accept | */* |
| Connection | keep-alive |
| Content-Length | 2 |
| Content-Type | application/json |





</p></details>

#### cURL

<details><summary></summary><p>

```
curl -X GET -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 2' -H 'Content-Type: application/json' -H 'User-Agent: python-requests/2.23.0' -d '{}' 'http://demo.scanapi.dev/api/devs/?newOpportunities=True'
```

</p></details>

### Response

#### Metadata

|               |                                          |
|---------------|------------------------------------------|
| response time | 0.407878 s |
| status code   | 200               |
| redirect      | False               |

#### Headers


| Header    | Value       |
|-----------|-------------|
| Date | Wed, 22 Apr 2020 22:42:03 GMT |
| Content-Type | application/json |
| Transfer-Encoding | chunked |
| Connection | keep-alive |
| Set-Cookie | __cfduid=d206167e1913f36b2454e5afd99c343bf1587595322; expires=Fri, 22-May-20 22:42:02 GMT; path=/; domain=.scanapi.dev; HttpOnly; SameSite=Lax |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Via | 1.1 vegur |
| CF-Cache-Status | DYNAMIC |
| Server | cloudflare |
| CF-RAY | 5882db0eecbfcfe8-GRU |
| Content-Encoding | gzip |
| cf-request-id | 0245a73d500000cfe8a1339200000001 |



#### Content
<details><summary></summary><p>


```
[{"uuid": "68af402f-1084-40a4-b9b2-6bb5c2d11559", "name": "Anna", "yearsOfExperience": 5, "languages": ["python", "c"], "newOpportunities": true}, {"uuid": "0d1bd106-c585-4d6b-b3a4-d72dedf7190e", "name": "Louis", "yearsOfExperience": 3, "languages": ["java"], "newOpportunities": true}]
```


</p></details>



## GET `/api/devs/?newOpportunities=False`

### Request

Full URL: http://demo.scanapi.dev/api/devs/?newOpportunities=False

#### Headers


| Header    | Value       |
|-----------|-------------|
| User-Agent | python-requests/2.23.0 |
| Accept-Encoding | gzip, deflate |
| Accept | */* |
| Connection | keep-alive |
| Content-Length | 2 |
| Content-Type | application/json |





</p></details>

#### cURL

<details><summary></summary><p>

```
curl -X GET -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 2' -H 'Content-Type: application/json' -H 'User-Agent: python-requests/2.23.0' -d '{}' 'http://demo.scanapi.dev/api/devs/?newOpportunities=False'
```

</p></details>

### Response

#### Metadata

|               |                                          |
|---------------|------------------------------------------|
| response time | 0.3958 s |
| status code   | 200               |
| redirect      | False               |

#### Headers


| Header    | Value       |
|-----------|-------------|
| Date | Wed, 22 Apr 2020 22:42:03 GMT |
| Content-Type | application/json |
| Transfer-Encoding | chunked |
| Connection | keep-alive |
| Set-Cookie | __cfduid=d920d625bdfa704eaff65a8ee1c561dda1587595323; expires=Fri, 22-May-20 22:42:03 GMT; path=/; domain=.scanapi.dev; HttpOnly; SameSite=Lax |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Via | 1.1 vegur |
| CF-Cache-Status | DYNAMIC |
| Server | cloudflare |
| CF-RAY | 5882db118f41f764-GRU |
| Content-Encoding | gzip |
| cf-request-id | 0245a73ef60000f7646822e200000001 |



#### Content
<details><summary></summary><p>


```
[{"uuid": "129e8cb2-d19c-41ad-9921-cea329bed7f0", "name": "Marcus", "yearsOfExperience": 4, "languages": ["c"], "newOpportunities": false}]
```


</p></details>



## POST `/api/devs/`

### Request

Full URL: http://demo.scanapi.dev/api/devs/

#### Headers


| Header    | Value       |
|-----------|-------------|
| User-Agent | python-requests/2.23.0 |
| Accept-Encoding | gzip, deflate |
| Accept | */* |
| Connection | keep-alive |
| x-api-key | <sensitive_information> |
| Content-Length | 138 |
| Content-Type | application/json |





#### Body
<details><summary></summary><p>

```json
b'{"uuid": "b3ba74e55a2043178841e62523b0a146", "name": "Tarik", "yearsOfExperience": 2, "languages": ["ruby go"], "newOpportunities": false}'
```



</p></details>

#### cURL

<details><summary></summary><p>

```
curl -X POST -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 138' -H 'Content-Type: application/json' -H 'User-Agent: python-requests/2.23.0' -H 'x-api-key: <sensitive_information>' -d '{"uuid": "b3ba74e55a2043178841e62523b0a146", "name": "Tarik", "yearsOfExperience": 2, "languages": ["ruby go"], "newOpportunities": false}' http://demo.scanapi.dev/api/devs/
```

</p></details>

### Response

#### Metadata

|               |                                          |
|---------------|------------------------------------------|
| response time | 0.508169 s |
| status code   | 201               |
| redirect      | False               |

#### Headers


| Header    | Value       |
|-----------|-------------|
| Date | Wed, 22 Apr 2020 22:42:03 GMT |
| Content-Type | application/json |
| Content-Length | 138 |
| Connection | keep-alive |
| Set-Cookie | __cfduid=d0d8d798c7832b26ecc9a7dff0530e4af1587595323; expires=Fri, 22-May-20 22:42:03 GMT; path=/; domain=.scanapi.dev; HttpOnly; SameSite=Lax |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Via | 1.1 vegur |
| CF-Cache-Status | DYNAMIC |
| Server | cloudflare |
| CF-RAY | 5882db140cc1f3db-GRU |
| cf-request-id | 0245a740850000f3db20932200000001 |



#### Content
<details><summary></summary><p>


```
{"uuid": "b3ba74e55a2043178841e62523b0a146", "name": "Tarik", "yearsOfExperience": 2, "languages": ["ruby go"], "newOpportunities": false}
```


</p></details>



## GET `/api/devs/129e8cb2-d19c-51ad-9921-cea329bed7fa`

### Request

Full URL: http://demo.scanapi.dev/api/devs/129e8cb2-d19c-51ad-9921-cea329bed7fa

#### Headers


| Header    | Value       |
|-----------|-------------|
| User-Agent | python-requests/2.23.0 |
| Accept-Encoding | gzip, deflate |
| Accept | */* |
| Connection | keep-alive |
| Content-Length | 2 |
| Content-Type | application/json |





</p></details>

#### cURL

<details><summary></summary><p>

```
curl -X GET -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 2' -H 'Content-Type: application/json' -H 'User-Agent: python-requests/2.23.0' -d '{}' http://demo.scanapi.dev/api/devs/129e8cb2-d19c-51ad-9921-cea329bed7fa
```

</p></details>

### Response

#### Metadata

|               |                                          |
|---------------|------------------------------------------|
| response time | 0.404905 s |
| status code   | 404               |
| redirect      | False               |

#### Headers


| Header    | Value       |
|-----------|-------------|
| Date | Wed, 22 Apr 2020 22:42:04 GMT |
| Content-Type | text/html; charset=utf-8 |
| Transfer-Encoding | chunked |
| Connection | keep-alive |
| Set-Cookie | __cfduid=db9e6908f55e7239eede81d58e325ea221587595324; expires=Fri, 22-May-20 22:42:04 GMT; path=/; domain=.scanapi.dev; HttpOnly; SameSite=Lax |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Via | 1.1 vegur |
| CF-Cache-Status | DYNAMIC |
| Server | cloudflare |
| CF-RAY | 5882db173b90f770-GRU |
| Content-Encoding | gzip |
| cf-request-id | 0245a742830000f77097bbe200000001 |



#### Content
<details><summary></summary><p>


```
uuid 129e8cb2-d19c-51ad-9921-cea329bed7fa not found
```


</p></details>



## GET `/api/devs/129e8cb2-d19c-41ad-9921-cea329bed7f0`

### Request

Full URL: http://demo.scanapi.dev/api/devs/129e8cb2-d19c-41ad-9921-cea329bed7f0

#### Headers


| Header    | Value       |
|-----------|-------------|
| User-Agent | python-requests/2.23.0 |
| Accept-Encoding | gzip, deflate |
| Accept | */* |
| Connection | keep-alive |
| Content-Length | 2 |
| Content-Type | application/json |





</p></details>

#### cURL

<details><summary></summary><p>

```
curl -X GET -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 2' -H 'Content-Type: application/json' -H 'User-Agent: python-requests/2.23.0' -d '{}' http://demo.scanapi.dev/api/devs/129e8cb2-d19c-41ad-9921-cea329bed7f0
```

</p></details>

### Response

#### Metadata

|               |                                          |
|---------------|------------------------------------------|
| response time | 0.397922 s |
| status code   | 200               |
| redirect      | False               |

#### Headers


| Header    | Value       |
|-----------|-------------|
| Date | Wed, 22 Apr 2020 22:42:04 GMT |
| Content-Type | application/json |
| Transfer-Encoding | chunked |
| Connection | keep-alive |
| Set-Cookie | __cfduid=d100556c8900acb0b5e1b69858394ef2f1587595324; expires=Fri, 22-May-20 22:42:04 GMT; path=/; domain=.scanapi.dev; HttpOnly; SameSite=Lax |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Via | 1.1 vegur |
| CF-Cache-Status | DYNAMIC |
| Server | cloudflare |
| CF-RAY | 5882db19df90f65f-GRU |
| Content-Encoding | gzip |
| cf-request-id | 0245a744290000f65f52ba6200000001 |



#### Content
<details><summary></summary><p>


```
{"uuid": "129e8cb2-d19c-41ad-9921-cea329bed7f0", "name": "Marcus", "yearsOfExperience": 4, "languages": ["c"], "newOpportunities": false}
```


</p></details>



## DELETE `/api/devs/129e8cb2-d19c-41ad-9921-cea329bed7f0`

### Request

Full URL: http://demo.scanapi.dev/api/devs/129e8cb2-d19c-41ad-9921-cea329bed7f0

#### Headers


| Header    | Value       |
|-----------|-------------|
| User-Agent | python-requests/2.23.0 |
| Accept-Encoding | gzip, deflate |
| Accept | */* |
| Connection | keep-alive |
| x-api-key | <sensitive_information> |
| Content-Length | 2 |
| Content-Type | application/json |





</p></details>

#### cURL

<details><summary></summary><p>

```
curl -X DELETE -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 2' -H 'Content-Type: application/json' -H 'User-Agent: python-requests/2.23.0' -H 'x-api-key: <sensitive_information>' -d '{}' http://demo.scanapi.dev/api/devs/129e8cb2-d19c-41ad-9921-cea329bed7f0
```

</p></details>

### Response

#### Metadata

|               |                                          |
|---------------|------------------------------------------|
| response time | 0.405831 s |
| status code   | 200               |
| redirect      | False               |

#### Headers


| Header    | Value       |
|-----------|-------------|
| Date | Wed, 22 Apr 2020 22:42:05 GMT |
| Content-Type | application/json |
| Transfer-Encoding | chunked |
| Connection | keep-alive |
| Set-Cookie | __cfduid=d6749f4cd0ab345b361ce40b04c5cb4f01587595324; expires=Fri, 22-May-20 22:42:04 GMT; path=/; domain=.scanapi.dev; HttpOnly; SameSite=Lax |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Via | 1.1 vegur |
| CF-Cache-Status | DYNAMIC |
| Server | cloudflare |
| CF-RAY | 5882db1c6a30f5fb-GRU |
| Content-Encoding | gzip |
| cf-request-id | 0245a745bd0000f5fbd20df200000001 |



#### Content
<details><summary></summary><p>


```
{"deleted": "129e8cb2-d19c-41ad-9921-cea329bed7f0"}
```


</p></details>



## GET `/api/devs/129e8cb2-d19c-41ad-9921-cea329bed7f0/languages`

### Request

Full URL: http://demo.scanapi.dev/api/devs/129e8cb2-d19c-41ad-9921-cea329bed7f0/languages

#### Headers


| Header    | Value       |
|-----------|-------------|
| User-Agent | python-requests/2.23.0 |
| Accept-Encoding | gzip, deflate |
| Accept | */* |
| Connection | keep-alive |
| Content-Length | 2 |
| Content-Type | application/json |





</p></details>

#### cURL

<details><summary></summary><p>

```
curl -X GET -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 2' -H 'Content-Type: application/json' -H 'User-Agent: python-requests/2.23.0' -d '{}' http://demo.scanapi.dev/api/devs/129e8cb2-d19c-41ad-9921-cea329bed7f0/languages
```

</p></details>

### Response

#### Metadata

|               |                                          |
|---------------|------------------------------------------|
| response time | 0.39922 s |
| status code   | 200               |
| redirect      | False               |

#### Headers


| Header    | Value       |
|-----------|-------------|
| Date | Wed, 22 Apr 2020 22:42:05 GMT |
| Content-Type | application/json |
| Content-Length | 5 |
| Connection | keep-alive |
| Set-Cookie | __cfduid=d5f87ffaeef7bc253495042baead6c1801587595325; expires=Fri, 22-May-20 22:42:05 GMT; path=/; domain=.scanapi.dev; HttpOnly; SameSite=Lax |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Via | 1.1 vegur |
| CF-Cache-Status | DYNAMIC |
| Server | cloudflare |
| CF-RAY | 5882db1f0975f61b-GRU |
| cf-request-id | 0245a747610000f61b5fa90200000001 |



#### Content
<details><summary></summary><p>


```
["c"]
```


</p></details>

