
# Agency Data View

## Background

The project is taken over from an exercise within the udacity nano degree training. The frond-end is taken over from the COffee-Shop project. Therefore tool-environment, design and architecture are identical

## Getting Setup

> _tip_: this frontend is designed to work with [Flask-based Backend](../backend). It is recommended you stand up the backend first, test using Postman, and then the frontend should integrate smoothly.

### Installing Dependencies

#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

> _note_: If you are using Node.js version 17 or above, you might encounter issues due to OpenSSL changes. Use the following environment variable to avoid these issues:

```bash
export NODE_OPTIONS=--openssl-legacy-provider
```

#### Installing Ionic Cli

The Ionic Command Line Interface is required to serve and build the frontend. Instructions for installing the CLI is in the [Ionic Framework Docs](https://ionicframework.com/docs/installation/cli).

```bash
sudo npm install -g @ionic/cli
```

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

> _note_: If you encounter issues with `node-sass`, ensure `sass` is installed instead:

```bash
npm uninstall node-sass
npm install node-sass@4.14.1
```
> _tip_: **npm i** is shorthand for **npm install**

> _note_: If you encounter an error related to python2 while installing dependencies, you might need to install Python  Use the following command if necessary:
```bash
brew install python@2
```

## Required Tasks

### Configure Environment Variables

Ionic uses a configuration file to manage environment variables. These variables ship with the transpiled software and should not include secrets.

- Open `./src/environments/environments.ts` and ensure each variable reflects the system you stood up for the backend.

## Running Your Frontend in Dev Mode

Ionic ships with a useful development server which detects changes and transpiles as you work. The application is then accessible through the browser on a localhost port. To run the development server, cd into the `frontend` directory and run:

```bash
export NODE_OPTIONS=--openssl-legacy-provider
ionic serve
```

> _tip_: Do not use **ionic serve** in production. Instead, build Ionic into a build artifact for your desired platforms.
> [Checkout the Ionic docs to learn more](https://ionicframework.com/docs/cli/commands/build)

## Key Software Design Relevant to Our Coursework


### Available Users

Including corresponding passwords..

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