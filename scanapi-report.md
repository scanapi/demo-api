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
| response time | 0.478903 s |
| status code   | 200               |
| redirect      | False               |

#### Headers


| Header    | Value       |
|-----------|-------------|
| Date | Thu, 07 May 2020 23:05:09 GMT |
| Content-Type | text/html; charset=utf-8 |
| Transfer-Encoding | chunked |
| Connection | keep-alive |
| Set-Cookie | __cfduid=d900ff0f16ea1a20b0bc72268a366230f1588892709; expires=Sat, 06-Jun-20 23:05:09 GMT; path=/; domain=.scanapi.dev; HttpOnly; SameSite=Lax |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Via | 1.1 vegur |
| CF-Cache-Status | DYNAMIC |
| Server | cloudflare |
| CF-RAY | 58fe9589e97ff1f2-GRU |
| Content-Encoding | gzip |
| cf-request-id | 0292fbca2f0000f1f250b9a200000001 |



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
| response time | 0.411249 s |
| status code   | 200               |
| redirect      | False               |

#### Headers


| Header    | Value       |
|-----------|-------------|
| Date | Thu, 07 May 2020 23:05:10 GMT |
| Content-Type | application/json |
| Content-Length | 37 |
| Connection | keep-alive |
| Set-Cookie | __cfduid=d183782910f54d910b2c8f3c7dbda3e381588892709; expires=Sat, 06-Jun-20 23:05:09 GMT; path=/; domain=.scanapi.dev; HttpOnly; SameSite=Lax |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Via | 1.1 vegur |
| CF-Cache-Status | DYNAMIC |
| Server | cloudflare |
| CF-RAY | 58fe958cefa5f637-GRU |
| cf-request-id | 0292fbcc150000f637ed38c200000001 |



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
| response time | 0.475719 s |
| status code   | 200               |
| redirect      | False               |

#### Headers


| Header    | Value       |
|-----------|-------------|
| Date | Thu, 07 May 2020 23:05:10 GMT |
| Content-Type | application/json |
| Transfer-Encoding | chunked |
| Connection | keep-alive |
| Set-Cookie | __cfduid=d021ac938a98fb88a18379df36ecdb9471588892710; expires=Sat, 06-Jun-20 23:05:10 GMT; path=/; domain=.scanapi.dev; HttpOnly; SameSite=Lax |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Via | 1.1 vegur |
| CF-Cache-Status | DYNAMIC |
| Server | cloudflare |
| CF-RAY | 58fe958f8dfaeeae-GRU |
| Content-Encoding | gzip |
| cf-request-id | 0292fbcdb70000eeae1f3bf200000001 |



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
| response time | 0.390889 s |
| status code   | 200               |
| redirect      | False               |

#### Headers


| Header    | Value       |
|-----------|-------------|
| Date | Thu, 07 May 2020 23:05:11 GMT |
| Content-Type | application/json |
| Transfer-Encoding | chunked |
| Connection | keep-alive |
| Set-Cookie | __cfduid=d35ec739a9387e872e564190a635bfdc41588892710; expires=Sat, 06-Jun-20 23:05:10 GMT; path=/; domain=.scanapi.dev; HttpOnly; SameSite=Lax |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Via | 1.1 vegur |
| CF-Cache-Status | DYNAMIC |
| Server | cloudflare |
| CF-RAY | 58fe95929e1ff64f-GRU |
| Content-Encoding | gzip |
| cf-request-id | 0292fbcfa30000f64f49b34200000001 |



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
| response time | 0.407604 s |
| status code   | 200               |
| redirect      | False               |

#### Headers


| Header    | Value       |
|-----------|-------------|
| Date | Thu, 07 May 2020 23:05:11 GMT |
| Content-Type | application/json |
| Transfer-Encoding | chunked |
| Connection | keep-alive |
| Set-Cookie | __cfduid=deb7df0a9a84c3957139d5186e42c4d381588892711; expires=Sat, 06-Jun-20 23:05:11 GMT; path=/; domain=.scanapi.dev; HttpOnly; SameSite=Lax |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Via | 1.1 vegur |
| CF-Cache-Status | DYNAMIC |
| Server | cloudflare |
| CF-RAY | 58fe95950c0df6f0-GRU |
| Content-Encoding | gzip |
| cf-request-id | 0292fbd1290000f6f0c0a28200000001 |



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
| x-api-key | demoKEY123 |
| Content-Length | 138 |
| Content-Type | application/json |





#### Body
<details><summary></summary><p>

```json
b'{"uuid": "64afd412cbb94def9eee26684aa9e534", "name": "Tarik", "yearsOfExperience": 2, "languages": ["ruby go"], "newOpportunities": false}'
```



</p></details>

#### cURL

<details><summary></summary><p>

```
curl -X POST -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 138' -H 'Content-Type: application/json' -H 'User-Agent: python-requests/2.23.0' -H 'x-api-key: demoKEY123' -d '{"uuid": "64afd412cbb94def9eee26684aa9e534", "name": "Tarik", "yearsOfExperience": 2, "languages": ["ruby go"], "newOpportunities": false}' http://demo.scanapi.dev/api/devs/
```

</p></details>

### Response

#### Metadata

|               |                                          |
|---------------|------------------------------------------|
| response time | 0.4058 s |
| status code   | 201               |
| redirect      | False               |

#### Headers


| Header    | Value       |
|-----------|-------------|
| Date | Thu, 07 May 2020 23:05:11 GMT |
| Content-Type | application/json |
| Content-Length | 138 |
| Connection | keep-alive |
| Set-Cookie | __cfduid=dada61f9a3acadf4fc28d9a9e40af61281588892711; expires=Sat, 06-Jun-20 23:05:11 GMT; path=/; domain=.scanapi.dev; HttpOnly; SameSite=Lax |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Via | 1.1 vegur |
| CF-Cache-Status | DYNAMIC |
| Server | cloudflare |
| CF-RAY | 58fe9597ad87f6ab-GRU |
| cf-request-id | 0292fbd2c90000f6abf52e3200000001 |



#### Content
<details><summary></summary><p>


```
{"uuid": "64afd412cbb94def9eee26684aa9e534", "name": "Tarik", "yearsOfExperience": 2, "languages": ["ruby go"], "newOpportunities": false}
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
| response time | 0.503335 s |
| status code   | 404               |
| redirect      | False               |

#### Headers


| Header    | Value       |
|-----------|-------------|
| Date | Thu, 07 May 2020 23:05:12 GMT |
| Content-Type | text/html; charset=utf-8 |
| Transfer-Encoding | chunked |
| Connection | keep-alive |
| Set-Cookie | __cfduid=d967eb26281cd915dccafe1e16ce273801588892712; expires=Sat, 06-Jun-20 23:05:12 GMT; path=/; domain=.scanapi.dev; HttpOnly; SameSite=Lax |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Via | 1.1 vegur |
| CF-Cache-Status | DYNAMIC |
| Server | cloudflare |
| CF-RAY | 58fe959a38f0f677-GRU |
| Content-Encoding | gzip |
| cf-request-id | 0292fbd4640000f677130a0200000001 |



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
| response time | 0.507458 s |
| status code   | 200               |
| redirect      | False               |

#### Headers


| Header    | Value       |
|-----------|-------------|
| Date | Thu, 07 May 2020 23:05:12 GMT |
| Content-Type | application/json |
| Transfer-Encoding | chunked |
| Connection | keep-alive |
| Set-Cookie | __cfduid=d5368016359271144b8f4a7ff265e1c341588892712; expires=Sat, 06-Jun-20 23:05:12 GMT; path=/; domain=.scanapi.dev; HttpOnly; SameSite=Lax |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Via | 1.1 vegur |
| CF-Cache-Status | DYNAMIC |
| Server | cloudflare |
| CF-RAY | 58fe959d6b8fd00c-GRU |
| Content-Encoding | gzip |
| cf-request-id | 0292fbd6620000d00c83b0e200000001 |



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
| x-api-key | demoKEY123 |
| Content-Length | 2 |
| Content-Type | application/json |





</p></details>

#### cURL

<details><summary></summary><p>

```
curl -X DELETE -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 2' -H 'Content-Type: application/json' -H 'User-Agent: python-requests/2.23.0' -H 'x-api-key: demoKEY123' -d '{}' http://demo.scanapi.dev/api/devs/129e8cb2-d19c-41ad-9921-cea329bed7f0
```

</p></details>

### Response

#### Metadata

|               |                                          |
|---------------|------------------------------------------|
| response time | 0.500896 s |
| status code   | 200               |
| redirect      | False               |

#### Headers


| Header    | Value       |
|-----------|-------------|
| Date | Thu, 07 May 2020 23:05:13 GMT |
| Content-Type | application/json |
| Transfer-Encoding | chunked |
| Connection | keep-alive |
| Set-Cookie | __cfduid=dfed80a2adb13eed7d6b0d80f2d32ebba1588892713; expires=Sat, 06-Jun-20 23:05:13 GMT; path=/; domain=.scanapi.dev; HttpOnly; SameSite=Lax |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Via | 1.1 vegur |
| CF-Cache-Status | DYNAMIC |
| Server | cloudflare |
| CF-RAY | 58fe95a0ac28f1f6-GRU |
| Content-Encoding | gzip |
| cf-request-id | 0292fbd86c0000f1f667ac8200000001 |



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
| response time | 0.507751 s |
| status code   | 200               |
| redirect      | False               |

#### Headers


| Header    | Value       |
|-----------|-------------|
| Date | Thu, 07 May 2020 23:05:13 GMT |
| Content-Type | application/json |
| Content-Length | 5 |
| Connection | keep-alive |
| Set-Cookie | __cfduid=d221aefc4ece1ad149dfc63c35e2c15161588892713; expires=Sat, 06-Jun-20 23:05:13 GMT; path=/; domain=.scanapi.dev; HttpOnly; SameSite=Lax |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Via | 1.1 vegur |
| CF-Cache-Status | DYNAMIC |
| Server | cloudflare |
| CF-RAY | 58fe95a3cd47f6f0-GRU |
| cf-request-id | 0292fbda5f0000f6f0b2b3d200000001 |



#### Content
<details><summary></summary><p>


```
["c"]
```


</p></details>

