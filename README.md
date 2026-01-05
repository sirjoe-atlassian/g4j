# g4j - ExpressJS API Application

* GT-1 change

## Description

This is an ExpressJS skeleton application that provides RESTful API endpoints.

## Prerequisites

- Node.js (v14 or higher)
- npm (Node Package Manager)

## Installation

1. Clone the repository
2. Install dependencies:
```bash
npm install
```

## Running the Application

### Development Mode (with auto-reload)
```bash
npm run dev
```

### Production Mode
```bash
npm start
```

The server will start on port 3000 by default (or the port specified in the PORT environment variable).

## API Endpoints

### 1. GET /helloworld

Returns a simple "Hello World" message.

**Request:**
```
GET /helloworld
```

**Response:**
```json
{
  "message": "Hello World!",
  "timestamp": "2024-01-01T12:00:00.000Z"
}
```

**Status Codes:**
- `200 OK` - Success

---

### 2. GET /health

Health check endpoint to verify the server is running.

**Request:**
```
GET /health
```

**Response:**
```json
{
  "status": "ok",
  "uptime": 123.456
}
```

**Status Codes:**
- `200 OK` - Server is healthy

---

## Error Responses

### 404 Not Found
When accessing an undefined endpoint:
```json
{
  "error": "Not Found",
  "message": "Cannot GET /undefined-endpoint"
}
```

### 500 Internal Server Error
When a server error occurs:
```json
{
  "error": "Internal Server Error",
  "message": "Error details"
}
```

## Project Structure

```
.
├── server.js          # Main application file
├── package.json       # Project dependencies and scripts
├── .gitignore        # Git ignore rules
└── README.md         # This file
```

## Testing the API

You can test the API using:

**cURL:**
```bash
curl http://localhost:3000/helloworld
```

**Browser:**
Visit `http://localhost:3000/helloworld`

**Postman or similar API client:**
Create a GET request to `http://localhost:3000/helloworld`
