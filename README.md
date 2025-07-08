## API Reference

### Getting Started
This API is available remotely and is hosted by under the following url ..

https://tinizacapstoneprj-ae0dab8adaa4.herokuapp.com/

This API provides endpoints for deleting, registered actors associated movies. Find the endpoints described in the following..

### Endpoints
#### GET /actors
- Required Rights: 'get:actors'

- General: 

The API endpoint returns a list of all registrated actors 

Properties of actors are
 - name
 - age
 - gender
 - a list of movies being involved in

- Sample:

Request: GET https://tinizacapstoneprj-ae0dab8adaa4.herokuapp.com/actors

with Bearer Token

Response:

{
    "actors":[
        {
            "age":29,
            "gender":
            "female",
            "id":2,
            "movies":[
                {
                    "actors":[],
                    "id":2,
                    "release_date":
                    "Mon, 01 Jan 2024 00:00:00 GMT",
                    "title":"The fast and furious"
                },
                {
                    "actors":[],
                    "id":6,
                    "release_date":"Tue, 01 Jan 2002 00:00:00 GMT",
                    "title":"The Lord of the Rings"
                }
            ],
            "name":"Clint Eastwood"
            }
        ]
,"success":true
}


### Endpoints
#### POST /actors
- Required Rights: 'post:actors'

- General: Endpoint for actor registration with properties
            Properties of actors are
             - name
             - age
             - gender
             - a list of movies being involved in

Response:
The Endpoint returns the properties of the posted instance.

- Sample:

Requesting..

POST https://tinizacapstoneprj-ae0dab8adaa4.herokuapp.com/actors

Authorization: Bearer Token

Body: 
{
    "id":-1,
    "gender":"male",
    "age":50,
    "name":"Daniel Craig",
    "movies":[
        {   
            "actors":[
                    {
                        "age":29,
                        "gender":"female",
                        "id":2,"movies":[],
                        "name":"Robert de Niro"
                    }
                ],
            "id":2,
            "release_date":"Mon, 01 Jan 2024 00:00:00 GMT",
            "title":"The fast and furious"
        },{
            "actors":[
                {
                    "age":29,
                    "gender":"female",
                    "id":2,"movies":[],
                    "name":"Robert de Niro"
                },{
                    "age":29,
                    "gender":"female",
                    "id":7,
                    "movies":[],
                    "name":"Clint Eastwood"
                },{
                    "age":95,
                    "gender":"female",
                    "id":6,
                    "movies":[],
                    "name":"Audrey Hepburn"
                }
            ],
            "id":6,
            "release_date":"Tue, 01 Jan 2002 00:00:00 GMT",
            "title":"The Lord of the Rings"
        }
    ]
}

Response:

{
    "actors":[
        {
            "age":29,
            "gender":"female",
            "id":2,
            "movies":[
                {
                    "actors":[],
                    "id":2,
                    "release_date":"Mon, 01 Jan 2024 00:00:00 GMT",
                    "title":"The fast and furious"
                },{
                    "actors":[],
                    "id":6,"release_date":"Tue, 01 Jan 2002 00:00:00 GMT",
                    "title":"The Lord of the Rings"},
                {
                    "actors":[],
                    "id":7,"release_date":"Tue, 01 Jan 2002 00:00:00 GMT",
                    "title":"Star Wars 1"
                }
            ],
            "name":"Robert de Niro"
        },{
            "age":95,
            "gender":"female",
            "id":6,
            "movies":[
                {
                    "actors":[],
                    "id":7,"release_date":"Tue, 01 Jan 2002 00:00:00 GMT",
                    "title":"Star Wars 1"
                },{
                    "actors":[],
                    "id":6,
                    "release_date":"Tue, 01 Jan 2002 00:00:00 GMT",
                    "title":"The Lord of the Rings"#
                }
            ],
            "name":"Audrey Hepburn"
        }
    ],
    "success":true
}


### Endpoints
#### PATCH /actors
- Required Rights: 'patch:actors'

- General: 

Endpoint for modifying the actor properties. Each property can be modified, when listed in the body of the request
    Properties of actors are
     - name
     - age
     - gender
     - a list of movies being involved in

Response:
The Endpoint returns the properties of the patched instance.

- Sample:

PATCH https://tinizacapstoneprj-ae0dab8adaa4.herokuapp.com/actors/[ID of actor]

Authoriation: Bearer Token

Body: 

{"age":29,"gender":"female","id":2,"movies":[{"actors":[{"age":29,"gender":"female","id":2,"movies":[],"name":"Robert de Niro"},{"age":50,"gender":"male","id":101,"movies":[],"name":"Daniel Craig"}],"id":2,"release_date":"Mon, 01 Jan 2024 00:00:00 GMT","title":"The fast and furious"},{"actors":[{"age":29,"gender":"female","id":2,"movies":[],"name":"Robert de Niro"},{"age":29,"gender":"female","id":7,"movies":[],"name":"Clint Eastwood"},{"age":95,"gender":"female","id":6,"movies":[],"name":"Audrey Hepburn"},{"age":50,"gender":"male","id":101,"movies":[],"name":"Daniel Craig"}],"id":6,"release_date":"Tue, 01 Jan 2002 00:00:00 GMT","title":"The Lord of the Rings"}],"name":"Robert de Niro"}

Response:

{"age":29,"gender":"female","id":2,"movies":[{"actors":[{"age":29,"gender":"female","id":2,"movies":[],"name":"Robert de Niro"},{"age":50,"gender":"male","id":101,"movies":[],"name":"Daniel Craig"}],"id":2,"release_date":"Mon, 01 Jan 2024 00:00:00 GMT","title":"The fast and furious"},{"actors":[{"age":29,"gender":"female","id":2,"movies":[],"name":"Robert de Niro"},{"age":29,"gender":"female","id":7,"movies":[],"name":"Clint Eastwood"},{"age":95,"gender":"female","id":6,"movies":[],"name":"Audrey Hepburn"},{"age":50,"gender":"male","id":101,"movies":[],"name":"Daniel Craig"}],"id":6,"release_date":"Tue, 01 Jan 2002 00:00:00 GMT","title":"The Lord of the Rings"}],"name":"Robert de Niro"}

### Endpoints
#### DELETE /actors
- Required Rights: 'delete:actors'

- General: 

Endpoint for deleting registered actors
Parameter:
 - requires the identifier of the actor instance

Response:
The Endpoint returns the ID of the deleted instance.

- Sample:

Request:

DELETE https://tinizacapstoneprj-ae0dab8adaa4.herokuapp.com/actors/[ID of actor]

Authorization: Bearer Token

Response:

{
    "deleted": {
        "age": 95,
        "gender": "male",
        "id": 34,
        "movies": [],
        "name": "Quatsch mit Sosse"
    },
    "success": true
}

### Endpoints
#### GET /movies
- Required Rights: 'get:movies'

- General:  

The API endpoint provides a list of all registrated movies. 
Properties of movies are
 - title
 - release_date
 - list of actors being involved in the cast

- Sample:

Request: GET https://tinizacapstoneprj-ae0dab8adaa4.herokuapp.com/movies

with Bearer Token

Response:

{"movies":[{"actors":[{"age":29,"gender":"female","id":2,"movies":[],"name":"Robert de Niro"},{"age":50,"gender":"male","id":101,"movies":[],"name":"Daniel Craig"}],"id":2,"release_date":"Mon, 01 Jan 2024 00:00:00 GMT","title":"The fast and furious"},{"actors":[{"age":29,"gender":"female","id":2,"movies":[],"name":"Robert de Niro"},{"age":29,"gender":"female","id":7,"movies":[],"name":"Clint Eastwood"},{"age":95,"gender":"female","id":6,"movies":[],"name":"Audrey Hepburn"},{"age":50,"gender":"male","id":101,"movies":[],"name":"Daniel Craig"}],"id":6,"release_date":"Tue, 01 Jan 2002 00:00:00 GMT","title":"The Lord of the Rings"},{"actors":[{"age":29,"gender":"female","id":2,"movies":[],"name":"Robert de Niro"},{"age":29,"gender":"female","id":7,"movies":[],"name":"Clint Eastwood"},{"age":95,"gender":"female","id":6,"movies":[],"name":"Audrey Hepburn"}],"id":7,"release_date":"Tue, 01 Jan 2002 00:00:00 GMT","title":"Star Wars 1"}],"success":true}


### Endpoints
#### POST /movies
- Required Rights: 'post:movies'

- General: 

Endpoint of API registers a new movie with properies..
 - title: title of the movie
 - cast: actors being part of the cast
 - release_date: Date of movie release

Response:
The Endpoint returns the properties of the posted instance.

- Sample:

Post https://tinizacapstoneprj-ae0dab8adaa4.herokuapp.com/movies

Authorization Bearer Token

Body:

{
    "id":-1,
    "title":"Independence Day",
    "release_date":"2025-07-06T22:17:33.427Z",
    "actors":[]
}

Response: 

{"movies":[{"actors":[{"age":50,"gender":"male","id":101,"movies":[],"name":"Daniel Craig"},{"age":29,"gender":"female","id":2,"movies":[],"name":"Robert de Niro"}],"id":2,"release_date":"Mon, 01 Jan 2024 00:00:00 GMT","title":"The fast and furious"},{"actors":[{"age":29,"gender":"female","id":7,"movies":[],"name":"Clint Eastwood"},{"age":95,"gender":"female","id":6,"movies":[],"name":"Audrey Hepburn"},{"age":50,"gender":"male","id":101,"movies":[],"name":"Daniel Craig"},{"age":29,"gender":"female","id":2,"movies":[],"name":"Robert de Niro"}],"id":6,"release_date":"Tue, 01 Jan 2002 00:00:00 GMT","title":"The Lord of the Rings"},{"actors":[{"age":29,"gender":"female","id":7,"movies":[],"name":"Clint Eastwood"},{"age":95,"gender":"female","id":6,"movies":[],"name":"Audrey Hepburn"}],"id":7,"release_date":"Tue, 01 Jan 2002 00:00:00 GMT","title":"Star Wars 1"},{"actors":[],"id":100,"release_date":"Sun, 06 Jul 2025 00:00:00 GMT","title":"Independence Day"}],"success":true}


### Endpoints
#### PATCH /movies
- Required Rights: 'patch:movies'

- General: 

Endpoint for modifying the properties of a movie instance. Each property can be modified, when listed in the body of the request

Properties of actors are
 - title: title of the movie
 - cast: actors being part of the cast
 - release_date: Date of movie release

Response:
The Endpoint returns the new properties of the patched instance.

- Sample:

PATCH https://tinizacapstoneprj-ae0dab8adaa4.herokuapp.com/actors/[ID of movie]

Authoriation: Bearer Token

Body: 

{"actors":[],"id":100,"release_date":"Sun, 06 Jul 2025 00:00:00 GMT","title":"Independence Day"}

Response:

{"movies":[{"actors":[{"age":50,"gender":"male","id":101,"movies":[],"name":"Daniel Craig"},{"age":29,"gender":"female","id":2,"movies":[],"name":"Robert de Niro"}],"id":2,"release_date":"Mon, 01 Jan 2024 00:00:00 GMT","title":"The fast and furious"},{"actors":[{"age":29,"gender":"female","id":7,"movies":[],"name":"Clint Eastwood"},{"age":95,"gender":"female","id":6,"movies":[],"name":"Audrey Hepburn"},{"age":50,"gender":"male","id":101,"movies":[],"name":"Daniel Craig"},{"age":29,"gender":"female","id":2,"movies":[],"name":"Robert de Niro"}],"id":6,"release_date":"Tue, 01 Jan 2002 00:00:00 GMT","title":"The Lord of the Rings"},{"actors":[{"age":29,"gender":"female","id":7,"movies":[],"name":"Clint Eastwood"},{"age":95,"gender":"female","id":6,"movies":[],"name":"Audrey Hepburn"}],"id":7,"release_date":"Tue, 01 Jan 2002 00:00:00 GMT","title":"Star Wars 1"},{"actors":[],"id":100,"release_date":"Sun, 06 Jul 2025 00:00:00 GMT","title":"Independence Day"}],"success":true}


### Endpoints
#### DELETE /movies
- Required Rights: 'delete:movies'

- General:

Endpoint for deleting registered movies

Parameter:
 - requires the identifier of the actor instance

Response:
The Endpoint returns the ID of the deleted instance.

- Sample:

DELETE https://tinizacapstoneprj-ae0dab8adaa4.herokuapp.com/movies/[ID of movie]

Authorization: Bearer Token

Response:

{
    "deleted": {
        "actors": [],
        "id": 40,
        "release_date": "Tue, 01 Jan 2002 00:00:00 GMT",
        "title": "Independence Day 2"
    },
    "success": true
}

### Personal note..

Backend start:

export DATABASE_URL="postgresql://tim:drawer16388@localhost:5432/agency"

python3 app.y


### Testing

Use the content stored in directory Postman_Tests for import into Postman

Use the following tokens associated with the different availabel roles and permissions

name: Casting_Assistant@udacity.com
password: Casting_Assistant
Last JWT: 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZzSkhVTGN1ZW9xYTMxcWhuSTM0TyJ9.eyJpc3MiOiJodHRwczovL2Rldi1temNzbTFzcnBleXR3aTUxLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2ODZhZTdhNWQ4MmRjOWMxNmNmOWMzNWYiLCJhdWQiOiJBZ2VuY3kiLCJpYXQiOjE3NTE5NzYxNzYsImV4cCI6MTc1MTk4MzM3Niwic2NvcGUiOiIiLCJhenAiOiI1TTYwc1dRcVBZT3dwb2RsNEx0blozMFVLSHRCaUhNNSIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.pUmtYTakE9DZPkMX-MP3LpN-8b3mYFyjD74SiKtGdZ_Ha8XuqvZaujT9lve4eHTu-b1PaJBMGVUqoA8BnkaZhoeLNwffUcYR2Q07NtJ_D2Y0MwcNjGYk3yF0w9H0aU4E7swk_eblGRqhLkv38o_jnxPEGlI_FNoKa3dRHiGL5zzFfWYbcR8s7RLqDCF75gJvKdbcmUjB30qW7EwpXTDr5Ni2pr6udDaqsgM9HWbEJmFXi-nTN7QIKQ6mAdbkH9wPuhemapWya1TNu-_rSaDhmB1FPSutxUyldXdKqhnoCYI0buV5KcgsxsEEtBEmhCgVNlBu5Xj3olIpKK1lRR8DyQ

name: Casting_Director@udacity.com
password: Casting_Director
Last active JWT: 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZzSkhVTGN1ZW9xYTMxcWhuSTM0TyJ9.eyJpc3MiOiJodHRwczovL2Rldi1temNzbTFzcnBleXR3aTUxLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2ODZhZTc4MDE0NjZlODY4MTgzZmI4YzMiLCJhdWQiOiJBZ2VuY3kiLCJpYXQiOjE3NTE5NzYyMTUsImV4cCI6MTc1MTk4MzQxNSwic2NvcGUiOiIiLCJhenAiOiI1TTYwc1dRcVBZT3dwb2RsNEx0blozMFVLSHRCaUhNNSIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.BblL4-23AUwyrl9Zix0zwdk-kDV6pvGdOq320k3NPl08Z1VBbt4NHOKFvxJGl4PlO19Zhfz6I3ayuJkh1uRsVGnA-PgmRjgMHOEzGp8JSLe1d3_LmX-b5AfnC5iXkt4oSoC1enE-t7B6RS9c0m9IuEZByvnraHfjOzpbl4URTLR7HhpUdOT6Z5kEOrkscmf8RjYRy08bRj7SJXXam9skr2VDqV5KO9TMdhUd8o2UA5adkhnuTWnfbeE3WND1tSZbKcO4SQIwj_keKUR9riv0dRkbR2OLGSOVqtLKNIw_mLQ2FsXM9Ow1rLzRO3S7tE31Qwxa_rg59S7wbmTjJC3POQ


name: Executive_Producer@udacity.com
password: Executive_Producer
Last active JWT:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZzSkhVTGN1ZW9xYTMxcWhuSTM0TyJ9.eyJpc3MiOiJodHRwczovL2Rldi1temNzbTFzcnBleXR3aTUxLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2ODZhZTc1NzcxMGVkZWNhYzU4Y2JiNWIiLCJhdWQiOiJBZ2VuY3kiLCJpYXQiOjE3NTE5NzYyNjAsImV4cCI6MTc1MTk4MzQ2MCwic2NvcGUiOiIiLCJhenAiOiI1TTYwc1dRcVBZT3dwb2RsNEx0blozMFVLSHRCaUhNNSIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.ld7rISWy-IgPfF3L8NrZDBJHPQm8BckqdQZuofsgC-c8TmDXE1gz2dWBBupkszva8khYzGgc_n_ZyvSHHyp6JN31IeBO42NKztf5valAEWLZZGePtk2e9KYMJUjKSbkFvR2mOQxLy3nRtD8DCu6UVpFQl-5FyfNvUn-AsF0iTzK99bk0X-Zwvyx2nUexC3fotTIY_5qlG_myQ15nSmpCEIkdlhcuJPmo5Pbg9pxzS7YbjXNKNoMs9ZryNJFzO3CQVXJiOXbqJKY4KI1FyfekVV55R5rroB1f_QjS4t-UUyl9H31yWsl-f-yPkiwnItcK3-PFZcI7a8groXKsJTtPlA